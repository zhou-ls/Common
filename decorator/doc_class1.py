# -*- coding: utf-8 -*-
def pi_fu(cls):
    class PiFuClass:
        def __init__(self, name, pi_fu_name):
            self.wrapped = cls(name, pi_fu_name)
            self.pi_fu_name = pi_fu_name

        def display(self):
            self.wrapped.display()
            print(f"展示皮肤{self.pi_fu_name}")

    return PiFuClass


@pi_fu
class YingXiong:
    def __init__(self, name, pi_fu_name):
        self.name = name
        self.pi_fu_name = pi_fu_name

    def display(self):
        print(f"展示英雄{self.name}")


ya_se = YingXiong("亚瑟", "死亡骑士")
ya_se.display()
