with open("arquivo4.txt", "w") as file:
    file.writelines(["Marcos 10\n", "Felipe 4\n",
                    "José 6\n", "Ana 10\n", "Maria 9 \n", "Miguel 5 \n"])

lista_reprovador = []

with open("arquivo4.txt", "r") as file:
    for name_and_score in file:
        if int(name_and_score.split(" ")[1]) < 6:
            lista_reprovador.append(name_and_score)

    with open("arquivo5.txt", "w") as reprovados:
        reprovados.writelines(lista_reprovador)

leitura_de_reprovados = open("arquivo5.txt", "r")
print(leitura_de_reprovados.read())

leitura_de_reprovados.close()
