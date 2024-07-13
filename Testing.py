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
        self.add(A.scale(3))
        A["1"].set_color(BLUE)


class ComprehensionTest(Scene):
    def construct(self):
        V = VGroup(Square() for i in range(5)).arrange(RIGHT)
        self.add(V)
        self.wait()


class Lissjous(Scene):
    def construct(self):
        lcurves=VGroup(*[
            ParametricFunction(
            lambda t:[np.cos(a*t),np.sin(b*t),0],
            t_range=(0,TAU,TAU/100))
            for a in range(1,10)
            for b in range(1,10)
            ])
        
        lcurves.arrange_in_grid(rows=9  , cols=9)
        lcurves.set_color([BLUE,YELLOW])
        lcurves.scale(0.7)
        self.add(lcurves)
        return
        self.play(Create(lcurves),run_time=6)
        self.wait()
        
        dots=VGroup(*[
            Dot(radius=0.025).move_to(curve.get_start()) for curve in lcurves])

        self.play(
            Create(lcurves,lag_ratio=0.01,run_time=3),
            FadeIn(dots,time_span=(2,3))
        )
        # self.play(*(
        #     MoveAlongPath(dot,curve)
        #     for dot,curve in zip(dots,lcurves)
        #     ),run_time=20,rate_func=linear)

#SubexTest().render()