from manim import *
class mapping(Scene):
    def construct(self):
        t1 = Text('Balance', font = 'Monospace', font_size= 30)
        
        
        self.play(Write(t1))
        self.play(
            t1.animate.shift(LEFT*6)
        )
        
        a1 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).rotate(35* DEGREES).scale(1.5)
        a2 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).rotate(-35* DEGREES).scale(1.5).next_to(a1,DOWN)
        ag1 = VGroup(a1, a2).next_to(t1)
        
        self.play(
            Write(ag1), run_time=0.5
        )
        
        
        r1 = Rectangle(height=1, width=2).move_to(a1.get_end()).shift(RIGHT*1.03)
        kt = Text('0xheasy', font= 'Monospace', font_size=22).move_to(r1.get_center())
        r2 = Rectangle(height=1, width=2).move_to(a2.get_end()).shift(RIGHT*1.03)
        kt1 = Text('0xgiving', font= 'Monospace', font_size=22).move_to(r2.get_center())
        t2 = Text('Key 1', font = 'Monospace', font_size= 28).next_to(r1, UP)
        
        # all1 = VGroup(r1, kt,r2, kt1,t2)
    
       
        self.play(
            
            GrowFromCenter(r1),
            GrowFromCenter(kt),
            GrowFromCenter(r2),
            GrowFromCenter(kt1), run_time=0.5
            
        )
        
        self.play(
            GrowFromCenter(t2), run_time=0.5
        )
        
        
        a3 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).rotate(20* DEGREES).scale(1)
        a4 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).rotate(-15* DEGREES).scale(1).next_to(a3,DOWN)
        ag2 = VGroup(a3, a4).next_to(r1).shift(LEFT*0.2)
        
        self.play(
            Write(ag2), run_time=0.5
        )
        
       
        r3 = Rectangle(height=0.7, width=1.5).move_to(a3.get_end()).shift(RIGHT*0.78)
        kt2 = Text('USDT', font= 'Monospace', font_size=22).move_to(r3.get_center())
        r4 = Rectangle(height=0.7, width=1.5).move_to(a4.get_end()).shift(RIGHT*0.78)
        kt3 = Text('WETH', font= 'Monospace', font_size=22).move_to(r4.get_center())
        
        t3= Text('Key 2', font = 'Monospace', font_size= 28).next_to(r3, UP)
        
       
        self.play(
            
            GrowFromCenter(r3),
            GrowFromCenter(kt2),
            GrowFromCenter(r4),
            GrowFromCenter(kt3), run_time=0.5
            
        )
        self.play(
            GrowFromCenter(t3), run_time=0.5
        )
        
        
        a5 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).scale(0.8).next_to(r3).shift(LEFT*0.23)
        a6 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).scale(0.8).next_to(r4).shift(LEFT*0.23)
        ag3 = VGroup(a5, a6)
        
        self.play(
            Write(ag3), run_time=0.5
        )
        
        
        
        r5 = Rectangle(height=0.7, width=1.5).move_to(a5.get_end()).shift(RIGHT*0.78)
        kt4 = Text('50', font= 'Monospace', font_size=22).move_to(r5.get_center())
        r6 = Rectangle(height=0.7, width=1.5).move_to(a6.get_end()).shift(RIGHT*0.78)
        kt5 = Text('5', font= 'Monospace', font_size=22).move_to(r6.get_center())
        
        t4= Text('Value', font = 'Monospace', font_size= 28).next_to(r5, UP)
        
       
        self.play(
            
            GrowFromCenter(r5),
            GrowFromCenter(kt4),
            GrowFromCenter(r6),
            GrowFromCenter(kt5), run_time=0.5
            
        )
        
        self.play(
            GrowFromCenter(t4), run_time=0.5
        )
        
        
        a7 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).rotate(30* DEGREES).scale(1.15)
        a8 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).scale(1.05).next_to(a7,DOWN*0.1).shift(RIGHT*0.1).shift(LEFT*0.1)
        a9 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).rotate(-30* DEGREES).scale(1.15).next_to(a7,DOWN)
        ag4 = VGroup(a7, a8, a9).next_to(r2).shift(LEFT*0.25)
        
        self.play(
            Write(ag4), run_time=0.5
        )
        
        r7 = Rectangle(height=0.7, width=1.5).move_to(a7.get_end()).shift(RIGHT*0.8)
        kt6 = Text('OP', font= 'Monospace', font_size=22).move_to(r7.get_center())
        r8 = Rectangle(height=0.7, width=1.5).move_to(a8.get_end()).shift(RIGHT*0.78)
        kt7 = Text('USDC', font= 'Monospace', font_size=22).move_to(r8.get_center())
        r9 = Rectangle(height=0.7, width=1.5).move_to(a9.get_end()).shift(RIGHT*0.8)
        kt8 = Text('RRT', font= 'Monospace', font_size=22).move_to(r9.get_center())
        
        
        self.play(
            GrowFromCenter(r7),
            GrowFromCenter(kt6),  
            GrowFromCenter(r8),
            GrowFromCenter(kt7),
            GrowFromCenter(r9),
            GrowFromCenter(kt8), run_time=0.5
            
        )
        
        
        a10 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).scale(0.75).next_to(r7).shift(LEFT*0.23)
        a11 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).scale(0.75).next_to(r8).shift(LEFT*0.23)
        a12 = Arrow(max_stroke_width_to_length_ratio=0.7, max_tip_length_to_length_ratio=0.12).scale(0.75).next_to(r9).shift(LEFT*0.23)
        
        ag5 = VGroup(a10, a11, a12)
        
        self.play(
            Write(ag5), run_time=0.5
        )
        
        r10 = Rectangle(height=0.7, width=1.5).move_to(a10.get_end()).shift(RIGHT*0.78)
        kt9 = Text('1000', font= 'Monospace', font_size=22).move_to(r10.get_center())
        r11 = Rectangle(height=0.7, width=1.5).move_to(a11.get_end()).shift(RIGHT*0.78)
        kt10 = Text('70', font= 'Monospace', font_size=22).move_to(r11.get_center())
        r12 = Rectangle(height=0.7, width=1.5).move_to(a12.get_end()).shift(RIGHT*0.78)
        kt11 = Text('10', font= 'Monospace', font_size=22).move_to(r12.get_center())
        
        
        self.play(
            GrowFromCenter(r10),
            GrowFromCenter(kt9),
            GrowFromCenter(r11),
            GrowFromCenter(kt10),
            GrowFromCenter(r12),
            GrowFromCenter(kt11), run_time=0.5
            
        )
        
        
        self.wait(2)
            
        