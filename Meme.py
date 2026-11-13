meme_dict = {"LOL": "Una respuesta a algo gracioso","CRINGE": "Algo raro o embarazoso","ROFL": "Una respuesta a una broma","SHEESH": "Ligera desaprobación","CREEPY": "Aterrador o siniestro", "AGGRO": "Ponerse agresivo o enojado"}

print("¡Bienvenido al diccionario!")
print("Escribe 5 palabras en MAYÚSCULAS.")

for i in range(5):
    word = input("Escribe una palabra: ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Esa palabra no está en el diccionario.")

print("¡Gracias por usar el diccionario!")
