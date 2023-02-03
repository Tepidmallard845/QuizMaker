#python C:\Projects-BIG-\Websites\PYmodern-first\base.py

import customtkinter

#Light="light", Dark="dark" or Defualt/Custom="System"
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")#"blue","green","dark-blue"

#very basic graphical interface
root = customtkinter.CTk()
root.geometry("500x350")#pixels

#login logic
def login():
    print("test successful")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)#can also use frame.grid()

label = customtkinter.CTkLabel(master=frame, text="Login System")#, text_font=("Roboto",24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()
