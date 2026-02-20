def accum():
    v = 0
    try:
        while True:
            v += yield
    except GeneratorExit:
        return v
