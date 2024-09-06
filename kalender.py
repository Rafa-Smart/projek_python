print("========================")
print("PROGRAM KALENDER")
print("========================")

import calendar
tahun = int(input("masukan tahun :"))
bulan = int(input("masukan bulan :"))
print()

print("hasil :")
print(calendar.month(tahun,bulan)) 
no = 140 % 16
print(no)