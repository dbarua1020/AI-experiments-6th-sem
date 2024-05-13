def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def unify(x, y, theta):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x[0].islower():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y[0].islower():
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def substitute(theta, expression):
    if theta is None:
        return None
    elif isinstance(expression, str):
        return theta.get(expression, expression)
    elif isinstance(expression, list):
        return [substitute(theta, exp) for exp in expression]
    else:
        return expression

if __name__ == "__main__":
    equation1 = ["+", "x", 2]
    equation2 = ["+", 3, "y"]
    theta = unify(equation1, equation2, {})
    print("Unifier:", theta)

    if theta:
        solved_equation1 = substitute(theta, equation1)
        print("Solved Equation 1:", solved_equation1)

        solved_equation2 = substitute(theta, equation2)
        print("Solved Equation 2:", solved_equation2)
