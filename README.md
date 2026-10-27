<div align="center">

<h1>gravity-sim</h1>

<p>Two balls, one force. Gravity simulation in Python and pygame.</p>

<img src="screenshot.png" width="400">

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
