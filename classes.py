from NumPy_TutorialPoint import x


class siri():
    def __init__(self, x):
        self.x = x

    def __add__(self, o):
        return self.x + o.x


r = siri(10)
r1 = siri(20)
print(r + r1)
