GOAL:    viewer gets "my iPhone and my PC, tied together locally, nothing else" and remembers the name Moorline.
OUTPUT:  HyperFrames, 1920 x 1080, 30 fps render (silent) + sound muxed by audio/mix.py (video stream copied). GIF stays silent.
TIME:    28.9 s x 30 = 867 frames
REFS:    Apple launch films -> giant kinetic type that slams and then holds dead still, hard cut on the fastest frame.
         Linear -> one clear promise, strict left grid, restraint, product pieces isolated big.
         Raycast (kinetic product motion) -> rebuilt UI pieces doing real actions fast, object-to-object chain.
LOOK:    ground #0c0d0f + 48 px grid at 3.5% white (from banner.svg); surfaces #16181c/#1d2025; lines #3a3e46;
         ink #F2F3F5, quiet #8E939B; accent #F0553A (rope, strikes, hub) and #ff8a5c only on the rope gradient.
         Inter 900, -4% tracking for display (150-300 px); Inter 700 for lines (64-72 px). No glow, no glass.
OBJECTS: iPhone (280x580, r48, island), PC monitor (720x450 + neck + base), the mooring rope (orange cubic + dotted
         overlay, knots at both ends), Moorline helm mark (traced from the iOS app icon), module icons from assets/icons.
MOTION:  enter expo.out 0.25-0.4 s with blur 8-16 px; camera/flood power2.inOut; zoom-through/exit power3.in 0.25-0.3 s;
         words 0.07 s apart; titles land and hold still.
SHOTS:   hook 0-4.6      "Your iPhone." / whip / "Your PC." / rope thrown between them, "Moored over your home network." -> zoom through rope
         nocloud 4.6-7.5 Cloud. Account. Telemetry. Auto-start. each struck by the orange line; "Just your home network." -> whip up
         modules 7.5-18.9 one stage that rebuilds: Goz, Conch, Wake, Ekran+Kamera, Kumanda, Sync, Siri, something crosses the rope each beat -> PC leaves, phone carries on
         secure 18.9-22.5 phone draws the pairing QR, "Pair once." + four security lines -> iris from the checkmark floods orange
         idle 22.5-25.1  on orange: "~3 MB" "0% CPU", tray bar slides up -> orange irises down into the hub
         end 25.1-28.9   helm mark builds from its hub, "Moorline" + tagline hold 2.4 s
BANNED:  floating void with small centred things, glow/bloom, glass cards, three cards in a row, logo docked in a corner,
         fade+slide-up on everything, text moving while read, emoji, Turkish copy on screen (module proper names excepted).
QA:      frames 0.1, 1.5, 3.8, 5.8, 8.5, 10, 12, 13.5, 15, 16.5, 18, 20.5, 23.5, 27.5; no frozen >1.5 s, no text cut.
SOUND:   ElevenLabs (audio/eleven.py, one take each): music bed (composition plan, drives to ~26.3 s and stops on the logo),
         SFX whoosh/rope/strike/tick/qr/check/hit in audio/src. Cue times in audio/mix.py come from the scene timelines.
         python video/audio/mix.py <silent.mp4> <out.mp4> -> -14 LUFS, -2 dBTP target, video bit-identical.
