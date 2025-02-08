with open("Chapter_9/old.txt") as f:
    content = f.read()

with open("Chapter_9/new.txt","w" ) as f:
    f.write(content)
