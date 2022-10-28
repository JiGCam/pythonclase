# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# integrates
sub_total= 10_000
extra= 1_000
tax= 500
total= (sub_total-tax)+extra
print= total

# snakecase
sour_candy= "sour_patch"
print(sour_candy)

# hard-code
fruit= "orange"
print(fruit)
print(fruit.capitalize())
fruit_uppercase = fruit.upper()
print(fruit_uppercase)
frit_lowercase = fruit_uppercase.lower()
print(fruit_lowercase)

user_name = input("Ponga su nombre: ").capitalize()
user_lastname = input("Ahora ponga sus apellidos: ").title()




def controlar_lista_de_estudiantes():
    students = []
    name1 = "Jorge"
    name2 = "Jose"
    # .append() agregar un objeto
    students.apped(name1)
    students.apped(name2)
    print(students)

    # .pop() quita el ultimo objeto
    students.pop()
    return students


print(controlar_lista_de_esudiantes())









def prender_apagar_luz():
    trigger = True
    if trigger == True:
        print()

    apagador = True
    if apagador == True:
        print("Apague la luz")
        apagador = False
    else:
        print("Prenda la luz")
        apagador = True
    print(f"El apagador tiene: {apagador}")

prender_apagar_luz()