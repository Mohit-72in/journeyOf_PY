data = True
word = "python"
line = 1
with open("practice.txt",'r') as f:
    while data:
        data = f.readline()
        if(word in data):
            print(f"'{word}' found at line {line}")
            break
        line += 1