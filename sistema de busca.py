
from time import sleep

folha_de_pagamento = {'pedro': 1400.00, 'ronaldo':7000.00, 'marcelo': 7000.00}
nome  = input('digite o nome do funcionário que deseja pesquisar: ')

if nome in folha_de_pagamento:
    print('...')
    sleep(2)
    print('colaborador encontrado')
    print(f'o funcionário {nome} recebe')
    print(folha_de_pagamento[nome])
else:
    print('colaborador nao encontrado no banco de dados.')
