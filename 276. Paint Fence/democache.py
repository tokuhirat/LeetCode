def demo_lru_cache(max_size):
    def decorating_function(user_function):
        return _lru_cache_wrapper(user_function, max_size)

    return decorating_function


def _lru_cache_wrapper(user_function, max_size):
    cache = {}

    # link filed name
    PREV = 0
    NEXT = 1
    KEY = 2
    RESULT = 3

    root = []
    root[:] = [root, root, None, None]
    full = False

    def wrapper(*args):
        nonlocal root, full
        key = args
        link = cache.get(key)
        if link is not None:
            prev_link, next_link, _, result = link
            prev_link[NEXT] = next_link
            next_link[PREV] = prev_link
            last = root[PREV]
            last[NEXT] = link
            link[PREV] = last
            link[NEXT] = root
            root[PREV] = link
            return result

        result = user_function(*args)
        if full:
            old_root = root
            old_root[KEY] = key
            old_root[RESULT] = result
            root = old_root[NEXT]
            old_result = root[RESULT]
            old_key = root[KEY]
            root[KEY] = None
            root[RESULT] = None
            del cache[old_key]
            cache[key] = old_root
            return result

        prev_link = root[PREV]
        link = [prev_link, root, key, result]
        prev_link[NEXT] = link
        root[PREV] = link
        cache[key] = link
        full = len(cache) >= max_size
        return result

    return wrapper


if __name__ == "__main__":
    import functools
    import time

    test_num = 40
    cache_size = 32

    def calc_time(f):
        start = time.perf_counter()
        print(f(test_num))
        end = time.perf_counter()
        print(end - start)
        print()

    def fib(n):
        if n == 1 or n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)

    print("without cache")
    calc_time(fib)

    @demo_lru_cache(cache_size)
    def fib_cache(n):
        if n == 1 or n == 2:
            return 1
        return fib_cache(n - 1) + fib_cache(n - 2)

    print("with democache")
    calc_time(fib_cache)

    @functools.lru_cache(cache_size)
    def fib_functool_cache(n):
        if n == 1 or n == 2:
            return 1
        return fib_functool_cache(n - 1) + fib_functool_cache(n - 2)

    print("with functools.lru_cache")
    calc_time(fib_functool_cache)

    # result
    # without cache
    # 102334155
    # 5.854699125047773
    #
    # with democache
    # 102334155
    # 4.25002072006464e-05
    #
    # with functools.lru_cache
    # 102334155
    # 1.0291812941432e-05
