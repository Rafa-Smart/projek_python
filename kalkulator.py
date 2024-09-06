print(20*"=")
print("KALKULATOR SEDERHANA")
print(20*"=")

angka_1 = float(input("masukan angka 1 : "))
operator = input("pilih (+,-,x,/,%,pangkat) :")
angka_2 = float(input("masukan angka 2 :"))

if operator == "+":
        hasil = angka_1 + angka_2
        print(f"hasilnya adalah : {hasil}")
elif operator == "-":
        hasil = angka_1 - angka_2
        print(f"hasilnya adalah : {hasil}")
elif operator == "x":
        hasil = angka_1 * angka_2
        print(f"hasilnya adalah : {hasil}")
elif operator == "/":
        hasil = angka_1 / angka_2
        print(f"hasilnya adalah : {hasil}")
elif operator == "**":
        hasil = angka_1 ** angka_2
        print(f"hasilnya adalah : {hasil}")
elif operator == "%":
        hasil = angka_1 % angka_2
        print(f"hasilnya adalah : {hasil}")  
elif operator == "pangkat":
        hasil = angka_1 ** angka_2
        print(f"hasilnya adalah : {hasil}")  
        # f ini untuk meminta data dari hasil
        # dan f ini adalah format untuk menggabungkan
        # string("") dan angka      

print("TERIMA KASIH")