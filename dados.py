import sys
import csv

lista = ['Elisangela', 'F', '940045878', 'angela.elis@gmail.com']


#funcao adcionar
def adcionar_dados(i):
    #acessando  csv
    with open('dados.csv','a+', newline='') as file:
      escrever = csv.writer(file)
      escrever.writerow(i)  
        
    
# função ver dados
def ver_dados():
   dados = []
   # acessando  csv
   with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            dados.append(linha)
        return dados


# funcao remover dados
def remover_dados(i):
    def adcionar_novalista(j):
        # acessando csv
        with open('dados', 'w',newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)  
            ver_dados()


    nova_lista = []
    telefone = i
    with open('dados.csv', 'r') as file:
        ler_csv = csv. reader(file)

        for linha in ler_csv:
             nova_lista.append(linha)
             for campo in linha:
                 if campo == telefone:
                     nova_lista.remove(linha)

    # adcionando nova lista                 
    adcionar_novalista(nova_lista)     



# funcao atualizar dados
def atualizados_dados(i):
    def adcionar_novalista(j):
        # acessando csv
        with open('dados', 'w',newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)  
            ver_dados()


    nova_lista = []
    telefone = i[0]
    with open('dados.csv', 'r') as file:
        ler_csv = csv. reader(file)

        for linha in ler_csv:
             nova_lista.append(linha)
             for campo in linha:
                 if campo == telefone:
                     nome = i[1]
                     sexo = i[2]
                     telefone = i[3]
                     email =i [4]

                     dados = [nome, sexo, telefone, email]

                     # trocando lista por index
                     index = nova_lista.index(linha)
                     nova_lista[index] = dados

    # adcionando nova lista                 
    adcionar_novalista(nova_lista)    


       
# função pesquisar dados
def pesquisar_dados(i):
   dados = []
   telefone = i

   print(i)

   # acessando csv
   with open('dados.csv') as file:
       ler_csv = csv.reader(file)
       for linha in ler_csv:
           for campo in linha:
               if campo == telefone:
                   dados.append(linha)
               
           

print(pesquisar_dados('940023214'))
