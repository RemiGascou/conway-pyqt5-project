# Conway's Game of Life

This folder contains the files about the game _Conway's Game of Life_. It's a simple game created by the British mathematician John Horton Conway in 1970.
It's a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. The only interaction that the player have with the game is at the beginning with the creation of the initial grid.

## The game

It all start with a square or rectangular grid. It's divided into small parts, or cells, which can either be alive or dead.
At the beginning, the player can choose which cell are alive, the others being dead. Then every turn is played by the game itself with 4 simple rules.

### The rules

At each turn, the game applies 4 simple rules to each cell to determine its future state.

1. Any live cell with fewer than two live neighbors dies, as if by under population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## The files

So far, the only file that is in the folder is `Conway's game of life.py`. It implements the game, but without any graphical interface. This part is currently in developpement.

## References

See [Conway's Game of Life | Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) for more information on this game.

## Documentation of the file

### `Conway's game of life.py`

- `getNeighbours(grid, x, y)`
   - Function that, for a given grid and a given cell, identified with its coordinates `x` and `y`, return the coordinates and values of its neighbours
   - Parameters :
     - grid : a `n` x `m` array with the values of each cell, dead or alive
     - `x` : the coordinate of the cell on the x-axis
     -  `y` : the coordinate of the cell on the y-axis
   - Return :
     - neighbours : a dictionnary containing the coordinates and the values of the neighbours of the cell
   - Note : to access to the value of a given cell neighbour, use `neighbours[x][y]`, considering that `neighbours` is returned by the function and `x` and `y` are the coordinates of the cell of which we want to have access
- `countNeighbours(grid, x, y, valueOn, valueOff)`:
   - Function that, for a given grid and a given cell, identified with its coordinates `x` and `y`, return the number of cells in its neighbourhood that are on and the number that are off
   - Parameters :
     - grid : a `n` x `m` array with the values of each cell, dead or alive
     - `x` : the coordinate of the cell on the x-axis
     -  `y` : the coordinate of the cell on the y-axis
     - `valueOn` : the value that code the fact that a cell is on
     - `valueOff` : the value that code the fact that a cell is off
   - Return :
     - `numberOn`, `numberOff` : the number of cells that are on and off in the neighbourhood
- `applyRules(grid, valueOn, valueOff)`:
   - Function that, for a given grid, apply the rules of the game (see above for the detail)
   - Parameters :
     - grid : a `n` x `m` array with the values of each cell, dead or alive
     - `valueOn` : the value that code the fact that a cell is on
     - `valueOff` : the value that code the fact that a cell is off
   - Return :
     - `nextGrid` : the grid updated with the rules of the game (see above for the detail)
- `generateRandomGrid(xSize, ySize, valueOn, valueOff)`:
   - Function that generate randomly a grid
   - Parameters :
     - `xSize` : the size of the grid on the x-axis
     - `ySize` : the size of the grid on the x-axis
     - `valueOn` : the value that code the fact that a cell is on
     - `valueOff` : the value that code the fact that a cell is off
   - Return :
     - `grid` : the grid generated randomly
