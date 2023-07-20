from tkinter import ttk
from tkinter.ttk import *
from tkinter import*
from tkinter import messagebox

from dados import *
# cores -----------------------------

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#38576b"  # preta/black
co4 = "#403d3d"   # letra
co5 = "#FF1493"  # DeepPink
co6 = "#ef5350"   # vermelha
co7 = "#93cd95"   # verde

co1 = co1
co1= co1

# criando janela --------------------

janela = Tk ()
janela.title ("")
janela.geometry('500x450')
janela.configure(background=co3)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

################# Frames ####################

frame_cima = Frame(janela,width=500, height=50,bg=co3, relief="flat")
frame_cima.grid(row=0, column=0,pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=500, height=150,bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela,width=500, height=100,bg=co1, relief="flat")
frame_tabela.grid(row=2, column=0,columnspan=2,padx=10, pady=1, sticky=NW)

# configurando frame cima

l_nome = Label(frame_cima, text="Agenda Telefônica", height=1,anchor=NE, font=('arial 20 bold'), bg=co3, fg=co1)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima,width=500, text="", height=1,anchor=NW, font=('arial 1 '), bg=co1)
l_linha.place(x=0, y=46)

# configurando frame baixo

l_nome = Label(frame_baixo, text="Nome*", anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25,justify="left",relief=FLAT, font=('',10), highlightthickness=1)
e_nome.place(x=80, y=20)

l_sexo = Label(frame_baixo, text="Sexo*", anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_sexo.place(x=10, y=50)
c_sexo = Combobox(frame_baixo, width=27)
c_sexo['values'] = ('', 'F', 'M')
c_sexo.place(x=80, y=50)

l_telefone = Label(frame_baixo, text="Telefone*", anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_telefone.place(x=10, y=80)
e_telefone = Entry(frame_baixo, width=25,justify="left", relief=FLAT, font=('',10), highlightthickness=1)
e_telefone.place(x=80, y=80)

l_email = Label(frame_baixo, text="E-mail*", anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_email.place(x=10, y=110)
e_email = Entry(frame_baixo, width=25,justify="left",relief=FLAT, font=('',10), highlightthickness=1)
e_email.place(x=80, y=110)

l_procurar = Button(frame_baixo, text="Procurar", font=('Ivy 8 bold'), bg=co3, fg=co1, relief=RAISED, overrelief=RIDGE)
l_procurar.place(x=290, y=20)
e_procurar = Entry(frame_baixo, width=16,justify="left",relief=FLAT, font=('',11), highlightthickness=1)
e_procurar.place(x=347, y=21)

b_ver = Button(frame_baixo, text="Ver dados", width=10, font=('Ivy 8 bold'), bg=co3, fg=co1, relief=RAISED, overrelief=RIDGE)
b_ver.place(x=290, y=50)

b_adcicionar = Button(frame_baixo, text="Adcicionar", width=10, font=('Ivy 8 bold'), bg=co3, fg=co1, relief=RAISED, overrelief=RIDGE)
b_adcicionar.place(x=400, y=50)

b_atualizar = Button(frame_baixo, text="Atualizar", width=10, font=('Ivy 8 bold'), bg=co3, fg=co1, relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=400, y=80)

b_deletar = Button(frame_baixo, text="Deletar", width=10, font=('Ivy 8 bold'), bg=co3, fg=co1, relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=400, y=110)


# configurando frame tabela


#creating a treeview with dual scrollbars

 # creating a treeview with dual scrollbars
dados_h = ['Nome', 'Sexo', 'telefone','email']

dados = [['Caique', 'M', '940032587', 'caiquebitt@gmail.com'],
['Camille', 'F', '940023214', 'millevitoria@gmail.com'], 
['Elisangela', 'F', '940045878', 'angela.elis@gmail.com']
]

global tree

tree = ttk.Treeview(frame_tabela, selectmode="extended",columns=dados_h, show="headings")

# vertical scrollbar
vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
# horizontal scrollbar
hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

hd=["nw","nw","nw","nw","nw",]
h=[120,50,80,120,200]
n=0

# tree cabecalho
tree.heading(0,text='Nome', anchor=NW)
tree.heading(1,text='Sexo', anchor=NW)
tree.heading(2,text='Telefone', anchor=NW)
tree.heading(3,text='Email', anchor=NW)

# tree  corpo
tree.column(0, width=120,anchor='nw')
tree.column(1, width=50,anchor='nw')
tree.column(2, width=100,anchor='nw')
tree.column(0, width=120,anchor='nw'[0])


for item in dados:
        tree.insert('', 'end', values=item)




#funcoes--------------------------------------------------------


janela.mainloop()
