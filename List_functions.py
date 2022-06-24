from List_data import Bag,Vazio

class Operador(Bag):
    def __init__(self,slots,peso_maximo):
        super().__init__(slots,peso_maximo)


    def guardar_item(self,item):
        slotfree = self.slots_disponiveis() > 0
        weightfree = (self.soma_peso() + item.peso) <= self.peso_maximo
        if slotfree and weightfree:
            index_vazio = self.retorna_index_vazio()
            self.items[index_vazio] = item

        elif(not slotfree):
            print("SEM ESPAÇO")

        else:
            print("Excedendo Peso Máximo")

    def remover_item(self,index):
        if self.items[index-1].nome == "vazio":
            print("Ja é nulo")
        else:
            self.items[index-1] = Vazio()
            
    def representação(self):
        print(f"Peso: {self.soma_peso()}\nSlots: {self.slots_disponiveis()}\n")
        for index,item in enumerate(self.items):
            print(f'slot: {index+1}|{item}')