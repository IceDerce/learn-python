# 正确的写法
def func(a, b=5, c=10):
    """
    Keyword Arguments(关键字参数)

    一：不需要考虑参数的顺序 二：只对需要的参数赋值
    :param a: 需要定义
    :param b: 有默认参数
    :param c: 有默认参数
    :return: 打印出a,b,c的值
    """
    print('a is {} and b is {},and last c is {}'.format(a, b, c))


__version__ = 0.1


# 不推荐的写法
def func1(d, e=5, f=10):
    print('d is', d, 'and e is', e, ',and f is', f)

'''
func(3, 7)
func(25, c=25)
func(c=50, a=100)
'''