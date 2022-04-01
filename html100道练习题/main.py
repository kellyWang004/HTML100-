import os
for i in range(110,120):
    with open(f"{i}.html","w",encoding="UTF-8") as file:
        with open("109.html","r",encoding="UTF-8") as file2:
            file.write(file2.read())