# Berat Maksimal Bagasi
berat_maksimal = 22     # 50 lbs = 22 kg

# Input Berat Bagasi A
A = int(input("Masukkan Berat Bagasi A (kg) = "))  #Untuk Berat Bagasi 49 kg
Hasil = (A > berat_maksimal)
print("Bagasi dengan Berat", A, "adalah", not Hasil)

# Input Berat Bagasi B
B = int(input("Masukkan Berat Bagasi B (kg) = "))  #Untuk Berat Bagasi 110 kg
Hasil = (B > berat_maksimal)
print("Bagasi dengan Berat", B, "adalah", not Hasil)