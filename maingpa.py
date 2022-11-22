from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty
import datetime
from datetime import date
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
import json



class HomePage(MDScreen):
    pass
class TodoCard(FakeRectangularElevationBehavior,MDFloatLayout):
    title = StringProperty()
    description = StringProperty()


class MainApp(MDApp):
    def build(self):
        global screen_manager
        self.title ="Ä Goals"
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Screens/Main.kv"))
        screen_manager.add_widget(Builder.load_file("Screens/Login.kv"))
        screen_manager.add_widget(Builder.load_file("Screens/SignUp.kv"))
        screen_manager.add_widget(Builder.load_file('Screens/PageScreens.kv'))
        screen_manager.add_widget(Builder.load_file('Screens/Addtodo.kv'))
        screen_manager.add_widget(Builder.load_file('Screens/todo.kv'))
        



        Window.size = [300, 600]
        return screen_manager

    def on_start(self):
        today = date.today()
        wd = date.weekday(today)
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().strftime("%b"))
        day = str(datetime.datetime.now().strftime("%d"))
        screen_manager.get_screen("todoScreen").date.text = f"{days[wd]}, {day} {month} {year}"
    
    def on_complete(self,checkbox, value,description,bar):
        if value:
            description.text = f"[s]{description.text}[/s]"
            bar.md_bg_color =0,179/255,0,1
        else:
            remove = ["[s]", "[/s]"]
            for i in remove:
                description.text = description.text.replace(i,"")
                bar.md_bg_color =1,170/255,23/255,1

    def add_todo(self,title,description):
        if title !="" and description !="" and len(title)<21 and len(description)<61:
            screen_manager.transition.direction = "right"
            screen_manager.current = "todoScreen"
            
            screen_manager.get_screen("todoScreen").todo_list.add_widget(TodoCard(title=title, description=description))
            screen_manager.get_screen("add_todo").description.text =""
        elif title =="":
            Snackbar(text="Title is missing!",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif description =="":
            Snackbar(text="Description is missing!",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif len(title)>21:
            Snackbar(text="Title too long!must<20",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif len(description)>61:
            Snackbar(text="Description too long! must<60",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()


    def userSignUp(self,user_name,user_email,user_password):
        usr_database = open('assets/user_data.json','r')
        data = usr_database.read()
        usr_datar = json.loads(data)

        user_name = screen_manager.get_screen("SignUp").usr_name.text
        user_email = screen_manager.get_screen("SignUp").usr_email.text
        user_password = screen_manager.get_screen("SignUp").usr_pass.text
        
       
        #m-put in own conditional branch
        if user_name !="" and user_email !="" and user_password !="" and len(user_name)<21 and len(user_password)<60:
            usr_datar['sheets'][0]['lines'][0]['usr_name'] = user_name
            usr_datar['sheets'][0]['lines'][0]['usr_email'] = user_email
            usr_datar['sheets'][0]['lines'][0]['usr_password']= user_password
            user_dbase =open('assets/user_data.json','w')
            
            json.dump(usr_datar,user_dbase,indent=4)
            screen_manager.transition.direction = "right"
            screen_manager.current = "Home"

        elif user_name =="":
            Snackbar(text="Username  missing!",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif user_email =="":
            Snackbar(text="Email  missing!",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif user_password =="":
            Snackbar(text="Password missing!",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif len(user_name)>21:
            Snackbar(text="Username must<21",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif len(user_password)>61 :
            Snackbar(text="Password must<61",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()

    def userlogin(self,user_name,user_password):
        usr_database = open('assets/user_data.json','r')
        data = usr_database.read()
        usr_datar = json.loads(data)
            
        user_name = screen_manager.get_screen("Login").usr_Username.text
        user_password = screen_manager.get_screen("Login").usr_password.text
        
        usname = usr_datar['sheets'][0]['lines'][0]['usr_name'] 
        uspassword = usr_datar['sheets'][0]['lines'][0]['usr_password']

        if user_name !="" and user_password !="" and user_name == usname and user_password == uspassword:
            screen_manager.transition.direction = "right"
            screen_manager.current = "Home"

        elif user_name =="":
            Snackbar(text="Username  missing!",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif user_password =="":
            Snackbar(text="Password missing!",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif user_name != usname:
            Snackbar(text="Invalid username",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()
        elif user_password != uspassword:
            Snackbar(text="Invalid password",snackbar_x ="10dp",snackbar_y ="10dp",
                    size_hint_x =(Window.width -(dp(10)*2))/Window.width, bg_color=(1,170/255,23/255,1),
                    font_size ="19dp").open()

    #m-add call append to database funct 



"""  def stringSearch(self,stringTosearch ):
        # Input the key value that you want to search
        stringTosearch = input("Enter a key value: \n")
        # load the json data
        database = open('course_database.json','r')
        data = database.read()
        #pass string as dictionary
        datar =json.loads(data)
        # Search the key value using 'in' operator
        if stringTosearch in datar:
            # Print the success message and the value of the key
            print("%s is found in JSON data" %stringTosearch)
            print("The value of", stringTosearch,"is", datar[stringTosearch])
        else:
            # Print the message if the value does not exist
            print("%s is not found in JSON data" %stringTosearch)
    def userrSignUp(self,usr_name,usr_email,usr_password):
        pass """

    


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


    


