import customtkinter as  ctk
import time as t

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")
class GUI():
        def __init__(self):
            self.window = ctk.CTk()
            self.window.geometry("500x300")
            self.window.title("Notes App")
           #Header
            intro = ctk.CTkLabel(self.window, text="Welcome To Notes App" ,font=("cursive", 30))
            intro.pack(padx=20,pady=20)
            #Notes input
            intro2 = ctk.CTkLabel(self.window, text="""Would You Like To Create Or Open A File""" ,font= ("Arial",20))
            intro2.pack(pady=20,padx=20)  
            
            
            
            
            def get():
                self.window = ctk.CTk()
            
                self.window.geometry("400x300")
            
                self.window.title("Notes App")
                
                input_label1 = ctk.CTkLabel(self.window, text="File Name" ,font=("Arial", 15))
                input_label1.pack(padx=1,pady=1)
                input_2 = ctk.CTkEntry(self.window,placeholder_text="File name",width=300)
                input_2.pack()
                #file extention input
                input_label2 = ctk.CTkLabel(self.window, text="File Extention Type" ,font=("Arial", 15))
                input_label2.pack(padx=1,pady=1)
                input_3 = ctk.CTkEntry(self.window, placeholder_text= "txt",width=300)
                input_3.pack()
            
                def find_note():
                    file_name = input_2.get()
                    file_type = input_3.get()
                    self.save = f"{file_name}.{file_type}"
                    self.window.destroy() 
                    self.Third_window()
                find_note
                btn = ctk.CTkButton(self.window,text="Find File" ,font=("Arial",15) ,command=find_note )
                btn.pack(padx=10,pady=5)
                self.window.mainloop()
            
            
            
            
            
            
            btn = ctk.CTkButton(self.window,text="Open Existing File " ,font=("Arial",15) ,command =get )
            btn.pack(pady= 20,padx=20)
            def tran():
                self.window.destroy()
                self.First_window()
                
                
            btn2 = ctk.CTkButton(self.window,text="Create New File " ,font=("Arial",15) ,command=tran)
            btn2.pack(padx=10,pady=5)
            self.window.mainloop()
            

        def First_window(self) :
            self.window = ctk.CTk()
            
            self.window.geometry("600x500")
            
            self.window.title("Notes App")
            def tran():
                GUI()
                
                
            
            btn2 = ctk.CTkButton(self.window,text="Home " ,font=("Arial",15) ,command = tran)
            btn2.pack(padx=10,pady=5)
           
            
             
           #Header
            intro = ctk.CTkLabel(self.window, text="Welcome To Notes App" ,font=("cursive", 20))
            intro.pack(padx=20,pady=20)
            #Notes input
            self.input = ctk.CTkTextbox(self.window, height=250,width=400,font=("cursive",15))
            self.input.pack()
            btn  = ctk.CTkButton(self.window,text="Save Note " ,font=("Arial",15) ,command = self.new_window)
            btn.pack()
            self.window.mainloop()

            
            
             
        def new_window(self):
                self.window = ctk.CTk()
                self.window.geometry("400x300")
                self.window.title("Notes App")
                input_label1 = ctk.CTkLabel(self.window, text="File Name" ,font=("Arial", 15))
                input_label1.pack(padx=1,pady=1)
                input_2 = ctk.CTkEntry(self.window,placeholder_text="File name",width=300)
                input_2.pack()
                #file extention input
                input_label2 = ctk.CTkLabel(self.window, text="File Extention Type" ,font=("Arial", 15))
                input_label2.pack(padx=1,pady=1)
                input_3 = ctk.CTkEntry(self.window, placeholder_text= "txt",width=300)
                input_3.pack()
            
                def save_note():
                    file_name = input_2.get()
                    file_type = input_3.get()
                    get_time = t.localtime()
                    time = f"Time Saved => {get_time.tm_hour}:{get_time.tm_min}"
                    text= self.input.get("1.0",ctk.END)
                    save = open(f"{file_name}.{file_type}", "w")
                    save.write(f"{text}\n {time}")
                    save.close() 
                    self.window.destroy() 
                btn = ctk.CTkButton(self.window,text="Save note" ,font=("Arial",15) ,command=save_note )
                btn.pack(padx=10,pady=5)
                self.window.mainloop()
        def Third_window(self):
                self.window = ctk.CTk()
                self.window.geometry("400x300")
                self.window.title("Notes App")
                file = open(self.save,"r" ) 
                text = file.read()
                file.close()
                input_label1 = ctk.CTkLabel(self.window, text=text ,font=("Arial", 15))
                input_label1.pack(padx=10,pady=10)
                self.window.mainloop()
                #create new window           
GUI()
