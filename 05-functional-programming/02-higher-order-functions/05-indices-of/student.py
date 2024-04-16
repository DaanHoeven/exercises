def is_odd(x):
    return x % 2 != 0


def indices_of(xs, condition):
    return [x for x in range(len(xs)) if condition(xs[x])]


print(indices_of([0, 1, 2, 3, 4, 5], is_odd))
