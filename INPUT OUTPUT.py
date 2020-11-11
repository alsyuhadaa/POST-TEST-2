# DESKRIPSI BENDA
print("DESKRIPSI SEPATU")
sepatu=[]

# STRING
merk = input("merk sepatu: ")
print("merk sepatu adalah:",merk)
print("-bertype: ",type(merk))
sepatu.append(merk)

# INTEGER
ukuran = int(input("ukuran sepatu: "))
print("ukuran sepatu adalah:",ukuran)
print("-bertype: ",type(ukuran))
sepatu.append(ukuran)

# FLOAT
harga = float(input("harga sepatu: "))
print("harga sepatu adalah:",harga)
print("-bertype: ",type(harga))
sepatu.append(harga)

# STRING
warna = input("warna sepatu: ")
print("warna sepatu adalah:",warna)
print("-bertype: ",type(warna))
sepatu.append(warna)

#INTEGER
jumlah = int(input("jumlah sepatu yang di miliki: "))
print("jumlah sepatu adalah:",jumlah)
print("-bertype: ",type(jumlah))
sepatu.append(jumlah)

print("Merk sepatu adalah",merk, "dengan ukuran",ukuran, "dengan harga",harga, "berwarna",warna, "dan jumlah yang dimiliki",jumlah,)

print(sepatu)