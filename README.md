# PythonItemBag
Uma mochila de itens em Python, permite guardar e remover itens. A mochila possui slots e peso, que se excedidos impossibilita o armazenamento de mais itens.

Para criar Itens, adicione a lista em item_data.
Crie um Objeto Bag com propriedades de slots e peso em main.

Execute executar.bat

Use nomeObjectBag.guardar_item(item) para guardar.
Use nomeObjectBag.remover_item(index) para removêlo.
Use nomeObjectBag.representacao() Para visualizar a bag.

<hr> 


Exemplo com items e bag já existentes:

mochila.guardar_item(lista["Espada"]) 
mochila.guardar_item(lista["Adaga"])  
mochila.guardar_item(lista["Armadura"])

Guarda os itens em um slot disponivel.

<hr>

mochila.remover_item(1)

Remove o item do slot informado.

<hr>

mochila.representacao()

Mostra o conteudo da bag.
