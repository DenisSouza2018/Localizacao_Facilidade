import time
import sys

from Localizacao_Facilidade.In_Out.read import read_inst as le
from Localizacao_Facilidade.In_Out.write import write_file as escreve

t_inicio = time.time()

def main(inst):
    path = 'c:/Meta/Localizacao_Facilidade/Instancias/' + inst
    dados = le(path)
    print(dados)

    escreve(dados, inst)

if __name__ == '__main__':
    main(str(sys.argv[1]))

t_total = time.time() - t_inicio
print('{:.4f}s'.format(t_total))
