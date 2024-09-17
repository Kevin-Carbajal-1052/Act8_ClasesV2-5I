class Informacion:
    #listas
    def mi_lista(self):
        lista_nomperro=["Uziel","Carlos","Emi"]
        for x in lista_nomperro:
            print(x)

    #Tuplas
    def mi_tupla(self):
        tupla_Razas=("Chihuahua","Pug","David")
        for x in tupla_Razas:
            print(x)
    
    #Conjuntos
    def miconjunto(self):
        conj_colores=["Rojo","Blanco","Negro"]
        for x in conj_colores:
            print(x)

    #Diccionario
    def midiccionario(self):
        print("Edades")
        dic_edad={
            "Uziel:" : "5",
            "Carlos:" : "7",
            "Emi:" : "1"
        }
        for x,y in dic_edad.items():
            print(x,y)

#Creando el objeto
datos=Informacion()
print("--Listado de nombre de perros--")
datos.mi_lista()
print("--Tupla de razas de perros--")
datos.mi_tupla()
print("--Conjuntos de colores--")
datos.miconjunto()
print("--Diccionario--")
datos.midiccionario()