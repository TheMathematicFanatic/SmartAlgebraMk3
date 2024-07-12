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


class SubexColorTest(Scene):
    def construct(self):
        c = SmVar('c')
        u = SmVar('u')
        v = SmVar('v')
        gamma = (1-v**2/c**2)**(-(SmZ(1)/2))
        Expr = f(3+gamma)/(12*gamma-14*x**2)+(2*z-y)**gamma
        self.add(Expr)
        Expr.set_color_by_subex({
            2:GREEN,
        })


class SubexTest(Scene):
    def construct(self):
        A = a+4
        self.add(A)
        debug_smarttex(self, A)


