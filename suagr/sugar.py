__doc__ = """        
        语法糖（Syntactic sugar）：
            计算机语言中特殊的某种语法
            这种语法对语言的功能并没有影响
            对于程序员有更好的易用性
            能够增加程序的可读性
        """

__all__ = ['example_three_operator', 'example_base', 'example_with', 'example_for_else',
           'example_try_else', 'example_lambda', 'example_dynamic_args', 'example_express',
           'example_generator', 'example_closure', 'example_decorator']


def example_three_operator():
    """
        三目运算符
    """
    b = 2
    c = 3

    a = max(b, c)
    a = c > b and c or b
    a = c if c > b else b
    a = [b, c][c > b]

    return a


def example_base():
    """
        常规操作
    """
    a = 1; b = 23; c = 3
    b, c = c, b
    a < c < b < 5
    '1' * 100
    [1,2,3,4] + [5,6,7,8]

    l = [1, 2, 3, 4, 5]
    l[2]
    l[:3]
    l[3:]
    l[2:4]
    l[:-1]
    l[:]
    l[::2]


def example_with():
    """
        with 语法
    """

    with open('example_2.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


def example_for_else():
    """
        for else
    """
    for i in range(0):
        print(i)
        break
    else:
        print('for end')


def example_while_else():
    """
        while else
    :return:
    """
    i = 1
    while i:
        print(i)
        i -= 1
        break
    else:
        print('while end')


def example_try_else():
    """
        try else
    """
    try:
        1 / 1
    except Exception as e:
        print('except occured')
    else:
        print('it is fine')
    finally:
        print('i am finally')


def example_lambda(in_dict):
    """
        lambda 表达式， 匿名函数表达式
    """

    print('in_dict:', in_dict)
    out_dict = sorted(in_dict.items(), key=lambda x: x[1])
    print('out_dict', out_dict)


def example_dynamic_args(*args, **kwargs):
    """
        动态参数
    """
    print(args)
    print(kwargs)


def example_express(in_list):
    """
        推导式
    """

    print('array before:', in_list)
    array = [i for i in in_list if i % 2 != 0] # 列表推导表达式
    print('array after:', array)

    print('array before:', in_list)
    array = (i for i in in_list if i % 2 != 0) # 生成器推导表达式
    print('array after:', array)

    print('array before:', in_list)
    array = {i for i in in_list if i % 2 != 0} # 集合推导表达式
    print('array after:', array)

    print('array before:', in_list)
    array = {i: i * 2 for i in in_list if i % 2 != 0}  # 字典推导表达式
    print('array after:', array)


def example_generator(in_list):
    """
        生成器
    """
    for i in in_list:
        yield i * 2


def example_decorator(func):
    '''装饰器'''
    def inner():
        func()

    return inner


def example_closure(a):
    """
        闭包
    """
    # a = 2

    def inner_func(b):
        return b * a

    return inner_func


def example_decorator(func):
    """
        装饰器
    """
    def inner_func():
        # TODO something
        func()
        # TODO something else

    return inner_func


'''
    zip, filter, map, reduce, eval, super
'''


if '__main__' == __name__:
    in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
    in_dict = {'a': 10, 'b': 2, 'c': 3}
    example_express(in_list)
    # example_lambda(in_dict)
    # example_dynamic_args(*in_list, **in_dict)
