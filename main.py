from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
import random
import easygui
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import pyautogui
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os
import requests

from kivy.uix.togglebutton import ToggleButton
from tkinter import messagebox
from tkinter import Tk
root1 = Tk()
root1.withdraw()
user_screen_width, user_screen_height= pyautogui.size()
program_width = user_screen_width/2
program_height = user_screen_height/1.4
Window.size = (program_width, program_height)

def __init__():    
    if "assets" in os.listdir():
        for file in os.listdir("assets"):
            print (file)
            os.remove("assets/" + file)
        os.rmdir("assets")
    if not "assets" in os.listdir():
        os.mkdir("assets")
    if not "config.txt" in os.listdir("assets"):
        config = open("assets\\config.txt", "w")
        config.write
        config.close

config = {'target_folder':'', 'image_amount':'', 'search_terms':''}

from kivy.uix.label import Label
import webbrowser

"""A kivy widget that implements a hyperlink"""
import webbrowser


def error_prompt(message):
    prompt = messagebox.showinfo(title = "Error",message = message)
    return prompt
    
Builder.load_string("""
<folder_selectScreen>:
    BoxLayout:
        orientation: 'vertical'
        size: root.size
        Label:
            text : 'Choose Where You Would Like To Download Images To'
        Button:
            id: button1
            text: 'Select Folder'
            on_release: root.update_selected()
        Label:
            id: label1
            text: 'You Have Selected: ' + root.selected
        Button:
            id: continue1
            text: 'Continue'
            on_release: root.continue_or_not()
    FloatLayout:
        Button:
            background_normal: ''
            background_color: 0, 0, 0, 0
            text: 'All Images Downloaded Are Sourced From [color=0645AD]https://www.pexels.com/[u][/color]'
            markup: True 
            size_hint: 1,.05
            pos_hint: {'x':0, 'y':0}
            on_press: root.web()
            
<image_amountScreen>:
    BoxLayout:
        spacing: 1
        orientation: 'vertical'
        size: root.size
        Label:
            text : 'How many Images Would You Like to Download'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '-1000'
                on_press:
                    root.update_image_amount_m('1000')
            Button:
                text: '-100'
                on_press:
                    root.update_image_amount_m('100')
            Button:
                text: '-10'
                on_press:
                    root.update_image_amount_m('10')
            Label:
                id: input
                text: str(root.input)
            Button:
                text: '+10'
                on_press:
                    root.update_image_amount_p('10')
            Button:
                text: '+100'
                on_press:
                    root.update_image_amount_p('100')
            Button:
                text: '+1000'
                on_press:
                    root.update_image_amount_p('1000')
        Button:
            text: 'Reset'
            on_press: root.reset()
        BoxLayout:

            orientation: 'horizontal'
            Button:
                id : previous1
                text : 'Previous'
                on_release:
                    root.manager.transition.direction = 'right'
                    root.manager.current = "folder_select"
            Button:
                id: continue2
                text: 'Continue'
                on_release:
                    root.continue_or_not()
    FloatLayout:
        Button:
            background_normal: ''
            background_color: 0, 0, 0, 0
            text: 'All Images Downloaded Are Sourced From [color=0645AD]https://www.pexels.com/[u][/color]'
            markup: True 
            size_hint: 1,.05
            pos_hint: {'x':0, 'y':0}
            on_press: root.web()

<Search_termsScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text : 'Select Search Terms:'
        GridLayout:
            id: grid
            cols : 6
            rows: 6
            ToggleButton:
                id : Lake
                text: 'Lake'
                on_state: root.select('Lake')
            ToggleButton:
                id : River
                text: 'River'
                on_state: root.select('River')
            ToggleButton:
                id : Sunset
                text: 'Sunset'
                on_state: root.select('Sunset')
            ToggleButton:
                id : Sky
                text: 'Sky'
                on_state: root.select('Sky')
            ToggleButton:
                id : Ocean
                text: 'Ocean'
                on_state: root.select('Ocean')
            ToggleButton:
                id : Moon
                text: 'Moon'
                on_state: root.select('Moon')
            ToggleButton:
                id : Urban
                text: 'Urban'
                on_state: root.select('Urban')
            ToggleButton:
                id : Cityscape
                text: 'Cityscape'
                on_state: root.select('Cityscape')
            ToggleButton:
                id : Cloudscape
                text: 'Cloudscape'
                on_state: root.select('Cloudscape')
        BoxLayout:
            orientation: 'horizontal'
            TextInput:
                id:textinput
                hint_text : 'Enter Custom Search'
            Button:
                text : 'Add'
                on_press: root.get_text(root.added_search_terms)
            Button:
                text : 'Remove All'
                on_press: root.remove_all()
        Label:
            id: search_terms_for_label
            text : 'You Have Selected: ' + root.search_terms_for_label
        BoxLayout:
            orientation: 'horizontal'
            Button:
                id : previous1
                text : 'Previous'
                on_release:
                    root.manager.transition.direction = 'right'
                    root.manager.current = "image_amount"
            Button:
                id: continue2
                text: 'Continue'
                on_release:
                    root.continue_or_not()
    FloatLayout:
        Button:
            background_normal: ''
            background_color: 0, 0, 0, 0
            text: 'All Images Downloaded Are Sourced From [color=0645AD]https://www.pexels.com/[u][/color]'
            markup: True 
            size_hint: 1,.05
            pos_hint: {'x':0, 'y':0}
            on_press: root.web()
<script_runScreen>:
    BoxLayout:
        Label: 
            text : str(root.config)
    FloatLayout:
        Button:
            background_normal: ''
            background_color: 0, 0, 0, 0
            text: 'All Images Downloaded Are Sourced From [color=0645AD]https://www.pexels.com/[u][/color]'
            markup: True 
            size_hint: 1,.05
            pos_hint: {'x':0, 'y':0}
            on_press: root.web()
""")

class folder_selectScreen(Screen):
    selected= StringProperty()
    def __init__(self, **kwargs):
        super(folder_selectScreen, self).__init__(**kwargs)
        self.selected = "Nothing"
    def update_selected(self):
        global continue_allowed
        selected = easygui.diropenbox()
        selected_after_check = None
        if selected == None:
            selected_after_check = self.selected
            continue_allowed = False
        if not selected == None:
            selected_after_check = selected
            continue_allowed = True
        self.selected = selected_after_check
    def continue_or_not(self):
        global config
        try:
            if not continue_allowed == None:
                if continue_allowed == True:
                    self.manager.transition.direction = 'left'
                    self.manager.current = "image_amount"
                    config.__setitem__("target_folder",str(self.selected))
                    print(config)
                        
        except NameError:
            error_prompt("No Folder Selected")
    def web(self):
        webbrowser.open('https://www.pexels.com')



class image_amountScreen(Screen):
    input = NumericProperty()
    def __init__(self, **kwargs):
        super(image_amountScreen, self).__init__(**kwargs)
        self.input = 10
    def update_image_amount_p(self,amount):
        self.input = int(self.input) + int(amount)
    def update_image_amount_m(self,amount):
        if not self.input == 0:
            if not int(self.input) - int(amount) < 10:
                self.input = int(self.input) - int(amount)
            else:
                self.input = 10
    def reset(self):
        self.input = 1
    def continue_or_not(self):
        continue_allowed = False
        if 10 <= self.input <=1000000:
            continue_allowed = True
        else:
            error_prompt("Selected Amount out of range 10-100000")
        if continue_allowed == True:
            global config
            self.manager.transition.direction = 'left'
            self.manager.current = "search_terms"
            config.__setitem__("image_amount", str(self.input))
            print(config)
    def web(self):
        webbrowser.open('https://www.pexels.com')

search_terms = []
class search_termsScreen(Screen):
    search_terms_for_label = StringProperty()
    def __init__(self, **kwargs):
        super(search_termsScreen, self).__init__(**kwargs)
    def select(self,term):
        global config
        global search_terms
        if not term in search_terms:
            search_terms.append(term)
        else:
            search_terms.remove(term)
        seperater = ", "
        self.search_terms_for_label = seperater.join(search_terms)
    def pressed(self,term):
        if not term.text in search_terms:
            search_terms.append(term.text)
        else:
            search_terms.remove(term.text)
        seperater = ", "
        self.search_terms_for_label = seperater.join(search_terms)
    added_search_terms = []
    
    def get_text(self,added_search_terms):
        if not self.ids.textinput.text == "":
            if not self.ids.textinput.text in added_search_terms:
                button_name = self.ids.textinput.text
                new_button = ToggleButton(text=button_name)
                new_button.bind(on_press = self.pressed)
                try:
                    self.ids.grid.add_widget(new_button)
                    added_search_terms.append(self.ids.textinput.text)
                    self.ids.textinput.text = ""
                except:
                    error_prompt("Too Many Search Terms Added")
            else:
                error_prompt("Already Added")
        else:
            error_prompt("Nothing In The Input Box")
    
    def remove_all(self):
        self.ids.grid.clear_widgets()

    search_terms = search_terms
    def continue_or_not(self):
        global config
        config.__setitem__("search_terms", str(search_terms))
        print(config)
        with open("assets/config.txt","a+") as config_file:
            config_file.write(str(config))
            config_file.close()
        if not search_terms == []:
            self.manager.transition.direction ='left'
            self.manager.current = "script_run"
        else: 
            error_prompt("No Search Terms Selected")
    def web(self):
        webbrowser.open('https://www.pexels.com')

class script_runScreen(Screen):
    config = open('assets/config.txt', 'a+').read().rstrip()
    def web(self):
        webbrowser.open('https://www.pexels.com')


class Download_Background_ImagesApp(App):
    def build(self):
        global screens,sm
        sm = ScreenManager()
        sm.add_widget(folder_selectScreen(name="folder_select"))
        sm.add_widget(image_amountScreen(name="image_amount"))
        sm.add_widget(search_termsScreen(name="search_terms"))
        sm.add_widget(script_runScreen(name="script_run"))
        
        return sm

if __name__ == '__main__':
    __init__()
    Download_Background_ImagesApp().run()