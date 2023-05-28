from Index import *
from tkinter import *
from tkinter import ttk
import sqlite3 as banco


conexão = banco.connect('Database/Database.db')
cursor = conexão.cursor()

criar_tabelas()


def buscar():
    Table.delete(*Table.get_children())
    textInput_id.insert(END, "%")
    id = textInput_id.get()
    cursor.execute(""" SELECT * FROM Pessoa WHERE id LIKE '%s' ORDER BY id""" %id)
    buscartabela = cursor.fetchall()
    for i in buscartabela:
        Table.insert("", END, values=i)
        clearInputs()



def clearInputs():
    textInput_N.delete(0, END)
    textInput_id.delete(0, END)
    textInput_age.delete(0, END)
    textInput_cpf.delete(0, END)

def Quit(): 
    window.destroy()

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('800x520')
window.maxsize(width=800, height=520)
#window.maxsize(width=width, height=height)
window.minsize(width=600, height=370)
window.title('Database')

#grid
frame1 = Frame(window, bg='#ddd')
frame1.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)

frame2 = Frame(window, bg='#c9c9c9')
frame2.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)

#Table pessoa
Table = ttk.Treeview(frame2, height=3, column=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7'))
Table2 = ttk.Treeview(frame2, height=3, column=('Col1', 'Col2', 'Col3', 'Col4', 'Col5'))

relx_b = 0.0

query = Button(frame1, text='Consultar', bd=0, command=buscar)
query.place(relx=relx_b, rely=0.09, relheight=0.08, relwidth=1.0)

insert = Button(frame1, text='Inserir', bd=0)
insert.place(relx=relx_b, rely=0.2, relheight=0.08, relwidth=1.0)

update = Button(frame1, text ='Atualizar', bd=0)
update.place(relx=relx_b, rely=0.3, relheight=0.08, relwidth=1.0)

delete = Button(frame1, text='Deletar', bd=0)
delete.place(relx=relx_b, rely=0.4, relheight=0.08, relwidth=1.0)


def mostrar_tabela1():
    Table2.pack_forget() 
    Table = ttk.Treeview(frame2, height=3, column=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7'))
    Table.heading('#0', text='')
    Table.heading('#1', text='ID')
    Table.heading('#2', text='CPF')
    Table.heading('#3', text='Nome')
    Table.heading('#4', text='Nome do meio')
    Table.heading('#5', text='Sobrenome')
    Table.heading('#6', text='Idade')
    Table.heading('#7', text='Conta')

    Table.column('#0', width=1, stretch=NO)
    Table.column('#1', width=50)
    Table.column('#2', width=100)
    Table.column('#3', width=100)
    Table.column('#4', width=120)
    Table.column('#5', width=100)
    Table.column('#6', width=50)
    Table.column('#7', width=100)
    Table.place(relx=0.025, rely=0.01, relwidth=0.95, relheight=0.55)
    scroolTable = Scrollbar(frame2, orient='vertical')
    Table.configure(yscrollcommand = scroolTable.set)
    scroolTable.place(relx=0.97, rely=0.01, relwidth=0.95, relheight=0.55)

    # Buttons and text inputs 1
    label = Label(frame2, text='ID', bg='#c9c9c9')
    label.place(relx=0.1, rely=0.65)
    label = Label(frame2, text='Nome', bg='#c9c9c9')
    label.place(relx=0.25, rely=0.65)
    label = Label(frame2, text='CPF', bg='#c9c9c9')
    label.place(relx=0.55, rely=0.65)
    label = Label(frame2, text='Idade', bg='#c9c9c9')
    label.place(relx=0.75, rely=0.65)

    textInput_id = Entry(frame2, bd=0)
    textInput_id.place(relx=0.1, rely=0.7, relwidth=0.08)
    textInput_N = Entry(frame2, bd=0)
    textInput_N.place(relx=0.25, rely=0.7, relwidth=0.2)
    textInput_cpf = Entry(frame2, bd=0)
    textInput_cpf.place(relx=0.55, rely=0.7, relwidth=0.08)
    textInput_age = Entry(frame2, bd=0)
    textInput_age.place(relx=0.75, rely=0.7, relwidth=0.08)

    clear = Button(frame2, text='Limpar',  bd=0.5, command=clearInputs)
    clear.place(relx=0.8, rely=0.85)

    Enviar = Button(frame2, text='Enviar', bd=0.5)
    Enviar.place(relx=0.9, rely=0.85)

    reset = Button(frame2, text='Restaurar', bd=0.5)
    reset.place(relx=0.68, rely=0.85)

    # Buttons and text inputs 2
    label = Label(frame2, text='ID', bg='#c9c9c9')
    label.place(relx=0.1, rely=0.65)
    label = Label(frame2, text='Nome', bg='#c9c9c9')
    label.place(relx=0.25, rely=0.65)
    label = Label(frame2, text='CPF', bg='#c9c9c9')
    label.place(relx=0.55, rely=0.65)
    label = Label(frame2, text='Idade', bg='#c9c9c9')
    label.place(relx=0.75, rely=0.65)

    textInput_id = Entry(frame2, bd=0)
    textInput_id.place(relx=0.1, rely=0.7, relwidth=0.08)
    textInput_N = Entry(frame2, bd=0)
    textInput_N.place(relx=0.25, rely=0.7, relwidth=0.2)
    textInput_cpf = Entry(frame2, bd=0)
    textInput_cpf.place(relx=0.55, rely=0.7, relwidth=0.08)
    textInput_age = Entry(frame2, bd=0)
    textInput_age.place(relx=0.75, rely=0.7, relwidth=0.08)

    clear = Button(frame2, text='Limpar',  bd=0.5, command=clearInputs)
    clear.place(relx=0.8, rely=0.85)

    Enviar = Button(frame2, text='Enviar', bd=0.5)
    Enviar.place(relx=0.9, rely=0.85)

    reset = Button(frame2, text='Restaurar', bd=0.5)
    reset.place(relx=0.68, rely=0.85)

def mostrar_tabela2():
    Table.pack_forget()  
    Table2 = ttk.Treeview(frame2, height=3, column=('Col1', 'Col2', 'Col3', 'Col4', 'Col5'))
    Table2.heading('#0', text='')
    Table2.heading('#1', text='Agência')
    Table2.heading('#2', text='Numero')
    Table2.heading('#3', text='Saldo')
    Table2.heading('#4', text='Gerente')
    Table2.heading('#5', text='Titular')

    Table2.column('#0', width=1, stretch=NO)
    Table2.column('#1', width=50)
    Table2.column('#2', width=100)
    Table2.column('#3', width=100)
    Table2.column('#4', width=120)
    Table2.column('#5', width=100)
    Table2.place(relx=0.025, rely=0.01, relwidth=0.95, relheight=0.55)
    scroolTable = Scrollbar(frame2, orient='vertical')
    Table2.configure(yscrollcommand = scroolTable.set)
    scroolTable.place(relx=0.97, rely=0.01, relwidth=0.95, relheight=0.55)

    # Buttons and text inputs 1
    label = Label(frame2, text='ID', bg='#c9c9c9')
    label.place(relx=0.1, rely=0.65)
    label = Label(frame2, text='Nome', bg='#c9c9c9')
    label.place(relx=0.25, rely=0.65)
    label = Label(frame2, text='CPF', bg='#c9c9c9')
    label.place(relx=0.55, rely=0.65)
    label = Label(frame2, text='Idade', bg='#c9c9c9')
    label.place(relx=0.75, rely=0.65)

    textInput_id = Entry(frame2, bd=0)
    textInput_id.place(relx=0.1, rely=0.7, relwidth=0.08)
    textInput_N = Entry(frame2, bd=0)
    textInput_N.place(relx=0.25, rely=0.7, relwidth=0.2)
    textInput_cpf = Entry(frame2, bd=0)
    textInput_cpf.place(relx=0.55, rely=0.7, relwidth=0.08)
    textInput_age = Entry(frame2, bd=0)
    textInput_age.place(relx=0.75, rely=0.7, relwidth=0.08)

    clear = Button(frame2, text='Limpar',  bd=0.5, command=clearInputs)
    clear.place(relx=0.8, rely=0.85)

    Enviar = Button(frame2, text='Enviar', bd=0.5)
    Enviar.place(relx=0.9, rely=0.85)

    reset = Button(frame2, text='Restaurar', bd=0.5)
    reset.place(relx=0.68, rely=0.85)

    # Buttons and text inputs 2
    label = Label(frame2, text='ID', bg='#c9c9c9')
    label.place(relx=0.1, rely=0.65)
    label = Label(frame2, text='Nome', bg='#c9c9c9')
    label.place(relx=0.25, rely=0.65)
    label = Label(frame2, text='CPF', bg='#c9c9c9')
    label.place(relx=0.55, rely=0.65)
    label = Label(frame2, text='Idade', bg='#c9c9c9')
    label.place(relx=0.75, rely=0.65)

    textInput_id = Entry(frame2, bd=0)
    textInput_id.place(relx=0.1, rely=0.7, relwidth=0.08)
    textInput_N = Entry(frame2, bd=0)
    textInput_N.place(relx=0.25, rely=0.7, relwidth=0.2)
    textInput_cpf = Entry(frame2, bd=0)
    textInput_cpf.place(relx=0.55, rely=0.7, relwidth=0.08)
    textInput_age = Entry(frame2, bd=0)
    textInput_age.place(relx=0.75, rely=0.7, relwidth=0.08)

    clear = Button(frame2, text='Limpar',  bd=0.5, command=clearInputs)
    clear.place(relx=0.8, rely=0.85)

    Enviar = Button(frame2, text='Enviar', bd=0.5)
    Enviar.place(relx=0.9, rely=0.85)

    reset = Button(frame2, text='Restaurar', bd=0.5)
    reset.place(relx=0.68, rely=0.85)



#Menu
menuBar = Menu(window)
window.config(menu=menuBar)
filemenu = Menu(menuBar)
filemenu2 = Menu(menuBar)

menuBar.add_cascade(label='Opções', menu=filemenu)
menuBar.add_cascade(label='Tabelas', menu=filemenu2)

filemenu.add_command(label='Sair', command=Quit)
filemenu2.add_command(label='Pessoas', command=mostrar_tabela1)
filemenu2.add_command(label='Contas', command=mostrar_tabela2)
window.mainloop()
