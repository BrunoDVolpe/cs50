#List loop
gro_dict = {}
while True:
  try:
    item = input().upper().strip()
  except EOFError:
    break
  else:
    try:
#      if gro_dict[item] > 0: (também dá assim, mas podemos fazer direto)
      gro_dict.update({item:gro_dict[item]+1})
    except KeyError:
      gro_dict.update({item:1})

keys = list(gro_dict)
keys.sort()

for itens in keys:
  print(gro_dict[itens], itens)

"""
#Outro jeito de resolver
#Pegando a lista
gro_list = []
while True:
  try:
    item = input().upper().strip()
    gro_list.append(item)
  except EOFError:
    gro_list.sort()
    break

#Tratando e exibindo a lista através do dicionário
dict_gro_list = {}
for item in gro_list:
  dict_gro_list.update({item:gro_list.count(item)})

for itens in list(dict_gro_list):
  print(dict_gro_list[itens], itens)
  """