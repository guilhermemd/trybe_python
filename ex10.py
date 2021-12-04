file_txt = open("arquivo.txt", mode="w")
# must have exactly one of c = create/r = read/ w = write/a = append mode

file_txt.write("nome idade\n")
file_txt.write("Maria 45\n")
file_txt.write("Miguel 33\n")

print("Túlio 22", file=file_txt)

LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
file_txt.writelines(LINES)

file_txt.close()
