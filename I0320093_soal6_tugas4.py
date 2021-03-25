# Aplikasi Operator Bitwise
a = 4                       # 4 = 0100
b = 11                      # 11 =1011

# 4 | 11
Hasil = a | b
print('Hasil dari a | b adalah ', Hasil, 'Binary = ', format(Hasil,'07b'))

# 4 >> 11
Hasil = a >> b
print('Hasil dari a >> b adalah ', Hasil, 'Binary = ', format(Hasil,'07b'))

# 4 ^ 11
Hasil = a ^ b
print('Hasil dari a * b adalah ', Hasil, 'Binary = ', format(Hasil,'07b'))

# ~a
Hasil = ~a
print('Hasil dari ~a adalah ', Hasil, 'Binary = ', format(Hasil,'08b'))

# 11 & 4
Hasil = b & a
print('Hasil dari b & a adalah ', Hasil, 'Binary = ', format(Hasil,'07b'))
