# -*- coding: iso-8859-15 -*-

# vogliamo leggere due numeri da tastiera
# e visualizzare il più grande

def max(a,b):
    if a > b:
        return a
    return b

def input_int(message):
    ok = False
    while not ok:
        try:
            x = int(input(message))
            ok = True
        except ValueError:
            print("Non hai inserito un numero")
        except:
            print("Si è verificato un errore")
    return x

# try:
#     x = int(input("Primo numero: "))
# except:
#     print("Non hai inserito un numero")
#     x = 0
    
# try:
#     y = int(input("Secondo numero: "))
# except:
#     print("Non hai inserito un numero")
#     y = 0
x = input_int("Primo numero: ")
y = input_int("Secondo numero: ")
print("Hai digitato", x, "e",y,". Il più grande è:", max(x,y))
