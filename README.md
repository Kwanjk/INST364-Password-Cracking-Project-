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
| **2** | **Reuse Blast Radius** | One leak → many accounts. Formula: `ceil(n·[1 – (1–p)^n])`. |
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
