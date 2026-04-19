<div align="center">

<img width="100%" alt="header" src="https://capsule-render.vercel.app/api?type=waving&height=210&text=yuurisan-lib&fontAlign=50&fontAlignY=36&fontSize=64&desc=Shared%20Utility%20Library%20by%20Yuurisandesu&descAlign=50&descAlignY=58"/>

<img alt="typing" src="https://readme-typing-svg.demolab.com?font=Inter&size=18&duration=3000&pause=650&center=true&vCenter=true&width=900&lines=Auto+Banner+%7C+Terminal+Title;Plug+and+Play+for+All+Yuuri+Bots"/>

<p>
  <img alt="python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white"/>
  <img alt="type" src="https://img.shields.io/badge/Type-Library-111111"/>
  <img alt="license" src="https://img.shields.io/badge/by-Yuurisandesu-111111"/>
</p>

<p>
  <b>yuurisan-lib</b> is a lightweight shared utility library used across all Yuuri bots.<br/>
  Provides a reusable banner and terminal title setter so every bot looks consistent.<br/>
  Built and distributed by <b>Yuurisandesu</b>.
</p>

</div>

---

## ⚙️ Requirements

- Python `3.10+`

---

## 🚀 Installation

**Direct Install (Recommended):**

```bash
pip install git+https://github.com/Yuurichan-N3/Yuurisan-lib.git
```

**From source:**

```bash
git clone https://github.com/Yuurichan-N3/Yuurisan-lib.git
cd Yuurisan-lib
pip install .
```

---

## 📦 Usage

```python
from yuurisan_lib import banner, set_title

set_title("My Bot")
banner("My Bot")
```

This will clear the terminal, print the Yuurisandesu ASCII banner, and set the terminal tab title to `My Bot by : 佐賀県産 (YUURI)`.

---

## ✨ Functions

`banner(nama_bot)` — Clears the terminal and prints the styled ASCII banner with bot name and current timestamp.

`set_title(nama_bot)` — Sets the terminal tab title to `{nama_bot} by : 佐賀県産 (YUURI)`.

---

## 🗂️ File Structure

```text
Yuurisan-lib/
├── yuurisan_lib/
│   └── __init__.py
├── setup.py
└── README.md
```

---

<div align="center">
<img width="100%" alt="footer" src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer"/>
</div>