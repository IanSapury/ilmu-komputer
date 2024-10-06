print ("---Kalkulator Sederhana---")
print ("__________________________")
print ("")

angka_1 = int(input("Masukan angka pertama : "))
option = input("pilih opsi (+, -, /, *): ")
angka_2 = int(input("Masukan angka kedua : "))

opsi_plus = angka_1 + angka_2
opsi_min = angka_1 - angka_2
opsi_bagi = angka_1 / angka_2
opsi_kali = angka_1 * angka_2

if option == "+" :
    print ("Hasilnya adalah : " + str(opsi_plus))
elif option == "-" :
    print ("Hasilnya adalah : " + str(opsi_min))
elif option == "/" :
    print ("Hasilnya adalah : " + str(round(opsi_bagi)))
elif option == "*" :
    print ("Hasilnya adalah : " + str(opsi_kali))
