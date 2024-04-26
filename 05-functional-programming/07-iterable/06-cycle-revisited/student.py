def cycle(xs):
    xs_list = list(xs)
    while True:
        for x in xs_list:
            yield x
