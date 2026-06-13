import prya093

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print("Penjumlahan Matriks")
hasil = prya093.tambah_matriks(A, B)

for i in hasil:
    print(i)

print("Transpose Matriks A")
transpose = prya093.transpose_matriks(A)

for i in transpose:
    print(i)