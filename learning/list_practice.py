"""
列表 List

列表可更改排序，元素可以删除，有顺序
格式，打印方式
"""
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('\nI have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
# 注意看这里的写法，将list中的每一项都打出来
for item in shoplist:
    print(item, end=' ')

print('\n\nI also have to buy rice.')
shoplist.append('rice')
# 这是直接打印list的样子
print('My shopping list is now', shoplist)

print('\nI will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('\nThe first item I will buy is', shoplist[0])

print('I bought the', shoplist[0])
del shoplist[0]
print('My shopping list is now', shoplist)
