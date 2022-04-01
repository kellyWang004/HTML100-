import os
for i in range(130,140):
    with open(f"{i}.html","w",encoding="UTF-8") as file:
        with open("129.html","r",encoding="UTF-8") as file2:
            file.write(file2.read())