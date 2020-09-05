
def write_file(dados,name_instancia):

    fp = open('Results/' + name_instancia, 'w')

    cont = 0
    for c in dados:
        linha = cont, c.custo, c.demanda
        fp.write(str(linha) + '\n')
        cont += 1
