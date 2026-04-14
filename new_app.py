# Step 1 ==> import libraries 
from kivy.app import App                      # base class , its manages app lifecycle (start,run,stop)
from kivy.uix.gridlayout import GridLayout    # container that arranges child widgets in a grid (rows and columns) , like a table
from kivy.uix.label import Label              # used to display text on screen , like titles or descriptions.
from kivy.uix.textinput import TextInput      # an text field where users can type input , like a form filed.
from kivy.uix.button import Button            # a clicked button that can trigger actions when pressed.
from kivy.graphics import Color , Rectangle 


# Step 2 ==> Building the App (Base class)
class childApp(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # step 1 ==> layout settings 
        self.cols = 2
        self.padding = 20 
        self.spacing = 15 

        # step 2 ==> background color (black)
        with self.canvas.before:
            Color(0,0,0,1)
            self.rect = Rectangle(size = self.size , pos = self.pos)

        self.bind(size = self.update_rect , pos = self.update_rect)

        # step 3 ==> add title to the page form 
        self.add_widget(Label(text = "Student Form App" , font_size = 28 , bold = True , color = (1,0.84,0,1) , size_hint_y = None , height = 50))

        # step 4 ==> add empty space 
        self.add_widget(Label())

        # step 5 ==> add input fileds 
        self.s_id = self.create_input("Student ID")
        self.s_name = self.create_input("Student Name")
        self.s_gender = self.create_input("Student Gender")
        self.s_country = self.create_input("Student Country")
        self.s_year = self.create_input("Student Year")
        self.s_marks = self.create_input("Student Marks")

        # step 6 ==> add button 
        self.press = Button(text = "Submit" , size_hint = (1,None) , height = 50 , background_color = (0.8 ,0.6 ,0 ,1) ,color = (0,0,0,1),bold=True )
        self.press.bind(on_press=self.click)
        self.add_widget(Label())
        self.add_widget(self.press)

    # step 7 ==> build create input function 
    def create_input(self , hint):
        self.add_widget(Label(text = hint , color = (1,0.84,0,1), font_size = 16))

        text_input = TextInput(hint_text = hint ,multiline = False , padding = (10,10),background_color=(0.1, 0.1, 0.1, 1),foreground_color=(1, 0.84, 0, 1), cursor_color=(1, 0.84, 0, 1)   )

        self.add_widget(text_input)

        return text_input
        
    # step 8 ==> function to update background 
    def update_rect(self , *args):
        self.rect.pos = self.pos 
        self.rect.size = self.size 

    # step 9 ==> function click button 
    def click(self , instance):
        print("Student ID:", self.s_id.text)
        print("Student Name:", self.s_name.text)
        print("Gender:", self.s_gender.text)
        print("Country:", self.s_country.text)
        print("Year:", self.s_year.text)
        print("Marks:", self.s_marks.text)


class parentApp(App):
    def build(self):
        return childApp()
    

if __name__ == "__main__":
    parentApp().run()