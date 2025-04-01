# criação da classe usuário,adicionando atributos da instãncia:

class Usuario():
    def __init__ (self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.__senha = senha

# encapsulamento aplicado na senha do usuário,só podendo ser acessada dentro da classe,a partir de um método:

    def mostra_senha(self):
        print(self.__senha)

    
# dados do usuário que serão utilizados: 

user = Usuario('gabrielzinho','renanplays20@gmail.com','1234567')
# saída dos dados 
print(f'nome :{user.nome}')
print(f'email:{user.email}')
print('a senha do usuário é :')
user.mostra_senha()
