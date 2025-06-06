db_livros = {}  

print('=_='*15)
print('BIBLIOTECA')
print('=_='*15)

class Livros:
    def __init__(self, autor, ano_lancamento, titulo, emprestado=False, usuario=None):
        self.autor = autor
        self.ano_lancamento = ano_lancamento
        self.titulo = titulo
        self.emprestado = emprestado
        self.usuario = usuario

def adiciona_livro():
    autor = input('Digite o nome do autor do livro:  ')
    titulo = input('Digite o título do livro: ')
    ano_lancamento = int(input('Digite o ano de publicação:  '))
    
    if titulo in db_livros:
        print('Esse livro já está cadastrado.')
        return

    novo_livro = Livros(autor=autor, ano_lancamento=ano_lancamento, titulo=titulo)
    db_livros[titulo] = novo_livro
    print('Livro adicionado!')

def listar_livro():
    if not db_livros:
        print('No momento não há livros cadastrados.')
    else:
        print('\nLista de livros:')
        for livro in db_livros.values():
            status = f"(Emprestado para {livro.usuario})" if livro.emprestado else "(Disponível)"
            print(f"- {livro.titulo} ({livro.ano_lancamento}) por {livro.autor} {status}")

def pesquisa_livro():
    termo = input('Digite o nome do autor ou do livro que deseja encontrar: ').lower()
    encontrados = []

    for livro in db_livros.values():
        if termo in livro.autor.lower() or termo in livro.titulo.lower():
            encontrados.append(livro)
    
    if encontrados:
        print('Livros encontrados:')
        for livro in encontrados:
            print(f"- {livro.titulo} ({livro.ano_lancamento}) por {livro.autor}")
    else:
        print('Nenhum livro encontrado com esse termo.')

def emprestar_livro():
    titulo = input('Digite o título do livro que deseja emprestar: ')
    livro = db_livros.get(titulo)
    
    if livro:
        if livro.emprestado:
            print(f'O livro já está emprestado para {livro.usuario}.')
        else:
            usuario = input('Digite o nome de quem está pegando o livro: ')
            livro.emprestado = True
            livro.usuario = usuario
            print(f'O livro "{livro.titulo}" foi emprestado para {usuario}.')
    else:
        print('Livro não encontrado.')

def devolver_livro():
    titulo = input('Digite o título do livro que deseja devolver: ')
    livro = db_livros.get(titulo)

    if livro:
        if livro.emprestado:
            print(f'O livro "{livro.titulo}" foi devolvido por {livro.usuario}.')
            livro.emprestado = False
            livro.usuario = None
        else:
            print('Esse livro não está emprestado.')
    else:
        print('Livro não encontrado.')

while True:
    try:
        opcoes = int(input(''' 
        1 - Adicionar Livro
        2 - Listar Livros
        3 - Pesquisar Livro
        4 - Empréstimo de Livro
        5 - Devolução de Livro
        0 - Sair
        --> '''))
    except ValueError:
        print('Digite um número válido.')
        continue

    if opcoes == 1:
        adiciona_livro()
    elif opcoes == 2:
        listar_livro()
    elif opcoes == 3:
        pesquisa_livro()
    elif opcoes == 4:
        emprestar_livro()
    elif opcoes == 5:
        devolver_livro()
    elif opcoes == 0:
        print('Encerrando...')
        break
    else:
        print('Opção inválida.')
