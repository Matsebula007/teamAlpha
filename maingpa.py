from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import json


'''
class HomePage(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.theme_cls_primary_palette = "LightBlue"
        Builder.load_file('ScreensDesign.kv')
        return HomePage()

'''

if __name__ == "__main__":
    #MainApp().run()
    #read database and pass as string    
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
    


    


