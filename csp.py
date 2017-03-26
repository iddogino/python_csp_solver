"""
For var in variables:
    1. Reduce domain:
        1.1 For each option in domain, check if setting it will mean iminent death. If so, remove it
    2. For each option in domain, create a new branch with var = option, and move to the next variable
"""


class Variable(object):
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain


class Constraint(object):
    def __init__(self, variables):
        self.variables = variables

    def check(self, values):
        return True


class AllDifferentConstraint(Constraint):
    def check(self, values):
        if len(values) == 0:
            return True
        v = None
        for val in values:
            if v is None:
                v = val
            elif val == v:
                return False
        return True


class AllEqualConstraint(Constraint):
    def check(self, values):
        if len(values) == 0:
            return True
        v = values[0]
        for val in values:
            if v != val:
                return False
        return True


"""
def consistent(assignment, variables, constrains)
# This could be optimized by forward checking variables as well
"""

"""
    Constraint function:
    In: values
    Out: True / False
    Checks if values match constraint
"""


# Returns a sub set of d with only the items whose key is in the keys array
def filter_dictionary(d, keys):
    return {k: v for (k, v) in d.items() if k in keys}


def dictionary_to_array(d):
    return [v for (k, v) in d.items()]


def union(d1, d2):
    d = d1.copy()
    d.update(d2)
    return d


def union_arr(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))


class Problem(object):
    def __init__(self):
        self.variables = []
        self.constraints = []

    def add_variable(self, variable):
        self.variables.append(variable)

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def check_consistency(self, assignment):
        for constraint in self.constraints:
            relevantValues = filter_dictionary(assignment, constraint.variables)
            if not constraint.check(dictionary_to_array(relevantValues)):
                return False
        return True

    def find(self, assignment, _v):
        vars = _v.copy()  # because it is passed by reference, we need to create a local copy
        if len(vars) == 0:
            return [assignment]

        var = vars.pop()
        results = []
        for option in var.domain:
            new_assignment = union(assignment, {var.name: option})
            if self.check_consistency(new_assignment):
                res = self.find(new_assignment, vars)
                results += res
        return results

    def get_solutions(self):
        return self.find({}, self.variables.copy())
