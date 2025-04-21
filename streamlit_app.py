"""
Password‑Security Simulator (2025 Final Prototype)
=================================================
Interactive Streamlit app that lets non‑expert employees see why weak or
reused passwords crumble under real‑world attacks, and how small habit
changes slash risk.

Frameworks highlighted
----------------------
* **Bounded Rationality** – sliders / presets model limited attention; concise
  color‑coded feedback respects cognitive limits.
* **Mental‑Model Nudges** – every output block ends with a one‑sentence myth‑
  buster correcting common misconceptions.

Run
---
    pip install streamlit zxcvbn altair pandas
    streamlit run streamlit_app.py
"""

from pathlib import Path
import math
import secrets
import string

import streamlit as st
import pandas as pd
import altair as alt

# ---------------- Page config -----------------
st.set_page_config(
    page_title="Password‑Security Simulator", page_icon="🔐", layout="centered"
)

# ---------------- Dependencies ---------------
try:
    from zxcvbn import zxcvbn  # type: ignore
except ImportError:
    st.error("Run **pip install zxcvbn** and restart the app.")
    st.stop()

# ---------------- Data helpers --------------
@st.cache_data
def load_common(n: int = 10000):
    """Return top‑N leaked passwords (rockyou subset). If file missing, fallback."""
    p = Path(__file__).with_name("top_100k.txt")
    if p.exists():
        return [line.strip() for line in p.read_text().splitlines()[:n]]
    return [
        "123456", "password", "123456789", "12345678", "qwerty",
        "111111", "abc123", "password1", "iloveyou", "admin",
    ]

COMMON_PWDS = load_common()
ONLINE_GUESS = 1e4   # 10 k/s
OFFLINE_GUESS = 1e9  # 1 B/s

# -------------- Utils -----------------------
CHAR_POOLS = {"lower": 26, "upper": 26, "digit": 10, "symbol": 32}

def brute_seconds(pwd: str, rate: float) -> float:
    """Return average brute‑force crack time (seconds) avoiding OverflowError."""
    pool = sum(
        CHAR_POOLS[key]
        for key, check in [
            ("lower", str.islower),
            ("upper", str.isupper),
            ("digit", str.isdigit),
            ("symbol", lambda c: not c.isalnum()),
        ]
        if any(check(c) for c in pwd)
    ) or CHAR_POOLS["lower"]

    log_combos = len(pwd) * math.log(pool)
    # exp(709) is roughly the max before IEEE float overflow
    if log_combos > 709:
        return float("inf")
    combos = math.exp(log_combos)
    return combos / rate / 2  # average halfway crack


def fmt_dur(sec: float) -> str:
    if sec == float("inf"):
        return "> 1 M years"
    units = [(60, "s"), (60, "min"), (24, "h"), (365, "d"), (1000, "y")]
    val, label = sec, "s"
    for factor, lbl in units:
        if val < factor:
            break
        val /= factor
        label = lbl
    return f"{val:.1f} {label}"


def strong_pw(length: int = 16) -> str:
    alpha = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alpha) for _ in range(length))

# ===== UI =====
st.title("🔐 Password‑Security Simulator")
st.markdown("_No passwords are sent anywhere – all calculations run in your browser._")

T1, T2, T3, T4 = st.tabs([
    "Strength Tester", "Reuse Blast Radius", "Stuffing Simulator", "Coach",
])

# ---------------- Strength Tester ----------
with T1:
    st.header("1. Password Strength Tester")
    pwd = st.text_input("Type a password to test", type="password")
    if not pwd:
        st.info("⬆️ Start typing to see results – one number at a time!")
    else:
        zx = zxcvbn(pwd)
        dict_hit = any(
            seq.get("dictionary_name") in {"passwords", "english"}
            and seq.get("rank", 1e9) <= 10000
            for seq in zx.get("sequence", [])
        )
        guesses      = zx.get("guesses", 1)
        entropy_bits = math.log2(guesses)
        offline      = brute_seconds(pwd, OFFLINE_GUESS)
        online       = brute_seconds(pwd, ONLINE_GUESS)

        # metrics
        c1, c2 = st.columns(2)
        c1.metric("Dictionary Hit?", "Yes" if dict_hit else "No")
        c1.metric("Entropy (bits)", f"{entropy_bits:.1f}")
        c2.metric("Offline GPU", fmt_dur(offline))
        c2.metric("Online 10 k/s", fmt_dur(online))

        # ————— build DataFrame —————
        bar_df = pd.DataFrame({
            "Scenario": ["Offline GPU", "Online 10 k/s"],
            "Seconds":  [offline,      online],
        })

        # ————— new log‑scale point+label plot —————
        base = (
            alt.Chart(bar_df)
               .encode(
                   y=alt.Y("Scenario:N",
                           axis=alt.Axis(title="", labelAngle=0, labelAlign="right")),
                   x=alt.X("Seconds:Q",
                           scale=alt.Scale(type="log"),
                           axis=alt.Axis(title="Crack time (s, log scale)")),
                   color=alt.Color("Scenario:N", legend=None),
                   tooltip=[
                       alt.Tooltip("Scenario:N", title="Attack"),
                       alt.Tooltip("Seconds:Q", format=".2e", title="Seconds")
                   ],
               )
        )
        points = base.mark_point(size=100, filled=True)
        labels = base.mark_text(align="left", dx=7, dy=-7)\
                     .encode(text=alt.Text("Seconds:Q", format=".1e"))
        chart  = (points + labels).properties(height=120)
        st.altair_chart(chart, use_container_width=True)

        if not dict_hit:
            st.markdown(
                ":mag: **Tip:** try `Password1` or `qwerty` to watch an instant failure."
            )


# ---------------- Reuse Blast Radius -------
with T2:
    st.header("2. Password Re‑use Blast Radius")
    acct = st.slider("Accounts protected by the SAME password", 1, 20, 5)
    breach_p = st.slider("Chance one of those services breaches this year (%)", 1, 50, 15)
    p = breach_p/100
    comp = math.ceil(acct * (1 - (1 - p)**acct)) #comp = ⌈ n · [1 – (1–p)^n] ⌉ for more realistic results 

    st.metric("Accounts that fall if just one leaks", f"{comp}/{acct}")
    st.progress(comp / acct)
    st.caption("Even a single breach exposes every reused login.")
    st.warning("**Lesson:** One leak ⇒ all reused accounts gone. Unique passwords = firewalls between services.")

# ---------------- Stuffing Simulator -------
if "stuff_res" not in st.session_state:
    st.session_state.stuff_res = None

with T3:
    st.header("3. Credential‑Stuffing Wave")
    users      = st.number_input("Employees in org",              10, 10000, 250)
    reuse_rate = st.slider("% reusing passwords",    0.0,   1.0, 0.3, 0.05)
    breach_pct = st.slider("% of staff already in breach", 0.0, 0.5, 0.1, 0.05)

    if st.button("Run Wave »"):
        breached    = int(users * breach_pct)
        reused      = int(users * reuse_rate)
        overlap     = int(breached * reuse_rate)
        compromised = breached + reused - overlap
        st.session_state.stuff_res = {
            "breached":   breached,
            "reused":     reused,
            "compromised":compromised,
        }

    if st.session_state.stuff_res:
        res = st.session_state.stuff_res
        df = pd.DataFrame({
            "Category": ["In breach", "Reuse", "Compromised"],
            "Count":    [res["breached"], res["reused"], res["compromised"]],
        })
        st.altair_chart(
            alt.Chart(df).mark_bar(color="#d62728")
             .encode(x="Category", y="Count"),
            use_container_width=True,
        )
        st.error(f"≈ {res['compromised']} / {users} accounts fall to a single stuffing wave.")
        st.caption("Bounded‑rationality note: sliders show trade‑offs quickly without math overload.")


# ---------------- Coach --------------------
with T4:
    st.header("4. Best‑Practice Coach")
    if st.button("Generate strong random password"):
        st.code(strong_pw(), language="text")
    st.markdown(
        """
*Use a password manager → one strong, unique string per site.*  
Free & open‑source options: [Bitwarden](https://bitwarden.com),
[KeePassXC](https://keepassxc.org).

Enable **multi‑factor authentication** wherever available. Rotate passwords
*only* if evidence of compromise (NIST SP 800‑63b).
"""
    )

st.caption("© 2025 Password‑Security Sim | Educational prototype | No telemetry")
