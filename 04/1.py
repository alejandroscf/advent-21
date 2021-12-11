#!/usr/bin/python3

import sys

boards = []
boards_t = []
board_idx = -1
line_idx = 0

numbers = []

for line in sys.stdin:
    if len(numbers) == 0:
        numbers = line.strip().split(",")
    elif line.strip() == "":
        board_idx += 1
        line_idx = 0
        boards.append([])
        boards_t.append([])
    else:
        num_line = line.split()
        num_line_t = [ numbers.index(x) for x in num_line ]
        boards[board_idx].append(num_line)
        boards_t[board_idx].append(num_line_t)

#print(boards)
#print(boards_t)

board_idx = 0
board_min_max = [len(numbers)]*len(boards)
for board in boards_t:
    for line in board:
        max_line = max(line)
        if max_line < board_min_max[board_idx]:
            board_min_max[board_idx] = max_line
    # TODO colums
    for column_i in range(len(board[0])):
        max_line = max([ line[column_i] for line in board ])
        if max_line < board_min_max[board_idx]:
            board_min_max[board_idx] = max_line
    board_idx += 1
win_round = min(board_min_max)
winner = board_min_max.index(win_round)
#print(win_round)
#print(winner)

score = 0

line_idx = 0
for line in boards_t[winner]:
    score += sum([ int(boards[winner][line_idx][idx]) for idx, x in enumerate(line) if x > win_round])
    line_idx += 1
print(score*int(numbers[win_round]))
