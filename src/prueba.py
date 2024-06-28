def show_list(lista):
    for el in lista:
        print(el, end= "")
    print("\n------------------------")


lista = [1,2,3,4,5,6,7,8]
copia = lista.copy


show_list(lista)



for el in lista:
    if el == 4:
        lista.remove(el)
    print(el, end= " ")
print("\n------------------------")

for i in range(len(lista)):
    if lista[i] == 4:
        list.remove(lista[i])
    print(lista[i],end=" ")


show_list(lista)