from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from datetime import datetime, date, time
from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.popup import Popup
x1 = 0



class ScrButton(Button):
    def __init__(self, screen,direction ='right', goal='main', text='', **kwargs):
        super().__init__(text=text,**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal








class MainScr(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name=name)
        btn= Button(text="Переключиться на другой экран")
        h1 = BoxLayout()
        label = Label(text= 'Выберите экран')
        h1.add_widget(label)
        v1 = BoxLayout(orientation = 'vertical', padding = 8,spacing = 8)
        btn1 = ScrButton(self,'right','second', text='1')
        btn2 = ScrButton(self,'right','three', text='2')
        btn3 = ScrButton(self,'right','fourth', text='3')
        v1.add_widget(btn1)
        v1.add_widget(btn2)
        v1.add_widget(btn3)
        
        h1.add_widget(v1)
        self.add_widget(h1)


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = ScrButton(self,'left','main',text="Возвращение!")
        v2 = BoxLayout(orientation = 'vertical', padding = 10,spacing = 20)
        #btn_ok = Button(text= 'Начать',size_hint = [None, None], size = [300,100],background_color= (1.0,0.0, 0.0, 1.0),pos_hint={'center_x':0.5})
        btn_ok = ScrButton(self,'left','five',text='Далее',size_hint = [None, None], size = [300,100],background_color= (1.0,0.0, 0.0, 1.0),pos_hint={'center_x':0.5})
        
        h2 = BoxLayout(orientation = 'horizontal', padding = 20,spacing = 80)
        h3 = BoxLayout(orientation = 'horizontal', padding = 20,spacing = 80)
        self.text2=Label(text='Данное приложение позволит вам с помощью теста Руфье' , font_size=9)
        self.text3=Label(text='провести первичную диагностику вашего здоровья',font_size=9)          
        self.text3=Label(text= 'Проба Руфье представляет собой нагрузочный комплекс',font_size=9)          
        self.text4=Label(text='предназначенный для оценки работоспособности сердца при физической нагрузке',font_size=9)
        self.text5=Label(text='затем в течение 45 секунд испытуемый выполняет 30 приседаний.',font_size=9)
        self.text6=Label(text='После окончания нагрузки испытуемый ложится',font_size=9)
        self.text7=Label(text='и у него вновь подсчитывается число пульсаций за первые 15 секунд',font_size=9)
        self.text=Label(text='введите имя ,и возвраст колонки не решают',font_size=9)
        self.btn_input = TextInput(size_hint = [None, None], size = [230,40],pos_hint={'center_x':1 ,'center_y':1.79})
        self.btn1_input = TextInput(size_hint = [None, None], size = [230,40],pos_hint={'center_x':12 ,'center_y':1.79})
        v2.add_widget(self.text2)
        v2.add_widget(self.text3)
        v2.add_widget(self.text4)
        v2.add_widget(self.text5)
        v2.add_widget(self.text6)
        v2.add_widget(self.text7)
        h2.add_widget(self.text)
        
        
        h2.add_widget(self.btn_input)
        
        
        h3.add_widget(self.btn1_input)
        
        
        
        v2.add_widget(h2)
        v2.add_widget(h3)
        v2.add_widget(btn_ok)
        
        
        self.add_widget(v2)    
       

        
       




class ThreeScr(Screen):
    def __init__(self, name='three'):
        super().__init__(name=name)
        btn = ScrButton(self,'left','main', text="Вернись, вернись!")
        self.add_widget(btn)       


class FourthScr(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        btn = ScrButton(self,'left','main', text="Вернись, вернись!")  
        self.add_widget(btn)       

class FiveScr(Screen):
    def __init__(self, name='five'):
        super().__init__(name=name)
        v4 = BoxLayout(orientation = 'vertical', padding = 10,spacing = 20)   
        btn_off = ScrButton(self,'left','six',text='Далее',size_hint = [None, None], size = [300,100],background_color= (1.214,4.0, 1.0, 1.0),pos_hint={'center_x':0.5})
        self.text15=Label(text='Замерьте пульс на 15 секунд' , font_size=15)
        self.text10=Label(text='Напишите результат в следующей страничке' , font_size=15)
        self.btn6_input = TextInput(size_hint = [None, None], size = [390,40],pos_hint={'center_x':0.5 ,'center_y':1.79})
        self.texttimer=Label(text='0' , font_size=15)
        Clock.schedule_interval(self.changetimer, 1)
        v4.add_widget(self.text15)
        v4.add_widget(self.text10)
        v4.add_widget(self.btn6_input)
        v4.add_widget(self.texttimer)
        v4.add_widget(btn_off)
        self.add_widget(v4)    

    def changetimer(self,a):
        self.texttimer.text=str(int(self.texttimer.text.split(' ')[0])+1)+" сек"
    

class SixScr(Screen):
    def __init__(self, name='six'):
        super().__init__(name=name)
        v5 = BoxLayout(orientation = 'vertical', padding = 10,spacing = 20)
        btn_rep = ScrButton(self,'left','seven',text="продолжить",size_hint = [None, None], size = [300,100],background_color= (1.154,4.0, 10.0, 5.0),pos_hint={'center_x':0.5})
        self.text21=Label(text='Сделайте 35 приседаний, если тяжело можно 20' , font_size=15)
        v5.add_widget(self.text21)
        v5.add_widget(btn_rep)
        self.add_widget(v5)

class SevenScr(Screen):
    def __init__(self, name='seven'):
        super().__init__(name=name)
        v6 = BoxLayout(orientation = 'vertical', padding = 10,spacing = 20)
        #btn_ok = Button(text= 'Начать',size_hint = [None, None], size = [300,100],background_color= (1.0,0.0, 0.0, 1.0),pos_hint={'center_x':0.5})
        btn_ok = ScrButton(self,'left','nine',text='Далее',size_hint = [None, None], size = [300,100],background_color= (1.0,0.0, 0.0, 1.0),pos_hint={'center_x':0.5})
        h7 = BoxLayout(orientation = 'horizontal', padding = 20,spacing = 50)
       
        self.text2=Label(text='В течение минуты замерьте пульс два раза:' , font_size=12)
        self.text3=Label(text='за первые 15 секунд минуты, затем за последние 15 секунд',font_size=12)          
        self.text5=Label(text= 'Результаты запишите в соответствующие поля',font_size=12)          
        self.text=Label(text='1 колонка:результат: , 2 колонка: Результат после отдыха:',font_size=9)
        self.btn_input = TextInput(size_hint = [None, None], size = [240,40],pos_hint={'center_x':14 ,'center_y':1})
        self.btn_input.check = self.set_x1
        self.btn1_input = TextInput(size_hint = [None, None], size = [240,40],pos_hint={'center_x':0.73 ,'center_y':1.29})
        v6.add_widget(self.text2)
        v6.add_widget(self.text3)
        v6.add_widget(self.text)
        v6.add_widget(self.text5)
        
        
        
        
        h7.add_widget(self.btn_input)
        
        
        
        v6.add_widget(self.btn1_input)
        
        
        
        v6.add_widget(h7)
       
        v6.add_widget(btn_ok)
        
        
        self.add_widget(v6)  

    def set_x1(self):
        global x1
        x1 = self.btn1_input.text

class NineScr(Screen):
    def __init__(self, name='nine'):
        super().__init__(name=name)
        vs = BoxLayout(orientation = 'vertical', padding = 10,spacing = 20) 
        btn = ScrButton(self,'left','main', text="Программа недоделана, сорян!")  
        self.add_widget(btn)
        



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThreeScr())
        sm.add_widget(FourthScr())
        sm.add_widget(FiveScr())
        sm.add_widget(SixScr())
        sm.add_widget(SevenScr())
        sm.add_widget(NineScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm

app = MyApp()
app.run()