def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"Chapter_9/tables/table_{n}.txt", "w") as f:
        f.write(table)




for n in range(2, 21):
    generateTable(n)