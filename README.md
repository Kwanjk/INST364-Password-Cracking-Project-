# 🔐 Password‑Security Simulator (2025 Final Prototype)

Interactive Streamlit app that lets non‑expert employees **see** why weak or reused passwords crumble under real‑world attacks—and how small habit changes slash risk.

- **Bounded Rationality:** sliders/presets respect limited attention; visuals remove math barriers.  
- **Mental‑Model Nudges:** each output ends with a myth‑buster that corrects common misconceptions.

---

## 🎯 Project Objective

Most password‑compromise incidents don’t result from exotic zero‑day exploits; they arise from **predictable human behavior**—reusing passwords or assuming small tweaks (“Password1 → Password2”) suffice.  
This simulator shows how these habits are exploited through:

| Technique | What Attackers Do |
|-----------|------------------|
| **Brute‑force** | Systematically try every combination. |
| **Dictionary** | Test high‑probability words/phrases from leaked lists (e.g., *rockyou*). |
| **Credential Stuffing** | Replay usernames + passwords from past breaches on new sites. |

The tool delivers **immediate, visual feedback** that corrects misconceptions while respecting users’ limited time, attention, and cognitive bandwidth.

---

## 🧠 Human‑Centered Design Philosophy

### 1. Mental Models
Users rely on simplistic metaphors:
* “Long = strong.”  
* “I’ve never been hacked, so I’m safe.”  
* “Adding ‘123!’ makes it secure.”  

We surface *why* these models fail (blast‑radius math, live crack times).

### 2. Bounded Rationality
Memory limits → reuse; perceived hassle → skip managers.  
The UI employs low‑friction sliders, one‑click buttons, and color‑coded feedback to fit real cognitive constraints.

---

## 🧪 Core Features

| # | Tab | Key Insight |
|---|-----|-------------|
| **1** | **Password Strength Tester** | Shows entropy, dictionary hit, and crack times (GPU vs. web). |
| **2** | **Reuse Blast Radius** | One leak → many accounts. Formula: `math.ceil(n * (1 - (1 - p)**n))`. |
| **3** | **Credential‑Stuffing Wave** | Overlap math reveals org‑wide fallout from reuse × breaches. |
| **4** | **Best‑Practice Coach** | One‑click random password + links to Bitwarden / KeePassXC; MFA tips. |

---

## 👥 Anticipated User Journey

1. **Hook** – Test a familiar password → instant fail.  
2. **Explore** – Drag sliders, watch risk bars spike.  
3. **Reflect** – Myth‑buster captions correct mental models.  
4. **Act** – Generate strong password, install manager.  
5. **Share** – Screenshots circulate in team chat → viral learning.

---

## 📊 Why It Matters for Small‑Mid Orgs
* Few dedicate full‑time security staff.  
* Annual training quickly fades.  
* Simulator supplies *experiential* reinforcement with zero admin overhead.

---

## ⚙️ Tech Stack
* Python 3.9+ │ Streamlit │ zxcvbn │ Altair │ pandas │ math │ secrets

---

## 🚀 Quick Start

```bash
git clone https://github.com/your‑org/password‑sim.git
cd password‑sim

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install streamlit zxcvbn altair pandas

streamlit run streamlit_app.py       # open localhost:8501

---

## 🛠️ How the Code Works & Why It Matters

| Block / Function | Purpose in Code | Pedagogical Pay‑Off |
|------------------|-----------------|---------------------|
| **`load_common()`**<br>`@st.cache_data` | Loads the top _​N_ leaked passwords (RockYou subset) and caches them. | Powers the **“Dictionary Hit?”** flag—users instantly see when their password is already public. |
| **Entropy & Brute‑Force Math**<br>`brute_seconds()` | Calculates average crack time: \|pool\|<sup>length</sup> / rate ÷ 2 (half‑search expectation). | Visualizes the exponential benefit of adding length/char‑classes (bounded rationality: slider shows impact without math). |
| **Time Formatter**<br>`fmt_dur()` | Converts raw seconds into human units (min, h, d, y, > 1 M y). | Removes mental arithmetic; prevents “2.4 e8 s” confusion. |
| **`strong_pw()`** | Generates a cryptographically‑secure 128‑bit password via `secrets.choice()`. | Demonstrates an *actionable* fix—one click, no theory required. |
| **Strength Tester Tab**<br>`zxcvbn(pwd)` | Combines corpus stats & heuristic patterns (keyboard walks, dates). | Gives realistic feedback instead of naïve length rules; caps off with myth‑buster tips. |
| **Log‑Scale Altair Chart** | Plots crack seconds (online 10 k/s vs. offline 1 B/s GPU). | Milliseconds vs. millennia visual shock breaks overconfidence. |
| **Reuse Blast Radius** | Formula: `ceil(n · [1 – (1–p)^n])` → expected accounts lost if any site leaks. | Converts abstract probability into **“X / Y accounts fall”**—users grasp the cascade. |
| **Credential‑Stuffing Wave** | Inclusion‑exclusion: `breached + reused – overlap`. | Shows how reuse × previous breaches equals org‑wide compromise; slider makes trade‑offs salient. |
| **Best‑Practice Coach** | One‑click random password + links to Bitwarden / KeePassXC; NIST SP 800‑63b guidance. | Bridges insight → action (bounded rationality fix); dispels 90‑day‑rotation myth. |
| **Footer (“No telemetry”)** | States nothing is sent off‑box. | Builds trust; addresses privacy mental models. |

### Dictionary‑Match Logic
`zxcvbn` scans the password’s _sequence_ list. If any substring ranks ≤ 10 000 in the leaked dictionary, **Dictionary Hit? = Yes** and the effective crack time drops to seconds—showing why “Password1” is doomed even at 9 characters.

### Reuse Blast‑Radius Calculation
Probability that **at least one** of _n_ services breaches in a year:  
&nbsp;&nbsp;`P = 1 – (1 – p)^n`  

Expected accounts lost = `ceil(n · P)`  

> **Interpretation:** with 5 reused accounts and a 15 % breach chance each, you’re likely to lose ~3 accounts from a single leak.

### Credential‑Stuffing Overlap
* `breached` = users already in public dumps.  
* `reused` = users who reuse passwords.  
* `overlap` = employees in both groups.  
* `compromised = breached + reused – overlap` avoids double‑counting, yielding a realistic attacker success figure.

### Coach Output Significance
* **Random passwords** leverage crypto‑secure randomness—~128 bits of entropy.  
* Open‑source manager links lower cost & trust barriers.  
* NIST guidance (“change only on compromise”) corrects outdated rotation policies.

---

## 🔄 Future Work
* Export personal PDF/CSV reports for compliance.  
* Animated brute‑force timeline for live workshops.  
* Role‑specific modules (finance, HR, dev, intern).

> *“See your passwords through a hacker’s eyes—then never reuse one again.”*

© 2025 Password‑Security Simulator | Educational prototype | **No telemetry**
