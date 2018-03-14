def f(z, **kwargs):
    for a in kwargs:
        print("%s=%s" % (a, kwargs[a]))
    # print(kwargs.pop('a'))
    # print(kwargs.pop('b'))
    print(z)


def h(z, *l, **kwargs):
    print(z)
    print(l)
    print(kwargs)


def main():
    dict = {'c':'cat',}
    # f(10, a='apple', b='ball', **dict)
    dict['x'] = "xray"
    # f(**dict)

    h(10, 20, 30, **dict)


if __name__ == '__main__':
    main()