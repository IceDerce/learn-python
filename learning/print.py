#  print  结束默认是有转行的，如果不需要转行，自己加end
print('a', end=' ')
print('b', end=' ')
print('c')

#  转义符号\
print('What\' yours\' fucking name?')
#  同样也可以这么写
print("What's your' fucking name?")
#  用原始字符串的写法R（Raw）
print(r"What's your' fucking name?")


#     正确的转行方式
print('This is the first line.\nThis is the second line.')
#  这是反面教材
print('This is the first line.'
      'This is the second line.')
#  末尾的\只有不自动换新输入的作用，他的作用同 不转行
print('This is the first line.\
This is the second line.')





