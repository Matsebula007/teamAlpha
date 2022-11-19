from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
import json



class HomePage(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        self.title ="Ä Goals"
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Screens/Main.kv"))
        screen_manager.add_widget(Builder.load_file("Screens/Login.kv"))
        screen_manager.add_widget(Builder.load_file("Screens/SignUp.kv"))
        screen_manager.add_widget(Builder.load_file('Screens/PageScreens.kv'))
        Window.size = [300, 600]
        return screen_manager


if __name__ == "__main__":
    MainApp().run()
    #read database and pass as string 

    '''   
    database = open('assets/course_database.json','r')
    data = database.read()
    #pass string as dictionary
    datar =json.loads(data)
    test1name = datar['sheets'][0]['lines'][0]['course_ass'][0]['ass_number'][0]['id']
    

    newmark = float(input("Enter mark : "))
    datar['sheets'][0]['lines'][0]['course_ass'][0]['ass_number'][0]['Mark'] = newmark
    database = open('assets/course_database.json','w')
    json.dump(datar, database)
    test1mar = datar['sheets'][0]['lines'][0]['course_ass'][0]['ass_number'][0]['Mark']
    database.close()
    print( test1name ," : ", test1mar)
    '''


    


