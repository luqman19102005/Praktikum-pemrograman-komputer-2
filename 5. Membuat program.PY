#Buatlah program untuk menampilkan jumlah hari, jam, menit dan detik dari
#masukan berupa lamanya waktu dalam detik.

N = int(input("msaukkan jumlah detik: "))
A = (60 * 60 * 24)
HARI = N // A
B = A * HARI
C = N - B
JAM = C // (60 * 60)
D = JAM * (60 * 60)
E = C - D
MENIT = E // 60
DETIK = N % 60

print("dengan memasukkan", N, "detik akan menghasilkan luaran" ,HARI, "hari", JAM, "jam", MENIT, "menit", DETIK, "detik")

