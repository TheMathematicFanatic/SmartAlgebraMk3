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
            v:RED
        })


class SubexTest(Scene):
    def construct(self):
        A = a+4
        self.add(A.scale(3))
        A["1"].set_color(BLUE)


class SimpleSubexColorTest(Scene):
    def construct(self):
        C = SmZ(2)/2

        self.add(C)

        print(C.get_addresses_of_subex(2))


class SubexColorDemo(Scene):
    def construct(self):
        A = x-4
        B = 3*x-6
        C = x*y - (2*x**3 - y**x)

        D = (A*B**(y-2))/C

        self.add(D)
        D.set_color_by_subex({x:RED,y:BLUE,2:GREEN})