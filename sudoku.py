from csp import *

# Open file
game_file = open('games/sudoku/1.txt', 'r')
problem = Problem()

# Add variables
# This is bad code - assumes file is formatted properly. Never trust users - they are all idiots.
row = 1
for line in game_file:
    col = 1
    for elem in line.split(','):
        num = int(elem)
        var_name = row * 10 + col
        if num == 0:
            problem.add_variable(Variable(var_name, list(range(1, 10))))
        else:
            problem.add_variable(Variable(var_name, [num]))
        col += 1
    row += 1

# Add constrains
# rows different
for row in range(1, 10):
    problem.add_constraint(AllDifferentConstraint(range(row * 10 + 1, row * 10 + 10)))

# cols different
for col in range(1, 10):
    problem.add_constraint(AllDifferentConstraint(range(10 + col, 100 + col, 10)))

# squares different
problem.add_constraint(AllDifferentConstraint([11, 12, 13, 21, 22, 23, 31, 32, 33]))
problem.add_constraint(AllDifferentConstraint([14, 15, 16, 24, 25, 26, 34, 35, 36]))
problem.add_constraint(AllDifferentConstraint([17, 18, 19, 27, 28, 29, 37, 38, 39]))

problem.add_constraint(AllDifferentConstraint([41, 42, 43, 51, 52, 53, 61, 62, 63]))
problem.add_constraint(AllDifferentConstraint([44, 45, 46, 54, 55, 56, 64, 65, 66]))
problem.add_constraint(AllDifferentConstraint([47, 48, 49, 57, 58, 59, 67, 68, 69]))

problem.add_constraint(AllDifferentConstraint([71, 72, 73, 81, 82, 83, 91, 92, 93]))
problem.add_constraint(AllDifferentConstraint([74, 75, 76, 84, 85, 86, 94, 95, 96]))
problem.add_constraint(AllDifferentConstraint([77, 78, 79, 87, 88, 89, 97, 98, 99]))

solutions = problem.get_solutions()

for solution in solutions:
    for row in range(1, 10):
        for col in range(1, 10):
            index = row * 10 + col
            print(solution[index], end='')
            if col % 3 == 0:
                print('|', end='')
        print()
        if row % 3 == 0:
            print('---+---+---')
