def pyramid(p):
    for m in range (0,p):
        for n in range (0,m+1):
            print("* ",end="")
        print("\r")
p = 10
pyramid(p)
