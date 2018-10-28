import copy
import sys

solutions = []


def getSize():
	size = int(input("Enter size>>>"))
	if size <= 3:
		print("Too small")
		sys.exit()
	return size


def getBoard(size):
	board = [0] * size
	for i in range(size):
		board[i] = [0] * size
	return board


def printSolution(solutions, size):
	for sol in solutions:
		for row in sol:
			print(row)
		print()


def isSafe(board, row, col, size):
	# check row on left side
	for i in range(col):
		if board[row][i] == 1:
			return False

	# top left diagonal
	i, j = row, col
	while i >= 0 and j >= 0:
		if board[i][j] == 1:
			return False
		i -= 1
		j -= 1

	# bottom left diag
	i, j = row, col
	while i < size and j >= 0:
		if board[i][j] == 1:
			return False
		i += 1
		j -= 1
	return True

def addSolution(board):
	global solutions
	savedBoard = copy.deepcopy(board)
	solutions.append(savedBoard)

def solve(board, col, size):
	# basecase
	if col >= size:
		return
	for i in range(size):
		if isSafe(board, i, col, size):
			board[i][col] = 1
			if col == size-1:
				addSolution(board)
				board[i][col] = 0
				return
			solve(board, col+1, size)
			board[i][col] = 0 #backtrack

size = getSize()
board = getBoard(size)
solve(board,0, size)
printSolution(solutions,size)