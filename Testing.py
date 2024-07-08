from Nicknames import *

class BasicTest(Scene):
    def construct(self):
        A = x**2+3
        B = y**8-9
        C = (A/B)**(SmZ(1)/2)

        self.add(C)


class EvenMoreBasicTest(Scene):
    def construct(self):
        self.add(Tex("your mom"))