from csp import *

problem = Problem()

colors = ["blue","green","red"]
states = ["WA","NT","Q","NSW","V","SA","T"]

for state in states:
    problem.add_variable(Variable(state, colors))

problem.add_constraint(AllDifferentConstraint(["WA", "NT"]))
problem.add_constraint(AllDifferentConstraint(["WA", "SA"]))
problem.add_constraint(AllDifferentConstraint(["NT", "SA"]))
problem.add_constraint(AllDifferentConstraint(["NT", "Q"]))
problem.add_constraint(AllDifferentConstraint(["SA", "Q"]))
problem.add_constraint(AllDifferentConstraint(["SA", "NSW"]))
problem.add_constraint(AllDifferentConstraint(["SA", "V"]))
problem.add_constraint(AllDifferentConstraint(["Q", "NSW"]))
problem.add_constraint(AllDifferentConstraint(["V", "NSW"]))

print(problem.get_solutions()[0])
