import time


def tic_toc(function, *args, **kwargs):
    tic = time.perf_counter()
    print(function(*args, **kwargs))

    toc = time.perf_counter()

    return toc - tic
