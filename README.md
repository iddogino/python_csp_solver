#Constraint Satisfaction Problems Solve

This solves CSPs in python. This is currently a very simple and straightforward backtracking implementation with no forward checking / smart ordering.

See examples:

- Australia - map coloring problem
- Basic - simple usage
- Sudoku - solves a Sudoku puzzle

##Basic Usage

To create a new problem:

    from csp import *

    p = Problem()

Add variables - for each variable, give a list with it's domain (all possibilities for it's value):

    p.add_variable(Variable("a", [1, 2]))
    p.add_variable(Variable("b", [1, 2]))
    p.add_variable(Variable("c", [1, 2]))

Add constrains (read more bellow):

    p.add_constraint(AllDifferentConstraint(["a", "b"]))
    p.add_constraint(AllDifferentConstraint(["c", "b"]))

Get solutions:

    p.get_solutions()

This will return an array. It'll be empty if there is no assignment satisfying the constrains, or contain hashes of solutions.

##Constrains

Each constrain class extends the basic **Constraint** class. It provides a **check()** method which gets a list of values as input and returns True (satisfies constraint) or False.

Built in examples:

- CheckAllDifferent
- CheckAllEqual