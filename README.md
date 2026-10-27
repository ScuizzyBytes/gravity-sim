<div align="center">

<h1>gravity-sim</h1>

<p>Two balls, one force. Gravity simulation in Python and pygame.</p>

<img src="Screenshot from 2026-10-27 17-51-22.png" width="400">

</div>

## How it works

- Balls attract each other by Newton's law: `F = G * m1 * m2 / r²`
- Force is split into x and y with `atan2`, `cos`, `sin`
- Balls bounce off the walls

## Run

```
pip install pygame
python3 Atom.py
```
