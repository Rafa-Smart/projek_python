import math
print("PROGRAM MENGHITUNG LINGKARAN")
operator = input("pilih(luas,keliling) :")
jari_jari = float(input("masukan nilai jari jari :"))

if jari_jari % 7 == 0 :
    pi = 22/7
else :
    pi = 3.14

if operator == "luas":
    hasil = (jari_jari ** 2) * pi
    print(f"luas lingkaran adalah :", hasil)
elif operator == "keliling":
    hasil = 2 * pi * jari_jari
    print(f"keliling lingkaran adalah :", hasil)
    print("TERIMA KASIH")