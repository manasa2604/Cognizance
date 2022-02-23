for i in range(5):
    for p in range(0, 5-i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()