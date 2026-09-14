def heart_pattern(n, c=" ", d="*"):
    # Upper part
    for i in range(n//2, n, 2):
        # Left spacing
        for j in range(1, n-i, 2):
            print(c, end="")
        # Left half
        for j in range(i):
            print(d, end="")
        # Middle spacing
        for j in range(1, n-i+1):
            print(c, end="")
        # Right half
        for j in range(i):
            print(d, end="")
        print()

    # Lower part
    for i in range(n, 0, -1):
        # Left spacing
        for j in range(n-i):
            print(c, end="")
        # Stars
        for j in range(2*i-1):
            print(d, end="")
        print()

heart_pattern(19)