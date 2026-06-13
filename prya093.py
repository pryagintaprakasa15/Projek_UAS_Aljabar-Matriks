# Modul Matriks Sederhana

def tambah_matriks(A, B):
    hasil = []

    for i in range(2):
        baris = []
        for j in range(2):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)

    return hasil


def transpose_matriks(A):
    hasil = []

    for i in range(2):
        baris = []
        for j in range(2):
            baris.append(A[j][i])
        hasil.append(baris)

    return hasil