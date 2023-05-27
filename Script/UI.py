from tkinter import *
#from Trabalho import *

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('800x520')
window.maxsize(width=width, height=height)
window.minsize(width=400, height=320)
window.title('Database')

#grid
frame1 = Frame(window, bg='#eee')
frame1.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)

frame2 = Frame(window, bg='#ddd')
frame2.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)

# Main buttons
relx_b = 0.0

query = Button(frame1, text='Consultar')
query.place(relx=relx_b, rely=0.09, relheight=0.08, relwidth=1.0)

insert = Button(frame1, text='Inserir')
insert.place(relx=relx_b, rely=0.2, relheight=0.08, relwidth=1.0)

delete = Button(frame1, text ='Deletar')
delete.place(relx=relx_b, rely=0.3, relheight=0.08, relwidth=1.0)

update = Button(frame1, text='Atualizar')
update.place(relx=relx_b, rely=0.4, relheight=0.08, relwidth=1.0)

# Buttons and text inputs
clear = Button(frame2, text='Limpar')
clear.place(relx=0.8, rely=0.85)

clear = Button(frame2, text='Enviar')
clear.place(relx=0.9, rely=0.85)


window.mainloop()