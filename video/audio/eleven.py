"""One-shot ElevenLabs generation for the Moorline promo sound. Existing files are never regenerated.
python audio/eleven.py   -> audio/src/*.mp3, prints credits spent."""
import json, os, sys, time, urllib.error, urllib.request
from pathlib import Path

SRC = Path(__file__).resolve().parent / "src"
API = "https://api.elevenlabs.io/v1"
STYLE = "clean close-miked studio recording, single sound, no music, no voice, modern tech product UI sound design"
SFX = {  # name -> (prompt, seconds)
    "whoosh": ("fast tight air whoosh, quick whip pan swish", 0.6),
    "rope": ("a rope thrown fast through the air, taut zip then a soft tight snap as it catches", 1.0),
    "strike": ("single crisp marker strike-through swipe on paper, short dry swish", 0.5),
    "tick": ("tiny soft digital UI tick, clean glassy click", 0.5),
    "qr": ("rapid soft digital data chirps scanning, short pixel blips accelerating", 1.0),
    "check": ("warm clean two-note confirmation chime, modern app success", 0.8),
    "hit": ("deep cinematic logo impact hit, short punchy sub boom with a clean metallic ring tail", 2.5),
}
MUSIC = {
    "positive_global_styles": ["modern minimal electronic", "tech product launch", "clean punchy drums", "deep sub bass",
                               "plucky synth arpeggio", "instrumental", "112 bpm", "confident and warm"],
    "negative_global_styles": ["vocals", "lo-fi", "orchestral", "epic trailer", "dubstep wobble", "guitar"],
    "sections": [
        {"section_name": "Intro", "positive_local_styles": ["sparse pulsing synth", "filtered kick", "anticipation"],
         "negative_local_styles": ["full drums"], "duration_ms": 4600, "lines": []},
        {"section_name": "Drive", "positive_local_styles": ["full groove", "driving four on the floor", "bright arpeggio"],
         "negative_local_styles": ["breakdown"], "duration_ms": 14900, "lines": []},
        {"section_name": "Lift", "positive_local_styles": ["drums thin out", "rising filter sweep", "tension builds"],
         "negative_local_styles": ["drop"], "duration_ms": 6600, "lines": []},
        {"section_name": "Final hit", "positive_local_styles": ["one big final chord hit on the downbeat", "then sustained chord ringing out to silence"],
         "negative_local_styles": ["drums continuing", "new melody"], "duration_ms": 3400, "lines": []},
    ],
}


def key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if not k:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as r:
            k = winreg.QueryValueEx(r, "ELEVENLABS_API_KEY")[0]
    return k.strip()


def opn(req, timeout):
    for k in range(5):  # this network drops connects now and then
        try:
            return urllib.request.urlopen(req, timeout=timeout)
        except urllib.error.HTTPError:
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            if k == 4:
                raise
            print("  retry", e)
            time.sleep(5)


def used():
    req = urllib.request.Request(f"{API}/user/subscription", headers={"xi-api-key": key()})
    d = json.load(opn(req, 60))
    return d["character_count"], d["character_limit"]


def post(path, body, out):
    req = urllib.request.Request(f"{API}/{path}", data=json.dumps(body).encode(), method="POST",
                                 headers={"xi-api-key": key(), "Content-Type": "application/json", "Accept": "audio/mpeg"})
    for k in range(4):
        try:
            out.write_bytes(opn(req, 600).read())
            print("  ok", out.name)
            return
        except urllib.error.HTTPError as e:
            if e.code != 429 or k == 3:
                sys.exit(f"{out.name}: HTTP {e.code} {e.read().decode()[:400]}")
            time.sleep(10 * (k + 1))


if __name__ == "__main__":
    SRC.mkdir(parents=True, exist_ok=True)
    c0, lim = used()
    print(f"credits used {c0}/{lim}")
    if "--check" in sys.argv:
        sys.exit()
    for name, (text, dur) in SFX.items():
        if not (SRC / f"{name}.mp3").exists():
            post("sound-generation?output_format=mp3_44100_128",
                 {"text": f"{text}. {STYLE}", "duration_seconds": dur, "prompt_influence": 0.6}, SRC / f"{name}.mp3")
    if not (SRC / "music.mp3").exists():
        post("music?output_format=mp3_44100_192", {"composition_plan": MUSIC}, SRC / "music.mp3")
    c1, _ = used()
    print(f"spent {c1 - c0}, left {lim - c1}")
