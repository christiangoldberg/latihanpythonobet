#Nama: Christian Goldbetrg
#NIM: 12218086
#PR03 Metnum - Mencari Z Factor
#Korelasi: Dranchuk and Abu-Kassem Method

import math



print("DRANCHUK AND ABU-KASSEM Z FACTOR NO.1")

P = 5000
T = 250

#Menghitung Critical Temperature
gammag = 0.7
Ppc = 756.8 - 131.07*gammag - 3.6*(gammag**2)
Tpc = 169.2 + 349.5*gammag - 74*(gammag**2)
T = T + 459.67 #Rankine


#Tpr dan Ppr
Tr = T/Tpc
Pr = P/Ppc


A1 = 0.3265
A2 = -1.0700
A3 = -0.5339
A4 = 0.01569
A5 = -0.05165
A6 = 0.5475
A7 = -0.7361
A8 = 0.1844
A9 = 0.1056
A10 = 0.6134
A11 = 0.7210

F = True

z = 1.0000
ztotal = z
z = 1+(A1+(A2/Tr)+(A3/Tr**3)+(A4/Tr**4)+(A5/Tr**5))*(0.27*Pr/z*Tr)+(A6+(A7/Tr)+(A8/Tr**2))*((0.27*Pr/z*Tr)**2)-A9*((A7/Tr)+(A8/Tr**2))*((0.27*Pr/z*Tr)**5)+A10*(1+A11*((0.27*Pr/z*Tr)**2))*(((0.27*Pr/z*Tr)**2)/Tr**3)*pow(2.71828,-(A11*((0.27*Pr/z*Tr)**2)))
miu = abs(z - 0)
#ITERASI
while (F == True):
    z1 = 1+(A1+(A2/Tr)+(A3/Tr**3)+(A4/Tr**4)+(A5/Tr**5))*(0.27*Pr/z*Tr)+(A6+(A7/Tr)+(A8/Tr**2))*((0.27*Pr/z*Tr)**2)-A9*((A7/Tr)+(A8/Tr**2))*((0.27*Pr/z*Tr)**5)+A10*(1+A11*((0.27*Pr/z*Tr)**2))*(((0.27*Pr/z*Tr)**2)/Tr**3)*pow(2.71828,-(A11*((0.27*Pr/z*Tr)**2)))
    miu = abs(z1 - z)
    if(miu <= 0.00001):
        ztotal = z1
        F - False
    else:
        z = z1

print("Hasil:",ztotal)