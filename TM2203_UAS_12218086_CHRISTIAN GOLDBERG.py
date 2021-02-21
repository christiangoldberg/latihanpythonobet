#Nama: Christian Goldberg
#NIM: 12218086
#SOAL NO. 5 UAS METODE NUMERIK  TM2203
import math

print("Jawaban soal UAS No. 5")
#KAMUS
#DIKETAHUI:
g = 9.81 #Percepatan Gravitasi
A = 3.14*0.015*0.015 #Luas lubang
C = 0.55 #Koefisien
Hi = 2.75 #Kedalaman awal air
Hf = 0 #Kedalaman akhir
r = 1.5 #Jarijari tangki
Vi = (3.14/3)*Hi*Hi*((3*r)-Hi)
Vf = 0
Qi = 0.0028556891

print("Pilih salah satu:")
print("1. Metode Euler")
print("2. Metode Runge-Kutta")

Metode = int(input())
if (Metode == 1):
    deltat = (Vi - Vf)/Qi
    print("Lama waktu yang diperlukan dari kedalaman air 2.75 m hingga isi tangki habis adalah:")
    print(deltat)
elif (Metode == 2):
    #Setelah diubah menjadi bentuk dt/dH didapatkan sebuah konstanta (Detail terlampir pada jawaban manual)
    #RK Orde-3
    kons = 0.000548144056
    H = 0.0000000000
    t = 0.0000000000
    h = 0.916666667 #ditentukan sendiri
    m = 1
    takhir = 0
    ttotal = 0
    while (m <= 3): #3 Kali Langkah sesuai rumus n = (y1-y0)/h
        if (H == 0):
            k1 = 0
        else:
            k1 = h*((3*H)-(H**2))/((math.sqrt(H))*kons)
        Hk2 = H + (h/2)
        k2 = h*((3*Hk2)-(Hk2**2))/((math.sqrt(Hk2))*kons)
        Hk3 = H + h
        k3 = h*((3*Hk3)-(Hk3**2))/((math.sqrt(Hk3))*kons)
        takhir = float(t + ((k1 + (4*k2) + k3)/6))
        H = H + h
        t = ((3*H)-(H**2))/((math.sqrt(H))*kons)
        m = m + 1
    print("Lama waktu yang diperlukan dari kedalaman air 2.75 m hingga isi tangki habis adalah:")
    print(takhir)
else :
    print("Masukkan salah")