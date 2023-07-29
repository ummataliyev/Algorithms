def find_number(N=100):
    for number in range(1, N):
        answer = input(f"(Did you think {number}? (yes/no)")
        if answer == 'y':
            print("Yutdim!")
            return number


find_number(100)
