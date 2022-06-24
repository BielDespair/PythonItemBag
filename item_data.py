class Item:
    def __init__(self,nome,peso):
        self.nome = nome
        self.peso = peso

    def __str__(self):
        return f'{self.nome} Peso: {self.peso}'

lista = {"Espada":Item("Espada",10),
        "Armadura":Item("Armadura",20),
        "Lixo":Item("Lixo",1),
        "Adaga":Item("Adaga",3)}

espada = Item("Espada",10")
armadura = Item ("Armadura",20)
adaga = Item ("Adaga",3)
lixo = Item("Lixo",1)
