# Pendaftaran Kursus Online

## Input Usia dan Kelulusan Ujian Kualifikasi
Usia = int(input(" Berapa Usia Kamu ? "))
Kelulusan = input("Apakah Anda Sudah Lulus Ujian Kualifikasi (Y/T) ? ")

## Pengelompokkan Kebutuhan Usia dan Kelulusan Ujian Kualifikasi
Kebutuhan_Usia = (Usia >= 21)
Kebutuhan_Kelulusan = (Kelulusan == "Y")

# Output
if Kebutuhan_Usia and Kebutuhan_Kelulusan :
    print("Anda Dapat Mendaftar Kursus")
else: print("Anda Tidak Dapat Mendaftar Kursus")
