# N-Queen_Problem

The N-Queens Problem is a classic puzzle where the goal is to place N chess queens on an N x N chessboard in such a way that no two queens threaten each other. This means that no two queens can be placed in the same row, column, or diagonal.

This problem has been studied in mathematics and computer science for many years and has been used as a benchmark for testing algorithms for solving constraint satisfaction problems.

Problem Statement: 
The N-Queens Problem can be stated as follows:

Given an N x N chessboard, place N queens on the board so that no two queens threaten each other.

In other words, no two queens can be placed in the same row, column, or diagonal of the board.

This repository contains a Python implementation of the N-Queens problem using a recursive backtracking algorithm. The code allows the user to input the value of N and outputs a valid solution if it exists.


Understanding the Code: 
The is_valid function checks if a queen can be placed at a given row and column on the board without being threatened by any other queens already on the board.

The solve_n_queens function is a recursive function that uses backtracking to solve the N-Queens problem. It takes three parameters: board, row, and n. board is a 2-dimensional list representing the chessboard, row is the current row being processed, and n is the number of queens to be placed on the board.

The print_board function prints the board in a readable format.

The main code prompts the user to input the value of N, initializes an empty board, and then calls the solve_n_queens function to solve the problem. If a valid solution exists, it outputs the solution. Otherwise, it outputs a message indicating that no solution exists for the given value of N.

Contributing: 
Contributions to this repository are welcome. If you find any issues or have any suggestions for improvement, please create a pull request.
