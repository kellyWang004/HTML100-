import os
for i in range(88,101):
    with open(f"0{i}.html","w",encoding="UTF-8") as file:
        with open("087.html","r",encoding="UTF-8") as file2:
            file.write(file2.read())