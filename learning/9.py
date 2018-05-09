for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            print('%d is a heshu' % num)
            break
    else:
        print("%d is a zhishu" % num)
