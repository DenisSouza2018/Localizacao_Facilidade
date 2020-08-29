# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def getInstancias(name,id):

    # Diretorio Denis
    directory = 'C:/Users/denis/OneDrive/Documentos/Localizacao_e_facilidade/instancias/'+ name + id + '.txt'

    with open(directory, 'rb') as item:
        nrows, ncols = [int(field) for field in item.readline().split()]
        data = np.genfromtxt(item, dtype ="int32", max_rows = nrows)
    return  data


dado = getInstancias("cap","51")


print(dado)