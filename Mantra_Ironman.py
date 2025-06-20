# Mantra del Ironman en Python 17/Jun/2025
# Pulsar F5 para ejecutar el código en IDLE
# Pulsar Ctrl+F5 para ejecutar el código en VSCode
# En macOS, para que funcione F5, pulsar Fn (globo terráqueo) + F5
# $ git add Mantra_Ironman.py
# $ git commit -m "Comentario"
# $ git push

mantra = ["Confío en mí. He entrenado lo mejor que he podido y domino la distancia, por ello nadaré, pedalearé y correré para mí mismo."]
mantra.append("Los demás compiten conmigo, pero no son mis adversarios. Compito para mí.")
mantra.append("El triatlón debo verlo como algo divertido. Alegría y diversión pese a la dificultad, porque tengo el privilegio de deslizarme en el agua, viajar en bici y superar una larga distancia corriendo. Soy un privilegiado por ello.")
mantra.append("No tengo miedo pero las distancias me imponen respeto. Es natural.")

print("\nMantra del Ironman")
n = 1
for item in mantra:
    print(f"{n}: {item}")
    n += 1
print()
