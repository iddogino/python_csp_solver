from csp import *

p = Problem()
p.add_variable(Variable("a", [1, 2]))
p.add_variable(Variable("b", [1, 2]))
p.add_variable(Variable("c", [1, 2]))
p.add_constraint(AllDifferentConstraint(["a", "b"]))
p.add_constraint(AllDifferentConstraint(["c", "b"]))

print(p.get_solutions())
