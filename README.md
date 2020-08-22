## The Game of Life Challenge

Your task is to write an implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
You start with a two dimensional grid of cells, where each cell is either alive or dead. The grid is finite, and no life can exist off the edges. When calculating the next generation of the grid, follow these four rules:

1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with more than three live neighbours dies, as if by overcrowding.
3. Any live cell with two or three live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.

Your input is a string representing a starting generation, like this:

```bash
...
.*.
...
```

Your output should be a string representing the next generation of the game.

Successive calls to this should produce successive generations.

For example:

starting input:
```bash
...
***
...
```

first generation output:

```bash
.*.
.*.
.*.
```

second generation output:

```bash
...
***
...
```
---

The main script has a command line argument for the name of a shape from the examples.json file and produces an animation with the given shape as a starting point.


```bash
python3 game.py --shape pulsar
```
![Alt Text](https://media.giphy.com/media/XyDubPBkmOWrOElXPH/giphy.gif)