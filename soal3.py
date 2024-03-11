#buat fungsi def
def hitungips(jumlahmatkul):
    totalsks = 0
    totalbobot = 0

    for i in range(jumlahmatkul):
        nilai = input(f"Masukkan nilai mata kuliah {i+1} (A/B/C/D): ").upper()
        sks = 3  # Asumsi sks setiap mata kuliah selalu 3

        #gunakan percabangan(modul)
        if nilai == "A":
            bobot = 4
        elif nilai == "B":
            bobot = 3
        elif nilai == "C":
            bobot = 2
        elif nilai == "D":
            bobot = 1
        else:
            print("Nilai tidak valid/error. Masukkan nilai yang benar")
            continue
        totalsks += sks
        totalbobot += sks * bobot
    ips = totalbobot / totalsks
    return ips
# Input dari pengguna
jumlahmatkul = int(input("Masukkan jumlah mata kuliah: "))
# Hitung IPS
hasilitung = hitungips(jumlahmatkul)
# Tampilkan hasil
print(f"Indeks Prestasi Semester anda adalah : {hasilitung:.2f}")


