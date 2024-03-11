#membuat fungsi def ganjil
def ganjil(bawah, atas):
    #membuat fungsi for jika atas lebih gede dari bwh
    if bawah < atas:
        # fungsi for untuk deret input dri bil terkecil ke terbesar
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                print(i, end=" ")
                
    #kondisi selain diatas
    else:
        #  fungsi for untuk deret input dri bil terbesar ke terkecil
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                print(i, end=" ")
                
# Input untuk pengguja
bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
#outpu
print("deret bilangan ganjil nya:")
ganjil(bawah, atas)

