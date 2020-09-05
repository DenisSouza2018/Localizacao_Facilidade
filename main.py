# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from Funcao_Escrita.write import write_file


class dado:
    def __init__(self, demanda, custo):
        self.demanda = demanda
        self.custo = custo

class Cliente():
    demanda = 0
    custos = []


def getInstancias(name,id):

    # Diretorio Denis
    directory = 'C:/Users/denis/OneDrive/Documentos/Localizacao_Facilidade/instancias/'+ name + id + '.txt'

    # Variavies
    cliente = Cliente()
    vet_clientes = []
    aux = []
    results = []

    with open(directory, 'rb') as item:
        #Processo para remover o matriz inicial
        n_deposito, n_cliente = [int(field) for field in item.readline().split() ]
        data = np.genfromtxt(item, dtype ="int32", max_rows = n_deposito)

        #Estrutura responsavel por percorrer todo o arquivo
        for x in item.readlines():

            #Condição inicia para pegar a demanda de um cliente
            if len(x.split()) == 1:
                cliente.demanda = float(x)
                cliente.custos = []
                aux = []

            else:
                vet_custo = [float(field) for field in x.split()]
                cliente.custos = vet_custo

            # Condição responsavel por filtrar duplicatas
            if len(cliente.custos) != 0:
                aux += cliente.custos
                if len(aux) == n_deposito:
                    vet_clientes.append(aux)
                    results.append(dado(cliente.demanda,aux))



    return  results

def imprimir(dados):
    # Estrutura responsavel por imprimir dicionario
    cont = 0
    for c in dados:
        print(cont, ':',len(c.custo), c.custo, ',',c.demanda)
        cont += 1

    print('-------------------------')
    print(' ')

dados = getInstancias("cap","41")
imprimir(dados)

dados = getInstancias("cap","42")
imprimir(dados)

dados = getInstancias("cap","43")
imprimir(dados)

dados = getInstancias("cap","44")
imprimir(dados)

dados = getInstancias("cap","51")
imprimir(dados)

dados = getInstancias("cap","81")
imprimir(dados)

dados = getInstancias("cap","82")
imprimir(dados)

dados = getInstancias("cap","83")
imprimir(dados)

dados = getInstancias("cap","84")
imprimir(dados)

dados = getInstancias("cap","131")
imprimir(dados)

dados = getInstancias("cap","132")
imprimir(dados)

dados = getInstancias("cap","133")
imprimir(dados)

dados = getInstancias("cap","134")
imprimir(dados)

## Função responsavel por gravar o resultado em um arquivo
#write_file(dados,'instancia_2')
