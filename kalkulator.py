#!/usr/bin/python3
print("Witaj w kalkulatorze")

def dzialanie():
    liczba = int(input("Podaj liczbe: "))
    return liczba

def dodawanie(baza):
    return baza + dzialanie()
def odejmowanie(baza):
    return baza - dzialanie()
def mnozenie(baza):
    return baza * dzialanie()
def dzielenie(baza):
    dzielnik = dzialanie()
    if dzielnik > 0:
        return baza / dzielnik
    else:
        print("Nie mozna tak dzielic")
        return baza

baza = int(input("Podaj liczbe: "))
operacja = input("Podaj operację[+, -, *, /] lub wpisz 'exit' aby wyjść: ")

while True:
    if operacja == "exit":
        break
    else:
        if operacja == "+":
            baza = dodawanie(baza)
        elif operacja == "-":
            baza = odejmowanie(baza)
        elif operacja == "*":
            baza = mnozenie(baza)
        elif operacja == "/":
            baza = dzielenie(baza)
    print(f"{baza}")
    operacja = input("Podaj operację[+, -, *, /] lub wpisz 'exit' aby wyjść: ")


print(f"Wynik działania to: {baza}")
