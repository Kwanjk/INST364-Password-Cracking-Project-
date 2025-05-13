# 🔐 Password-Security Simulator (2025 Final Prototype)

This is an interactive educational simulation designed to **visually and experientially demonstrate the dangers of weak or reused passwords** in small to mid-sized organizations. Built with Streamlit, this prototype enables users, especially non-expert employees, to test password strength, explore real-world attack scenarios, and receive actionable coaching. The tool is grounded in cybersecurity principles and human-centered frameworks, specifically **Mental Models** and **Bounded Rationality**.

---

## Audience & Goals 

Front-line employees in small–mid-sized organizations who have little formal security training and often reuse passwords for convenience.  
Our aim: let them *see*—in under five minutes—how a single leaked password can cascade into multiple account takeovers, then give them a friction-free path to safer habits. 

---

## Focus (one tech topic, one human topic) 
*Tech lens*: **Password Cracking** — brute-force, dictionary, and credential-stuffing attacks.  
*Human lens*: **Bounded Rationality** — sliders, presets, and color-coded feedback replace mental math so the secure option is also the easiest.

---

## 🎯 Project Objective

Most password-compromise incidents don’t result from sophisticated malware or zero-day exploits. They stem from **predictable human behavior**, like reusing passwords across platforms or assuming that "slightly changing" a password keeps it secure. This simulator demonstrates how these common behaviors are **easily exploited through password cracking techniques** such as:

- **Brute-force attacks**
- **Dictionary attacks**
- **Credential stuffing**

The app is meant to serve as both a **teaching tool and behavior changer**, offering immediate feedback that corrects misconceptions while respecting users' limited time, attention, and cognitive bandwidth.

---

## 🧠 Human-Centered Design Philosophy

The design of this simulator is guided by two behavioral frameworks discussed throughout the course:

### Myth-Busting Messages (supporting Bounded Rationality)

Each tab ends with a one-sentence myth-buster (e.g., “One leak ⇒ all reused accounts fall”) to correct common password misconceptions without adding extra mental effort.

### Bounded Rationality

Rather than acting fully rationally, users take **shortcuts** based on attention, time, or memory constraints:
- Reusing passwords instead of creating new ones.
- Ignoring password managers due to perceived complexity.
- Choosing passwords they can recall easily instead of ones resistant to cracking.

This simulator meets users **where they are**, offering clear, low-friction interfaces (sliders, preset buttons, visual feedback) that deliver insights **without cognitive overload**.

---

## 🧪 Core Features

### 🔹 1. **Password Strength Tester**
- Uses the `zxcvbn` password estimation library to assess entropy, dictionary hits, and estimated crack time.
- Displays comparative results for **offline brute-force attacks** (1 billion guesses/sec [hashcat2025]) and **online attacks** (10,000 guesses/sec).
- Visually shows how even long passwords can fail if they contain predictable patterns (e.g., `Password1`).
- Ends each result block with a **myth-busting tip** aligned with common user misconceptions.

---

### 🔹 2. **Reuse Blast Radius**
- Models how reusing the **same password across multiple accounts** compounds risk.
- Takes into account the **probability of breach per site** to show how *one leak* compromises *many logins*.
- Uses math-based probability but renders it via **sliders and progress bars** for accessibility.
- Reinforces the idea that unique passwords act as **firewalls between services**.

---

### 🔹 3. **Credential-Stuffing Simulator**
- Simulates a real-world **attack wave** on an organization where some employees’ credentials are already in public breach databases.
- Calculates how many users are at risk based on:
  - Total users in the organization
  - % of staff reusing passwords
  - % of staff already in a breach
- Demonstrates how attackers succeed by **exploiting reused credentials**, not brute-force complexity.
- Reinforces **bounded rationality** by showing the magnitude of consequences through **simple sliders**.

---

### 🔹 4. **Best-Practice Coach**
- Provides instant generation of strong, random passwords using secure entropy sources.
- Offers curated, actionable advice:
  - Use of password managers
  - When to rotate passwords
  - MFA recommendations
- Highlights free/open-source tools (Bitwarden, KeePassXC) for low-barrier adoption.

---

## 🧪 Anticipated User Reactions & Learning Outcomes

Based on behavioral research and class frameworks, we anticipate:

### 🔸 Initial Reaction:
- Curiosity about how strong their existing password is.
- Surprise when familiar patterns (e.g., `qwerty123`, `Welcome2024`) fail instantly.

### 🔸 Cognitive Conflict:
- Users will experience **dissonance** when they see how quickly a reused or "tweaked" password is cracked.
- This aligns with **conceptual change theory**, confronting flawed mental models with credible, visible evidence.

### 🔸 Behavioral Intention Shift:
- Clear, low-effort simulations lower the barrier to adopting better practices.
- Sliders offer a **risk-cost feedback loop** without needing technical knowledge.
- Users begin to view password managers not as a hassle but as a **necessary firewall**.

---

## 📊 Why This Matters for Small-Mid Organizations

- These orgs are least likely to employ full-time cybersecurity staff.
- Employees are often **trained once and expected to remember forever**.
- This simulator complements formal training with **experiential learning**, enabling:
  - Visual consequence modeling
  - Habit-based nudges
  - Trustworthy, minimalistic coaching

---

## ⚙️ Tech Stack

- `Python`
- `Streamlit`
- `zxcvbn` (password strength estimator)
- `Altair` (visualization)
- `pandas`, `math`, `secrets` (data + secure generation)

---

## 🧩 Future Work

- Add **report download** option with personalized feedback summary.
- Introduce **attack visualization** (e.g., animated brute-force attempts).
- Integrate **role-specific simulations** (e.g., finance manager vs. intern) to personalize behavior risks.

---

## 📬 Final Thought

> "You don’t need to be a security expert.  
> You just need to *see* why good habits beat good intentions."

This simulator turns invisible threats into visible lessons, empowering users to build stronger password habits within the limits of human behavior.

---

## 🚀 How to Run the Simulator Locally

> **Prerequisites**:  
> • Python 3.9+  
> • Git (optional, for cloning)  
> • A modern web browser

1. **Clone or download the repository** (You can just copy the code into Python/VS Code)  
2. **Install dependencies**
   ```bash
   pip install streamlit zxcvbn altair pandas
3. **Run the app**
   ```bash
   streamlit run streamlit_app.py

---

## References 

[hashcat2025]  Hashcat v6.2.6 benchmark results on NVIDIA RTX 4090, run 2025-04-01.  
[rockyou2017]  RockYou plaintext password corpus (10 M entries). 2017 breach archive.  
[zxcvbn2014]   Wheeler, D. “zxcvbn: Low-budget password-strength estimation.” USENIX 2014.  
[NIST-63b]     NIST Special Publication 800-63b — Digital Identity Guidelines. June 2017.  

© 2025 Password‑Security Simulator | Educational use only | No data is collected or sent
