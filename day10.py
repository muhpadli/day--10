print("Belajar tipe data set")
kota = { "majene", "mamuju", "mamasa", "polman", "pasangkayu"}
print(kota)
print(type(kota))

print()
#menambahkan nilai data set
kota.add("mateng")
print(kota)
kota.update({"makassar","palu"})
print(kota)

print()
#menghapus nilai data set
kota.remove("palu")
print(kota)

print()
#operasi gabungan pada data set
negara = {"Indonesia", "Singapura"}
kota_negara = kota | negara
print(kota_negara)
alat_dapur = {"panci", "wajan", "kompor", "termos"}
alat_makan = {"piring", "sendok", "garpu"}
alat = alat_dapur.union(alat_makan)
print(alat)

print()
#operasi irisan data set
nilai1 = {2,4,6,7,8}
nilai2 = {3,4,5,6,7,8}
print(nilai1 & nilai2)
nilai3 = nilai1.intersection(nilai2)
print(nilai3)

print()
#operasi selisih data set
data_a = {3,5,7,8}
data_b = {5,7,9,11}
print(data_a - data_b)
data_c = data_a.difference(data_b)
print(data_c)

print()
#operasi data komplement
nilai_a = {4,3,5,7}
nilai_b = {3,6,5,9}
print(nilai_a  ^ nilai_b)
nilai_c = nilai_a.symmetric_difference(nilai_b)
print(nilai_c)


