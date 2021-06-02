# Sodoku Solver (CSP)
## _Using BackTracking, MRV, DH, and FC to solve any Sodoku puzzle_


Sodoku is a logic-based puzzle that consists of nine partially filled _3x3_ grids. There a few basic rules that make it a classic _constraint-satisfaction problem_.

- Each square must be filled with a digit (1-9)
- Each row must be filled with digits(1-9) with each digit only appearing once
- Each column must be filled with digits(1-9) with each digit only appearing once
- Each _3x3_ square must be filled with digits(1-9) with each digit only appearing once

## Algorithms

- **Backtracking (BT)**: A recursive depth-first search algorithm that assigns values to a variable that is chosen by a heuristic. The solution is incrementally built until a constraint is violated at which the algorithm "backtracks"
    --**Minimum Remaining Value (MRV)**: A heuristic that picks the varaiable that has the fewest legal values (most constrained). 
    --**Degree Heuristic (DH)**: A heuristic that chooses the variable that has constrains other variables the most. 
- **Forward Checking (FC)**: Eliminates value from neighbouring domains. If domain is empty, the algorithm can eliminate that value without having to backtrack.

    _Why use MRV + DH+ FC?_
    We can eliminate the values that will cause an incorrect solution earlier on so there are less branches at the top of the search tree to backtrack from. We use forward tracking to elimnate possible values before the backtracking algorithm gets to it allowing for less work to be done. Compared to simple backtracking, using MRV + FC can often times make the algorithm **1000x** faster [^1]

## Tech

- [Python 2.7] 

## Usage

The program will ask for a text document to be read. The text document should be formatted as shown below (nine rows of nine numbers with zeroes denoting the blank tiles)
```sh
000470030
004002000
009530060
500000400
000087900
090000600
006040000
850000000
070001200
```

After solving the puzzle the program will ask for the user to name the output file and print out to terminal the formatted results of the puzzle before and after it has been solved.

```sh
0 0 0 4 7 0 0 3 0    |   6 8 5 4 7 9 1 3 2 
0 0 4 0 0 2 0 0 0    |   7 3 4 1 6 2 5 9 8 
0 0 9 5 3 0 0 6 0    |   2 1 9 5 3 8 7 6 4 
5 0 0 0 0 0 4 0 0    |   5 6 8 9 1 3 4 2 7 
0 0 0 0 8 7 9 0 0    |   3 4 2 6 8 7 9 1 5 
0 9 0 0 0 0 6 0 0    |   1 9 7 2 5 4 6 8 3 
0 0 6 0 4 0 0 0 0    |   9 2 6 3 4 5 8 7 1 
8 5 0 0 0 0 0 0 0    |   8 5 1 7 2 6 3 4 9 
0 7 0 0 0 1 2 0 0    |   4 7 3 8 9 1 2 5 6 
```
## Results

| Puzzle      | Easy Time (seconds) | Medium Time (seconds) | Hard Time (seconds) | Expert Time (seconds) |
| :----------- | :-----------: | :-----------: | :-----------: | -----------: |
| 1   | 0.0521528720856 |  0.0914587974548 | 0.216630935669 | 0.503130197525 
| 2   | 0.0429151058197 |  0.107887983322  | 0.123332977295 | 0.801200151443
| 3   | 0.05295586586   |  0.0739970207214 | 0.225169897079 | 0.164076089859 
| 4   | 0.065633058548  |  0.0541348457336 | 0.121155977249 | 0.617947101593 
| 5   | 0.065633058548  |  0.115435123444  | 0.183528184891 | 0.250591993332
| Average   | 0.055857992172  |  0.088582754135  | 0.17396359444 | 0.4673891068


Puzzles generated from [sodoku.com]
[^1]: http://www.cs.toronto.edu/~hojjat/384w09/Lectures/Lecture-04-Backtracking-Search.pdf

[sodoku.com]: https://sudoku.com/expert/

[Python 2.7]: <https://www.python.org/download/releases/2.7/>
   