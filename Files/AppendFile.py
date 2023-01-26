x = ["le", "khanh", "hai", "dang"]
file = open("text", "a")

for item in x:
    file.write(item + "\n")

file.close()


file = open("test.txt", "x")