
import matplotlib.pyplot as plt
import pandas as pd

#Rumus Analitik untuk waktu dari 0 hingga t tertentu
def vanalitik(c, t, plotA):
    m = 68.1
    g = 9.81
    e = 2.71828
    for i in range (0,t+1,2):
        va = ((g*m)/c)*(1-(pow(e,(-(c/m)*i))))
        plotA.append(va)
    return plotA

#Rumus Analitik untuk waktu dari 0 hingga t tertentu
def vnumerik(c, t, plotN):
    m = 68.1
    g = 9.81
    vn = 0
    plotN.append(vn)
    for i in range(0,t-1,2):
        vn = vn + (g-(c/m)*vn)*((i+2)-i)
        plotN.append(vn)
    return plotN

#input Waktu
t = int(input("Waktu maksimal untuk plot kecepatan: "))
plotwaktu = []
for i in range (0,t+1,2):
    plotwaktu.append(i)

#Nilai c yang ditentukan
c1 = 10
c2 = 12.5
c3 = 15

#V Analitik
#1. Untuk c = 10
plotA1 = []
plotA1 = vanalitik(c1, t,plotA1)
dataA1 = {"t (s)": plotwaktu,
        "v (m/s)": plotA1}
dfA1 = pd.DataFrame(data=dataA1)
print(dfA1)

#2. Untuk c = 12.5
plotA2 = []
plotA2 = vanalitik(c2, t,plotA2)
dataA2 = {"t (s)": plotwaktu,
        "v (m/s)": plotA2}
dfA2 = pd.DataFrame(data=dataA2)
print(dfA2)

#3. Untuk c = 15
plotA3 = []
plotA3 = vanalitik(c3, t,plotA3)
dataA3 = {"t (s)": plotwaktu,
        "v (m/s)": plotA3}
dfA3 = pd.DataFrame(data=dataA3)
print(dfA3)

#V Numerik
#4. Untuk c = 10
plotA4 = []
plotA4 = vnumerik(c1, t,plotA4)
dataA4 = {"t (s)": plotwaktu,
        "v (m/s)": plotA4}
dfA4 = pd.DataFrame(data=dataA4)
print(dfA4)

#5. Untuk c = 12.5
plotA5 = []
plotA5 = vnumerik(c2, t,plotA5)
dataA5 = {"t (s)": plotwaktu,
        "v (m/s)": plotA5}
dfA5 = pd.DataFrame(data=dataA5)
print(dfA5)

#6. Untuk c = 15
plotA6 = []
plotA6 = vnumerik(c3, t,plotA6)
dataA6 = {"t (s)": plotwaktu,
        "v (m/s)": plotA5}
dfA6 = pd.DataFrame(data=dataA6)
print(dfA6)

#Pembuatan Plot Grafik
#Analitik
dataanalitik = {"t(s)": plotwaktu, "v = 10 m/s": plotA1, "v = 12.5 m/s": plotA2, "v = 15 m/s": plotA3}
dfanalitik = pd.DataFrame(data=dataanalitik)
dfanalitik.plot(kind="line",x="t(s)", y=["v = 10 m/s","v = 12.5 m/s","v = 15 m/s"])

#Numerik
datanumerik = {"t(s)": plotwaktu, "v = 10 m/s": plotA4, "v = 12.5 m/s": plotA5, "v = 15 m/s": plotA6}
dfnumerik = pd.DataFrame(data=datanumerik)
dfnumerik.plot(kind="line",x="t(s)", y=["v = 10 m/s","v = 12.5 m/s","v = 15 m/s"])
plt.show()