# ⚠️ Nature Client Analysis


<p align="center">
  <img src="https://img.shields.io/badge/Status-INSANELY%20SUSPICIOUS-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/VirusTotal-19%2F69-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Threat-TROJAN-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Category-HACKTOOL%20%7C%20PUA-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/File-Launcher.exe-blue?style=for-the-badge">
</p>

---

## 🚨 VirusTotal

| Result           | Value                                               |
| ---------------- | --------------------------------------------------- |
| **Detection**    | **19 / 69** security vendors                        |
| **Threat Label** | `trojan.gametool/filerepmalware`                    |
| **Categories**   | Trojan · PUA · HackTool · GameTool · FileRepMalware |
| **File**         | `Launcher.exe`                                      |
| **Size**         | 21.76 MB                                            |
| **Architecture** | 64-bit PE                                           |

---

## 🔎 What's Suspicious?

### 🎵 Spotify / Account-related strings

A **Minecraft client** containing references to Spotify and account-related APIs is unusual.

| Found                  |
| ---------------------- |
| `accounts.spotify.com` |
| `api.spotify.com`      |
| `open.spotify.com`     |

It also contained:

```text
https://api.spotify.com/v1/me
```


---

### 🎮 Looking for Other Games


The file appears to have accessed paths belonging to **many different games**, while being a literal *Minecraft* client.

| Game / Software found                                        |
| ------------------------------------------------------------ |
| **Genshin Impact** — `genshinimpact.exe`                     |
| **Hitman 3** — `hitman3.exe`                                 |
| **Civilization V** — `CivilizationV_DX11.exe`                |
| **Civilization: Beyond Earth** — `CivilizationBE_DX11.exe`   |
| **Borderlands: The Pre-Sequel** — `borderlandspresequel.exe` |
| **Ghost Recon Phantoms** — `GhostReconPhantoms.exe`          |
| **Vermintide** — `vermintide.exe`                            |
| **Warhammer** — `warhammer.exe`                              |
| **MechWarrior Online**                                       |
| **Total War: Rome II**                                       |
| **Mafia II Definitive Edition**                              |
| **Virtua Tennis 4**                                          |
| **XCOM: Chimera Squad**                                      |
| **Gundam Launcher**                                          |
| **Sudden Attack SEA**                                        |

Contains: 

```text
C:\Users\user\Desktop\genshin impact game\genshinimpact.exe
C:\Users\user\Desktop\retail\hitman3.exe
C:\Users\user\Desktop\CivilizationV_DX11.exe
C:\Users\user\Desktop\Game\PDC-Live\GhostReconPhantoms.exe
C:\Users\user\Desktop\vermintide.exe
C:\Users\user\mafia ii definitive edition.exe
C:\Users\user\Virtua Tennis 4
C:\Users\xcom-chimera-squad\launcher
```

> **Why is a Minecraft client looking through paths for other games?**

---

### 🎮 System information and Anti-Analysis 


| Behavior                        | Analysis    |
| ------------------------------- | ----------- |
| System information discovery    | ⚠️ Detected |
| Anti-debug / analysis detection | ⚠️ Detected |
| Obfuscation                     | ⚠️ Detected |

---

## 📉 FPS / Performance

> **There is a considerable FPS drop when playing with the client injected.**

---

## 🌐 Same Domain, Different Websites

The domain `natureclient.com` was reported to lead to **different websites at different times**, despite using the same URL.

```text
natureclient.com
        ↓
Website A → Real Nature Client

natureclient.com
        ↓
Website B → Polluted / Unofficial Client
```


> Note: I might be wrong here but i experienced this
---

## 🕵️ My Guess 

> **Just a Speculation.**

The client appears to collect **quite a lot of information that can identify the machine/user**, like system and hardware-related information.

It's concerning to say the least

but why does it need this -> *https://accounts.spotify.com/api/token*


**I don't have enough evidence to claim that it can doxx someone**, but I think this is worth investigating before trusting the client.

---

<details>
<summary>📎 File Information</summary>

```text
Launcher.exe

SHA-256:
18eab960e53c3abae8dab0efc833fca7ab568bbb2fd5bc94a515b8f867b3f599

Size:
21.76 MB

Type:
PE Executable (64-bit)
```

</details>

---

## Disclaimer: 
> The analysis was done at 2026-07-23 -> 2026-07-27. Things may have changed as of now.

## 📝 GitHub Note

> **GitHub:** Please don't take this repository down. This might be malware.

> **Client Devs:** I'm **not "LEAKING" the client**. How else can I attach the file?
