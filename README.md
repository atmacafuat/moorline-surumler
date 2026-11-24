<p align="center">
  <img src="assets/banner.svg" alt="Moorline — your iPhone, moored to your PC" width="100%">
</p>

<p align="center">
  <a href="https://github.com/atmacafuat/moorline-surumler/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/atmacafuat/moorline-surumler?style=flat-square&color=F0553A&label=latest"></a>
  <img alt="Windows 10/11" src="https://img.shields.io/badge/Windows-10%20%7C%2011-3a3e46?style=flat-square">
  <img alt="iPhone" src="https://img.shields.io/badge/iPhone-companion-3a3e46?style=flat-square">
  <img alt="No cloud" src="https://img.shields.io/badge/cloud-none-3a3e46?style=flat-square">
  <img alt="Signed updates" src="https://img.shields.io/badge/updates-signed-3a3e46?style=flat-square">
</p>

<h3 align="center">Your iPhone, moored to your PC.</h3>

<p align="center">Files, music, a webcam, a second screen and a remote, passed between your iPhone and your Windows PC<br>over your own network. No cloud, no account, no telemetry.</p>

<p align="center">
  <a href="https://github.com/atmacafuat/moorline-surumler/releases/latest"><b>Download for Windows</b></a>
  &nbsp;·&nbsp;
  <a href="https://atmacafuat.github.io/moorline-surumler/">Website</a>
</p>

<p align="center">
  <a href="assets/moorline-promo.mp4"><img src="assets/moorline-promo.gif" alt="Moorline in action (click for the full video)" width="100%"></a>
</p>

## Modules

<table>
  <tr>
    <td width="25%" valign="top"><img src="assets/icons/goz.svg" width="40" alt=""><br><b>Göz</b><br>Share a Reel, Short, photo or link from the phone. The PC saves it, transcribes it and turns it into notes.</td>
    <td width="25%" valign="top"><img src="assets/icons/conch.svg" width="40" alt=""><br><b>Conch</b><br>Phone music on PC speakers. Now playing, controls, its own volume, and a tiny overlay that never steals game focus.</td>
    <td width="25%" valign="top"><img src="assets/icons/wake.svg" width="40" alt=""><br><b>Wake</b><br>Drop files either way. Batch sends with per-file progress; only the failed ones retry.</td>
    <td width="25%" valign="top"><img src="assets/icons/ekran.svg" width="40" alt=""><br><b>Ekran</b><br>Your iPhone as a second screen.</td>
  </tr>
  <tr>
    <td valign="top"><img src="assets/icons/kamera.svg" width="40" alt=""><br><b>Kamera</b><br>Your iPhone camera as the PC's webcam.</td>
    <td valign="top"><img src="assets/icons/kumanda.svg" width="40" alt=""><br><b>Kumanda</b><br>Launch apps, set the volume, lock the PC from the phone. Every action is off until you allow it.</td>
    <td valign="top"><img src="assets/icons/sync.svg" width="40" alt=""><br><b>Sync</b><br>Clipboard both ways, battery level, phone notifications. All opt-in.</td>
    <td valign="top"><img src="assets/icons/siri.svg" width="40" alt=""><br><b>Siri</b><br>"Open Conch", "Send my last photo to my PC", "Lock my PC".</td>
  </tr>
</table>

## Why it stays out of the way

| | |
|---|---|
| **~3 MB, 0% CPU** | One native app (Rust + Tauri). Idles in the tray at about 3 MB of memory and 0% CPU; the window is fully unloaded when closed. |
| **Local only** | Everything stays on your home network. No cloud, no account, no telemetry. |
| **Nothing auto-starts** | No auto-start, no background updater. Updates are signed and checked only when you ask. |
| **Secure by default** | One-time QR pairing, certificate-pinned TLS, per-device tokens stored only as hashes, signed and replay-protected remote commands, deny-by-default permissions. |

## Install

1. Download `Moorline_x.y.z_x64-setup.exe` from the [**latest release**](https://github.com/atmacafuat/moorline-surumler/releases/latest).
2. Run it and open Moorline.
3. Open the Moorline app on your iPhone and scan the pairing QR code once.

Moorline only installs an update whose signature matches the key built into the app.

## Requirements

- Windows 10 or 11, 64-bit, with WebView2 (included in Windows 11)
- An iPhone with the Moorline app, on the same network as the PC

---

<p align="center"><sub>This repository hosts release files and the <a href="https://atmacafuat.github.io/moorline-surumler/">website</a> (<code>docs/</code>). Moorline by <b>optifor</b>.</sub></p>
