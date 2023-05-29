import customtkinter
from UI import intercafe

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')

window = customtkinter.CTk()
window.geometry('500x350')
window.title('Database Management Center')
window.iconbitmap('database_IconBlue.ico')

def exit():
    window.destroy()

def authenticate(user_var, pass_var, frame):
    if user_var == 'admin' and pass_var == 'admin':
        exit()
        intercafe()
    else:
        label = customtkinter.CTkLabel(frame, text='Usuário ou senha inválida!', text_color='red')
        label.pack(padx=10, pady=30)

        
def login():

    frame = customtkinter.CTkFrame(master=window)
    frame.pack(padx=60, pady=20, fill='both', expand=True)

    label = customtkinter.CTkLabel(frame, text='Fazer Login', font=('Consolas', 24))
    label.pack(padx=10, pady=10)

    user = customtkinter.CTkEntry(frame, placeholder_text='Usuário',  font=('Roboto', 12))
    user.pack(padx=10, pady=10)

    password = customtkinter.CTkEntry(frame, placeholder_text='Senha', show='*',  font=('Roboto', 12))
    password.pack(padx=10, pady=10)

    checkbox = customtkinter.CTkCheckBox(frame,  text='Lembre-me', font=('Roboto', 12))
    checkbox.pack(padx=10, pady=10)

    def login_button_click():
        user_var = user.get()
        pass_var = password.get()
        authenticate(user_var, pass_var, frame)

    button = customtkinter.CTkButton(frame, text='Entrar', font=('Roboto', 12), command=login_button_click)
    button.pack(padx=10, pady=10)

login()
window.mainloop()