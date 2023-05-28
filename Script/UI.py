from Index import *
from tkinter import *
from tkinter import ttk
import sqlite3 as banco


conexão = banco.connect('Database/Database.db')
cursor = conexão.cursor()

criar_tabelas()

class intercafe():

    def __init__(self):
        self.window = Tk()
        self.config()
        self.menu()
        self.window.mainloop()


    def inserirpessoa(self):
        cpf = self.textInput_cpf.get()
        nome = self.textInput_N.get()
        nomedomeio = self.textInput_N_meio.get()
        sobrenome = self.textInput_sobrenome.get()
        idade = self.textInput_age.get()
        conta = self.textInput_conta.get()
        id = 1500
        id +=1
        cursor.execute(f""" INSERT INTO pessoa(id,cpf, primeiro_nome, nome_do_meio, sobrenome, Idade, conta) VALUES('{id}','{cpf}', '{nome}', '{nomedomeio}', '{sobrenome}', '{idade}', '{conta}')""")
        conexão.commit()


    def inserirconta(self):
        agencia = self.textInput_agen.get()
        numero = self.textInput_num.get()
        saldo = self.textInput_saldo.get()
        gerente = self.textInput_gerente.get()
        titular = self.textInput_titular.get()
        id = 1500
        id +=1
        cursor.execute(f""" INSERT INTO Conta(id,Agência, Número, Saldo, Gerente, Titular) VALUES('{id}','{agencia}', '{numero}', '{saldo}', '{gerente}', '{titular}')""")
        conexão.commit()


    def consultarpessoa(self):
        self.Table.delete(*self.Table.get_children())
        self.textInput_id.insert(END, "%")
        id = self.textInput_id.get()
        cursor.execute(""" SELECT * FROM Pessoa WHERE id LIKE '%s' ORDER BY id""" %id)
        buscartabela = cursor.fetchall()
        for i in buscartabela:
            self.Table.insert("", END, values=i)
            self.clearInputs1()
    

    def consultarconta(self):
        self.Table2.delete(*self.Table2.get_children())
        self.textInput_id2.insert(END, "%")
        id2 = self.textInput_id2.get()
        cursor.execute(""" SELECT * FROM Conta WHERE id LIKE '%s' ORDER BY id""" %id2)
        buscartabela2 = cursor.fetchall()
        for i in buscartabela2:
            self.Table2.insert("", END, values=i)
            self.clearInputs2()


    def buscarpessoa(self):
        self.Table.delete(*self.Table.get_children())
        self.textInput_id.insert(END, "%")
        id = self.textInput_id.get()
        cursor.execute(""" SELECT * FROM Pessoa WHERE id LIKE '%s' ORDER BY id""" %id)
        buscartabela = cursor.fetchall()
        for i in buscartabela:
            self.Table.insert("", END, values=i)
            self.clearInputs1()


    def buscarconta(self):
        self.Table2.delete(*self.Table2.get_children())
        self.textInput_id2.insert(END, "%")
        id = self.textInput_id2.get()
        cursor.execute(""" SELECT * FROM Conta WHERE id LIKE '%s' ORDER BY id""" %id)
        buscartabela2 = cursor.fetchall()
        for i in buscartabela2:
            self.Table2.insert("", END, values=i)
            self.clearInputs2()


    def clearInputs1(self):
        self.textInput_N.delete(0, END)
        self.textInput_id.delete(0, END)
        self.textInput_age.delete(0, END)
        self.textInput_cpf.delete(0, END)
        self.textInput_conta.delete(0, END)
        self.textInput_N_meio.delete(0, END)
        self.textInput_sobrenome.delete(0, END)


    def clearInputs2(self):
        self.textInput_id2.delete(0, END)
        self.textInput_agen.delete(0, END)
        self.textInput_saldo.delete(0, END)
        self.textInput_gerente.delete(0, END)
        self.textInput_num.delete(0, END)
        self.textInput_titular.delete(0, END)

    def Quit(self): 
        self.window.destroy()


    def config(self):
        self.window.geometry('800x520')
        self.window.maxsize(width=800, height=520)
        #window.maxsize(width=width, height=height)
        self.window.minsize(width=600, height=370)
        self.window.title('Database')

        #grid
        self.frame1 = Frame(self.window, bg='#ddd')
        self.frame1.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)

        self.frame2 = Frame(self.window, bg='#c9c9c9')
        self.frame2.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)

        #Table pessoa
        self.Table = ttk.Treeview(self.frame2, height=3, column=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7'))
        self.fTable2 = ttk.Treeview(self.frame2, height=3, column=('Col1', 'Col2', 'Col3', 'Col4', 'Col5'))

    def butõespessoa(self):
        relx_b = 0.0
        query = Button(self.frame1, text='Consultar', bd=0, command=self.buscarpessoa)
        query.place(relx=relx_b, rely=0.09, relheight=0.08, relwidth=1.0)

        insert = Button(self.frame1, text='Inserir', bd=0, command=self.inserirpessoa)
        insert.place(relx=relx_b, rely=0.2, relheight=0.08, relwidth=1.0)

        update = Button(self.frame1, text ='Atualizar', bd=0)
        update.place(relx=relx_b, rely=0.3, relheight=0.08, relwidth=1.0)

        delete = Button(self.frame1, text='Deletar', bd=0)
        delete.place(relx=relx_b, rely=0.4, relheight=0.08, relwidth=1.0)


    def butõesconta(self):
        relx_b = 0.0
        query = Button(self.frame1, text='Consultar', bd=0, command=self.consultarconta)
        query.place(relx=relx_b, rely=0.09, relheight=0.08, relwidth=1.0)

        insert = Button(self.frame1, text='Inserir', bd=0, command=self.inserirconta)
        insert.place(relx=relx_b, rely=0.2, relheight=0.08, relwidth=1.0)

        update = Button(self.frame1, text ='Atualizar', bd=0)
        update.place(relx=relx_b, rely=0.3, relheight=0.08, relwidth=1.0)

        delete = Button(self.frame1, text='Deletar', bd=0)
        delete.place(relx=relx_b, rely=0.4, relheight=0.08, relwidth=1.0)

    
    def frame_1(self):
        self.frame1 = Frame(self.window, bg='#ddd')
        self.frame1.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)


    def frame_2(self):
         
        self.frame2 = Frame(self.window, bg='#c9c9c9')
        self.frame2.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)


    def mostrar_tabela1(self):
            self.frame1.destroy()
            self.frame2.destroy()
            self.frame_2()
            self.frame_1()
            self.Table = ttk.Treeview(self.frame2, height=3, column=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7'))
            self.Table.heading('#0', text='')
            self.Table.heading('#1', text='ID')
            self.Table.heading('#2', text='CPF')
            self.Table.heading('#3', text='Nome')
            self.Table.heading('#4', text='Nome do meio')
            self.Table.heading('#5', text='Sobrenome')
            self.Table.heading('#6', text='Idade')
            self.Table.heading('#7', text='Conta')

            self.Table.column('#0', width=1, stretch=NO)
            self.Table.column('#1', width=50)
            self.Table.column('#2', width=100)
            self.Table.column('#3', width=100)
            self.Table.column('#4', width=120)
            self.Table.column('#5', width=100)
            self.Table.column('#6', width=50)
            self.Table.column('#7', width=100)
            self.Table.place(relx=0.025, rely=0.01, relwidth=0.95, relheight=0.55)
            scroolTable = Scrollbar(self.frame2, orient='vertical')
            self.Table.configure(yscrollcommand = scroolTable.set)
            scroolTable.place(relx=0.97, rely=0.01, relwidth=0.95, relheight=0.55)
            self.labelspessoa()
            self.butõespessoa()
            

    def labelspessoa(self):
            label = Label(self.frame2, text='ID', bg='#c9c9c9')
            label.place(relx=0.1, rely=0.65)
            label = Label(self.frame2, text='Nome', bg='#c9c9c9')
            label.place(relx=0.25, rely=0.65)
            label = Label(self.frame2, text='Nome Do Meio', bg='#c9c9c9')
            label.place(relx=0.50, rely=0.65)
            label = Label(self.frame2, text='Sobrenome', bg='#c9c9c9')
            label.place(relx=0.75, rely=0.65)
            label = Label(self.frame2, text='CPF', bg='#c9c9c9')
            label.place(relx=0.1, rely=0.75)
            label = Label(self.frame2, text='Idade', bg='#c9c9c9')
            label.place(relx=0.35, rely=0.75)
            label = Label(self.frame2, text='Conta', bg='#c9c9c9')
            label.place(relx=0.47, rely=0.75)

            self.textInput_id = Entry(self.frame2, bd=0)
            self.textInput_id.place(relx=0.1, rely=0.7, relwidth=0.08)
            self.textInput_N = Entry(self.frame2, bd=0)
            self.textInput_N.place(relx=0.25, rely=0.7, relwidth=0.2)
            self.textInput_N_meio = Entry(self.frame2, bd=0)
            self.textInput_N_meio.place(relx=0.50, rely=0.7, relwidth=0.2)
            self.textInput_sobrenome = Entry(self.frame2, bd=0)
            self.textInput_sobrenome.place(relx=0.75, rely=0.7, relwidth=0.2)
            self.textInput_cpf = Entry(self.frame2, bd=0)
            self.textInput_cpf.place(relx=0.1, rely=0.8, relwidth=0.2)
            self.textInput_age = Entry(self.frame2, bd=0)
            self.textInput_age.place(relx=0.35, rely=0.8, relwidth=0.08)
            self.textInput_conta = Entry(self.frame2, bd=0)
            self.textInput_conta.place(relx=0.47, rely=0.8, relwidth=0.08)

            clear = Button(self.frame2, text='Limpar',  bd=0.5, command=self.clearInputs1)
            clear.place(relx=0.8, rely=0.85)

            Enviar = Button(self.frame2, text='Enviar', bd=0.5)
            Enviar.place(relx=0.9, rely=0.85)

            self.buscarpessoa()

    def mostrar_tabela2(self):
            self.frame2.destroy()
            self.frame1.destroy()
            self.frame_1()
            self.frame_2()
            self.Table2 = ttk.Treeview(self.frame2, height=3, column=('Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6'))
            self.Table2.heading('#0', text='')
            self.Table2.heading('#1', text='ID')
            self.Table2.heading('#2', text='Agência')
            self.Table2.heading('#3', text='Numero')
            self.Table2.heading('#4', text='Saldo')
            self.Table2.heading('#5', text='Gerente')
            self.Table2.heading('#6', text='Titular')

            self.Table2.column('#0', width=1, stretch=NO)
            self.Table2.column('#1', width=25)
            self.Table2.column('#2', width=50)
            self.Table2.column('#3', width=100)
            self.Table2.column('#4', width=100)
            self.Table2.column('#5', width=120)
            self.Table2.column('#6', width=100)
            self.Table2.place(relx=0.025, rely=0.01, relwidth=0.95, relheight=0.55)
            scroolTable = Scrollbar(self.frame2, orient='vertical')
            self.Table2.configure(yscrollcommand = scroolTable.set)
            scroolTable.place(relx=0.97, rely=0.01, relwidth=0.95, relheight=0.55)
            self.labelsconta()
            self.butõesconta()

    def labelsconta(self):
            label = Label(self.frame2, text='ID', bg='#c9c9c9')
            label.place(relx=0.45, rely=0.75)
            label = Label(self.frame2, text='Agência', bg='#c9c9c9')
            label.place(relx=0.1, rely=0.75)
            label = Label(self.frame2, text='Número', bg='#c9c9c9')
            label.place(relx=0.1, rely=0.65)
            label = Label(self.frame2, text='Saldo', bg='#c9c9c9')
            label.place(relx=0.35, rely=0.65)
            label = Label(self.frame2, text='Gerente', bg='#c9c9c9')
            label.place(relx=0.55, rely=0.65)
            label = Label(self.frame2, text='Titular', bg='#c9c9c9')
            label.place(relx=0.25, rely=0.75)


            self.textInput_id2 = Entry(self.frame2, bd=0)
            self.textInput_id2.place(relx=0.45, rely=0.80, relwidth=0.08)
            self.textInput_agen = Entry(self.frame2, bd=0)
            self.textInput_agen.place(relx=0.1, rely=0.80, relwidth=0.08)
            self.textInput_num = Entry(self.frame2, bd=0)
            self.textInput_num.place(relx=0.1, rely=0.7, relwidth=0.2)
            self.textInput_saldo = Entry(self.frame2, bd=0)
            self.textInput_saldo.place(relx=0.35, rely=0.70, relwidth=0.15)
            self.textInput_gerente = Entry(self.frame2, bd=0)
            self.textInput_gerente.place(relx=0.55, rely=0.70, relwidth=0.1)
            self.textInput_titular = Entry(self.frame2, bd=0)
            self.textInput_titular.place(relx=0.25, rely=0.80, relwidth=0.08)

            clear = Button(self.frame2, text='Limpar',  bd=0.5, command=self.clearInputs2)
            clear.place(relx=0.8, rely=0.85)

            Enviar = Button(self.frame2, text='Enviar', bd=0.5)
            Enviar.place(relx=0.9, rely=0.85)

            self.buscarconta()


#Menu
    def menu(self):
        menuBar = Menu(self.window)
        self.window.config(menu=menuBar)
        filemenu = Menu(menuBar)
        filemenu2 = Menu(menuBar)

        menuBar.add_cascade(label='Opções', menu=filemenu)
        menuBar.add_cascade(label='Tabelas', menu=filemenu2)

        filemenu.add_command(label='Sair', command=self.Quit)
        filemenu2.add_command(label='Pessoas', command=self.mostrar_tabela1)
        filemenu2.add_command(label='Contas', command=self.mostrar_tabela2)
        self.window.mainloop()


intercafe()