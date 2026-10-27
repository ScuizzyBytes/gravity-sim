<div align="center">

<h1>🌌 gravity-sim</h1>

<p><b>Two balls pulled together by gravity.</b><br>
Built with Python and pygame.</p>

</div>

---

## ✨ Features

- 🔴🔵 Two balls attract each other (Newton's law of gravitation)
- 🧱 Bounce off the walls
- 🚦 Speed limit so nothing flies away

## 🧠 How it works

Every frame:

1. Find `dx`, `dy` and the distance `r` between the balls
2. Compute force: `F = G * m1 * m2 / r²`
3. Split it into x and y with `cos` and `sin` of the angle (`atan2`)
4. Add it to the velocity, then move the balls

## ⚙️ Settings

| Variable | What it does |
|----------|--------------|
| `G` | strength of attraction |
| `MASS`, `MASS2` | mass of each ball |
| `MAX_V` | speed limit |

## 🚀 Run

```
pip install pygame
python3 Atom.py
```
