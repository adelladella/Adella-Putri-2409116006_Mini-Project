# Praktikum Mini Project NIM Genap
# Membuat percabangan untuk menentukan apakah total harga barang

print('Nama : Adella Putri')
print('NIM : 2409116006')
print('Kelas : A Sitem Informasi 2024')

print ('\n-----------------------------------------------------------------------------------')
print ('-------Selamat datang di Kalkulator Perhitungsn DIskon Secara Otomatis Adella------')
print ('-----------------------------------------------------------------------------------')

# Login Pengguna
while True:
    username = input("\nSilakan masukkan username anda : ")
    Nim = int(input("Silakan masukkan NIM anda : "))
    
    if username == 'Adella Putri' and Nim == 2409116006:
        print ("\n" "============Login Anda Telah Berhasil============")
        break
    else:
        print ("\nNim salah Anda tidak berhasil Login")

    
    
while True:
    # Input harga barang dan jumlah pembelian dari pengguna
    harga_per_barang = int(input("\nSilahkan Masukkan Harga Barang per Satuan dalam Rupiah: "))
    jumlah_barang_yang_akan_di_beli = int(input("\n" "Silahkan Masukkan Jumlah Barang yang Akan Dibeli: "))

    # Hitung total dari harga
    total_harga = harga_per_barang * jumlah_barang_yang_akan_di_beli

    # Percabangan untuk mengecek jika total lebih dari Rp 250.000
    if total_harga > 250000:
        print(f"\nTotal harga adalah Rp {total_harga}. Anda mendapatkan diskon 25%.")
        total_harga_diskon = total_harga * 75/100  
        print(f"Total diskon adalah Rp {total_harga_diskon}")
        print(f"Total harga {total_harga}")
        print(f"\nTotal harga setelah diskon adalah Rp {total_harga_diskon}")
    else:
        print(f"Total harga adalah Rp {total_harga}. Tidak ada diskon.")

    # Menanyakan apakah ingin mengulangi program atau tidak
    lanjut = input("\nApakah ingin melakukan pembelian lagi? (ya/tidak): ").lower()
    if lanjut != 'ya':
        break
