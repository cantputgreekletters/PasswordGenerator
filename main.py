#Imports
from random import randint as rn
import json
import tkinter as tk
#Constants
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters += letters.lower()
numbers = "0123456789"
Symbols = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/" + '"'
AllCharacters = tuple(letters + numbers + Symbols)
file = "passwords.json"
#Classes

class ListBoxSearch:
    def __init__(self,master) -> None:
        self.master = master
        self.search = tk.Entry(master=self.master)
        self.lb = tk.Listbox(master=self.master)
        self.lb.bind("<<ListboxSelect>>",self.on_select)
        self.button = tk.Button(master=self.master,command=self.click,text="Search")
        self.search_text = None
        self.selected = None
        self.inserted = []
    def insert(self,index,element):
        self.lb.insert(index,element)
        self.inserted.append(element)
    
    def pack(self):
        self.search.pack()
        self.button.pack()
        self.lb.pack()

    def on_select(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.selected = value

    def update_lb(self):
        
        if self.search_text:
            print(self.search_text)
            new_items = []
            lb_items = self.lb.get(0,self.lb.size())
            print(lb_items)
            for item in self.inserted:
                if self.search_text.lower() in item.lower():
                    new_items.append(item)
            self.lb.delete(0,self.lb.size())
            idx = 0
            for item in new_items:
                idx += 1
                self.lb.insert(idx,item)

        else:
            if len(self.lb.get(0,self.lb.size())) != len(self.inserted):
                self.lb.delete(0,self.lb.size())
                idx = 0
                for element in self.inserted:
                    idx += 1
                    self.lb.insert(idx, element)


    def click(self):
        self.search_text = str(self.search.get())
        self.update_lb()

class Window:
    def __init__(self) -> None:
        self.window = tk.Tk()
       

    def open(self):
        
        self.window.mainloop()
   
    
class GenerateWindow(Window):
    def __init__(self) -> None:
        super().__init__()        
        self.__settings()
        
    def __settings(self):
        
        self.window.title("Generate Window")
        self.window.geometry('600x500')
    

class PasswordsWindow(Window):
    def __init__(self) -> None:
        super().__init__()
        self.__settings()
    
    def __SettingWidgets(self):
        ins = ListBoxSearch(master=self.window)
        ins.pack()
        #Insert password keys
        with open(file,"r",encoding="utf-8") as f:
            data = json.load(f)
            idx = 0
            for key in data["Platforms"].keys():
                idx += 1
                ins.insert(idx,key)
        
        #Labels for showing the contents
        
        

    def __settings(self):
        self.window.title("Passwords Window")
        self.window.geometry('600x500')
        self.__SettingWidgets()
        
    
    

class MainWindow(Window):
    def __init__(self) -> None:
        super().__init__()
        
        self.GenerateWindowButton = None
        self.PasswordsWindow = None
        self.__settings()
        
    def __settings(self):
        self.window.title("Main Window")
        self.window.geometry('600x500')
        self.__SettingWidgets()
    
    def __Make_PG_Window(self):
        gw = GenerateWindow()
        gw.open()
    
    def __Make_P_Window(self):
        Pw = PasswordsWindow()
        Pw.open()
    
    def __SettingWidgets(self):
        self.GenerateWindowButton = tk.Button(master=self.window,text="Generate Password",command=self.__Make_PG_Window)
        self.GenerateWindowButton.pack()
        self.PasswordsWindow = tk.Button(master=self.window,text='Passwords',command=self.__Make_P_Window)
        self.PasswordsWindow.pack()
        tk.Button(master=self.window,text='Quit',command=self.window.destroy).pack()
    
    
#Functions
def GeneratePassword(length = 12):
    password = ''
    for _ in range(length):
        password += AllCharacters[rn(0,len(AllCharacters) - 1)]
    
    return password
   
#Main

#Testing
mw = MainWindow()
mw.open()


password = GeneratePassword()
print(password)

