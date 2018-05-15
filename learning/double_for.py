# range 前闭区间，后开区间
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            print('%d is 合数' % num)
            break
    else:
        print("%d is 质数" % num)
