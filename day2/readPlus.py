with open("sample2.txt",'r+') as f:
    f.write("This is added line.\n")
    print(f.read())

# -------------------------------------------------
with open("sample3.txt",'a+') as f:
    f.write("This is appended line.\n")
    f.seek(0)
    print(f.read())