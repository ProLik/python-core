# coding=utf8
# target 2.7.14


def test():
    "test function"

    print "hello world"

    print(abs(-1))

    print ("1111111")

    abs(1)

    print "%s is number %d! the amount is %f." % ("Python", 1, 0.44)

    import sys

    print >> sys.stderr, "has a error"

    logfile = open("error.txt", "a")

    print >> logfile, "catch a exception!"

    logfile.close()

    # name = raw_input("Enter login name:")

    # print "Your login is:", name

    # num = raw_input("Now enter a number:")

    # print "Doubling your number : %d" % (int(num) * 2)

    # 寻求未知方法的帮助
    # help(raw_input)


if __name__ == '__main__':
    test()
