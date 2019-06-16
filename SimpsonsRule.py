# Simpson's Rule
import math

# Function representing Simpson's Rule to approximate a definite integral
# a -> lower bound of integral
# b -> upper bound of integral
# n -> the number of iterations to be performed
# f -> the function
def simpsons_rule_integration(a, b, n, f):

    delta_x = (b - a)/n
    result = f(a)
    i = 0
    n += 1
    for xi in range(n):
        xi = a + delta_x*i

        # Even so multiply by 2
        if i % 2 == 0 and i != 0 and i != n-1:
            answer = 2 * f(xi)
            result += answer
        # Otherwise, if we're not at the first or last iteration, multiply by 4(odds)
        elif i != 0 and i != n-1:
            answer = 4 * f(xi)
            result += answer
        # The last element has been reached
        elif i == n-1:
            result += f(b)
        i += 1
    result *= (delta_x*1/3)
    return result


print(simpsons_rule_integration(1, 20, 100, lambda f: math.sin(f)))
