keer = int(input("Tot hoever wilt in de rij van Fibonacci gaan? "))

a = 0
b = 1

print(a)
print(b)

def fibonacci_rij_a():

    global a
    a = (int(a) + int(b))


def fibonacci_rij_b():

    global b
    b = (int(b) + int(a))


for c in range (0,keer):

    fibonacci_rij_a()

    print(a)

    fibonacci_rij_b()

    print(b)