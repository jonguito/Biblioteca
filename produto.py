# criação da classe Produto, já aplicando taxa como atributo da classe:
class Produto():
    taxa = 1.50

    # criação dos parâmetros e do valor do produto com a taxa:
    def __init__ (self,nome,descricao,valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.taxa)

# saída dos dados
produto1 = Produto('ps4','videogame console',2399.00 )
produto2 = Produto('Xbox Series X','videogame console', 2000.00 )

# utilizando .valor,del e __dict__ para testar funcionalidades da manipulação dasaída dos dados:
print(produto1.valor )       
del(produto1.valor)
print(produto1.__dict__)
