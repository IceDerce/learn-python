def total(a=5, *numbers, **phonebook):
    """
    它是如何工作的。

    当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数
    （Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。

    类似地，当我们声明一个诸如 **phonebook 的双星号参数时，从此处开始直至结束的所有关键字
    参数都将被收集并汇集成一个名为 phonebook 的字典（Dictionary）。
    """
    print('a', a)
# 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

# 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
print(total.__doc__)

__version__ = 0.1