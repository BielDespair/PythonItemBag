#insert para deixar um slot vazio na representação
#representação de slots (como no jogo da forca talvez?)
#classe item com peso,ocupações de slot,nome
#classe bag com slots,capacidade de peso,etc (lista?)
#def soma na classe item (para decidir a soma para comparação)
# "x" for lenght of slots da bag 
#slots = 4 dividir a classe em 4 partes para ocupar 4 slots

from List_functions import Operador
from Items import lista



sacola = Operador(10,60)

guardar = sacola.guardar_item
sacola.guardar_item(lista["Espada"])

sacola.representação()
guardar = sacola.guardar_item
remover = sacola.remover_item







