# A palavra "class" é usada para criar uma classe.
# Uma classe funciona como um molde para criar objetos
class Carro:

    # Método Construtor
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    # Métodos

    # Método acelerar
    # "aumento" será o valor recebido para aumentar a velocidade.
    def acelerar(self, aumento):
        # self.velocidade = self.velocidade + aumento 
        self.velocidade += aumento

        print(f"O carro acelerou para {self.velocidade} km/h")

    #Metodo frear
    def frear(self, reducao):
        if reducao >= self.velocidade:
            self.velocidade = 0
        else:
            self.velocidade -= reducao

        print(f"O carro freou para {self.velocidade} km/h")

    # Método para exibir informações
    def exibir_info(self):
        print("=== INFORMAÇÕES DO CARRO ===")

        # Exibe os atributos do objeto
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade Atual: {self.velocidade}")
        

# Criando um objeto da Classe Carro

# "carro1" é uma variável que recebe um objeto
carro1 = Carro("Chevrolet", "S10", 2013)

# Chamando os métodos

# O valor 50 será enviado para o parâmetro "aumento"
carro1.acelerar(50)

# O valor 20 será enviado para o parâmetro "redução"
# carro1.frear(reducao)
carro1.frear(20)

# Exibindo as informações do carro
carro1.exibir_info()




# # # "carro2" é uma variável que recebe um objeto
# carro2 = Carro("BYD", "Dolphin Mini", 2025)

# # # Exibir informações do carro 2
# print(f"Marca: {carro2.marca}")
# print(f"Modelo: {carro2.modelo}")
# print(f"Ano: {carro2.ano}")

