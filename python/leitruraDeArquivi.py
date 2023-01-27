f = open("saida.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("saida.txt", "r")
print(f.read())

