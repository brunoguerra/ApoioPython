# Olá Amores

inteira = 1
flutuante = 0.5

class Cadastro:
    def salvar(self):
        """
        Todas as classes que extenderem esta
        devem implementar o metodo dados
        E todas elas devem definir o atributo caminho
        para poder salvar
        """
        arquivo = open(self.caminho, 'a')
        resultado = ''
        for item in self.dados():
            resultado = resultado + ';' + str(item)
        arquivo.write(resultado+'\n')
        arquivo.close()

    def salvar_lista(self, lista, caminho):
        arquivo = open(caminho, 'a')
        resultado = ''
        for item in lista:
            resultado = resultado + str(item)
        
        arquivo.close()


class Cliente(Cadastro):
    def __init__(self):
        self.caminho = "clientes.txt"
    
    def set_cod(self, cod):
        self.codigo = cod

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def set_sexo(self, sexo):
        self.sexo = sexo

    def dados(self):
        return [self.codigo, self.nome, self.idade, self.sexo]


class Categoria(Cadastro):
    def __init__(self):
        self.caminho = "categoria.txt"

    def set_cod(self, cod):
        self.codigo = cod

    def set_nome(self, nome):
        self.nome = nome

    def dados(self):
        return [self.codigo, self.nome]

class Produto(Cadastro):
    def __init__(self):
        self.caminho = "produto.txt"

    def set_cod(self, cod):
        self.codigo = cod

    def set_nome(self, nome):
        self.nome = nome

    def set_embalagem(self, embalagem):
        self.embalagem = embalagem
    
    def set_preco_sugerido(self, preco):
        self.preco_sugerido = preco

    def set_categoria(self, categoria):
        self.categoria = categoria
    def dados(self):
        return [self.codigo, self.nome, self.embalagem, self.preco_sugerido, self.categoria.codigo]
    

cadastro = Cadastro()
cadastro.salvar_lista([11, 'BRUNO', 'M', '35'], 'cadastro-generico.txt')

cliente = Cliente()
cliente.set_cod(11)
cliente.set_nome('Bruno')
cliente.set_idade(35)
cliente.set_sexo('M')
cliente.salvar()


categoria = Categoria()
categoria.set_cod(11)
categoria.set_nome('Cerveja')
categoria.salvar()


produto = Produto()
produto.set_cod(11)
produto.set_nome('Budewiser')
produto.set_embalagem('lata')
produto.set_preco_sugerido(2.5)
produto.set_categoria(categoria)
produto.salvar()













