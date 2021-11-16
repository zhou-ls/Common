class Bases:

    def __init__(self, obj=None):
        self.obj = obj

    def screen(self, number):
        pass


class A(Bases):

    def screen(self, number):

        if number >= 200:
            print("{} 划入A集合".format(number))
        else:
            self.obj.screen(number)


class B(Bases):

    def screen(self, number):

        if 200 > number > 100:
            print("{} 划入B集合".format(number))
        else:
            self.obj.screen(number)


class C(Bases):

    def screen(self, number):
        if number <= 100:
            print("{} 划入C集合".format(number))


if __name__ == '__main__':
    """
    一个对象中含有另一个对象的引用以此类推形成链条
    每个对象中应该有明确的责任划分即处理请求的条件
    链条的最后一节应该设计成通用请求处理，以免出现漏洞
    请求应该传入链条的头部
    """
    test = [10, 100, 150, 200, 300]
    c = C()
    b = B(c)
    a = A(b)
    for i in test:
        a.screen(i)
