# Review: Moorline promo v1

- Picked storyline: "one rope, everything crosses it". It opens with type and objects, then one stage keeps rebuilding as each module sends something across the rope, then come trust, size and the end card. Two storylines were not built: a "day in the life" (a person, timestamps) and an "endless zoom" through the helm mark.
- Measured: `check` passes with 0 errors. Frame-diff motion scan at 10 fps (`motion.py`): the only still stretches are 0.7–1.1 s (the phone hero settling) and the final 2 s end-card hold, which carries a flowing rope. Snapshots were checked at the beats, and frame strips around every seam.
- Warnings kept on purpose:
  - `film_silent`: sound needs approval for ElevenLabs credits.
  - `text_below_floor`: these are UI labels inside the drawn screens, not lines meant to be read.
  - `composition_file_too_large` (modules.html): one stage on purpose.
- The screens are rebuilt from the product's components in English. The real Helm UI is Turkish and renders empty without a backend, so it was not captured directly.
- Weakest shot: the Ekran+Kamera beat squeezes two features into 1.5 s. The secure-scene opening has 0.3 s with only the phone on screen.
- With more time: a sound pass (rope "zip" and clicks), a cursor or finger on taps, and real Moorline screenshots once English UI strings exist.
