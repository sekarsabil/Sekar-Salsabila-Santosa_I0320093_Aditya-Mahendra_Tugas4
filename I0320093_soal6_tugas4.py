# Aplikasi Operator Bitwise
a = 4
b = 11

# 4 | 11
Hasil = a | b
print('Hasil dari a | b adalah ', Hasil, 'Binary = ', format(Hasil,'08b'))

# 4 >> 11
Hasil = a >> b
print('Hasil dari a >> b adalah ', Hasil, 'Binary = ', format(Hasil,'08b'))

# 4 ^ 11
Hasil = a ^ b
print('Hasil dari a * b adalah ', Hasil, 'Binary = ', format(Hasil,'08b'))

# ~a
Hasil = ~a
print('Hasil dari ~a adalah ', Hasil, 'Binary = ', format(Hasil,'08b'))

# 11 & 4
Hasil = b & a
print('Hasil dari b & a adalah ', Hasil, 'Binary = ', format(Hasil,'08b'))
