# Form untuk menanyakan Nama, Jenkel dan Alamat rumah.
print "Boleh tahu nama lengkap anda?",
nama = raw_input()
print "Jenis kelamin? L atau P",
jenkel = raw_input()
if jenkel == "L":
    jenkel = "Pria"
elif jenkel == "P":
    jenkel = "Wanita"
else:
    jenkel = "Anda salah memasukkan kode yang diminta!!!"

print "Alamat sesuai KTP?",
alamat = raw_input()

# Tampilkan semua yang didapat
print "Ok, kami sekarang sudah tahu nama anda %s, anda seorang %s dan beralamatkan di %s." % (nama, jenkel, alamat)
