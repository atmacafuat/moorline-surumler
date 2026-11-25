"""Mix music + SFX cues into audio/mix.wav (-14 LUFS, -1 dBTP) and mux onto the silent render (video stream copied, frames untouched).
python audio/mix.py <silent.mp4> <out.mp4>. Cue times are absolute seconds taken from the scene timelines (see SPEC.md SOUND)."""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DUR = 29.5
MUSIC_DB = -9          # bed sits under the SFX
MUSIC_FADE = (26.12, 0.3)  # track stops by itself at ~26.3; the logo hit covers the seam
CUES = [  # (sec, file, dB)
    (1.30, "whoosh", -5),   # phone whips out, PC slams in
    (2.33, "whoosh", -7),   # phone back in
    (2.60, "rope", -2),     # rope thrown between them
    (3.10, "tick", -10),    # second knot
    (4.42, "whoosh", -3),   # zoom through the rope
    (4.88, "strike", -5), (5.08, "strike", -6), (5.28, "strike", -5), (5.48, "strike", -6),  # Cloud/Account/Telemetry/Auto-start
    (7.36, "whoosh", -4),   # whip up into modules
    (8.25, "tick", -12), (9.75, "tick", -12), (11.20, "tick", -12), (12.80, "tick", -12),
    (14.30, "tick", -12), (15.70, "tick", -12), (17.20, "tick", -12),  # something crosses the rope each beat
    (19.08, "whoosh", -6),  # PC leaves
    (19.52, "qr", -4),      # phone draws the pairing QR
    (20.65, "check", -3),   # checkmark
    (20.99, "tick", -14), (21.21, "tick", -14),  # last two security lines
    (22.86, "whoosh", -5),  # iris floods orange
    (23.42, "tick", -10), (23.72, "tick", -10),  # ~3 MB, 0% CPU
    (25.80, "whoosh", -6),  # orange irises down into the hub
    (26.08, "hit", -4),      # helm mark hub lands
]


def ff(*a, **k):
    return subprocess.run(["ffmpeg", "-y", "-v", "error", *a], check=True, **k)


def build(out_wav):
    ins, chains = ["-i", str(HERE / "src/music.mp3")], []
    f0, fd = MUSIC_FADE
    chains.append(f"[0:a]aresample=48000,volume={MUSIC_DB}dB,afade=t=out:st={f0}:d={fd}[m]")
    for i, (t, name, db) in enumerate(CUES, 1):
        ins += ["-i", str(HERE / f"src/{name}.mp3")]
        ms = round(t * 1000)
        chains.append(f"[{i}:a]aresample=48000,volume={db}dB,adelay={ms}|{ms}[c{i}]")
    labels = "[m]" + "".join(f"[c{i}]" for i in range(1, len(CUES) + 1))
    mixed = f"{labels}amix=inputs={len(CUES) + 1}:normalize=0,alimiter=limit=0.5:level=false:attack=2:release=60,apad,atrim=0:{DUR}"
    pre = HERE / "_pre.wav"
    ff(*ins, "-filter_complex", ";".join(chains) + ";" + mixed + "[o]", "-map", "[o]", "-ac", "2", "-ar", "48000", str(pre))
    # two-pass loudnorm to -14 LUFS
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", str(pre), "-af", "loudnorm=I=-14:TP=-2:LRA=11:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    m = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
    ff("-i", str(pre), "-af", f"loudnorm=I=-14:TP=-2:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
       f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true",
       "-ar", "48000", str(out_wav))
    pre.unlink()


if __name__ == "__main__":
    src, out = sys.argv[1], sys.argv[2]
    wav = HERE / "mix.wav"
    build(wav)
    ff("-i", src, "-i", str(wav), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
       "-movflags", "+faststart", "-t", str(DUR), out)
