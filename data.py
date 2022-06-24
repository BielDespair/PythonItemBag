from collections import Counter

class Bag:
    def __init__(self,slots,peso_maximo):  
        self.slots = slots
        self.peso_maximo = peso_maximo
        self.items = self.add_slot_vazio()

    def slots_disponiveis(self):
            x = Counter(obj.nome for obj in self.items)
            slots_vazios = x['vazio']
            return slots_vazios

    def add_slot_vazio(self):
        items = []
        for x in range(0,self.slots):
            x = Vazio()
            items.append(x)
        return items

    def soma_peso(self):
        return sum(obj.peso for obj in self.items)

    def retorna_index_vazio(self):
        index_items = enumerate(self.items)
        achou = False
        while not achou:
            for index,obj in list(index_items):
                if obj.nome == 'vazio':
                    achou = True
                    return index

class Vazio:
    def __init__(self):
        self.peso = 0
        self.nome = 'vazio'

    def __str__(self):
         return 'vazio'
