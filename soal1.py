#membuatfungsi def perkalian()
def perkalian():
    #membuat input penggna
    input1 = int(input("masukkan input angka pertama:"))
    input2 = int(input("masukkan input angka kedua:"))
    
    hasil = 0
    #buat fungsi for untuk proses output program
    for i in range(input1):
        hasil = hasil + input2
        #rumusnya 
    HasilAkhir = (f"{input1} x {input2} = {f'{input2} + ' * (input1-1)}{input2} = {hasil}")
    #return hasil akhir(memanggil fungsi dan print ouput)
    return HasilAkhir
print(perkalian())