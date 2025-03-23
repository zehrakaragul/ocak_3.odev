def yazdir_1_100():
    # 1'den 100'e kadar olan sayıları yazdırma (for döngüsü kullanılarak)
    print("1'den 100'e kadar olan sayılar:")
    for i in range(1, 101):
        print(i)

def yazdir_cift_sayilar():
    # 1'den 100'e kadar sadece çift sayıları yazdırma (for döngüsü kullanılarak)
    print("\n1'den 100'e kadar olan çift sayılar:")
    for i in range(2, 101, 2):
        print(i)

def faktoriyel():
    # Kullanıcıdan alınan sayının faktöriyelini hesaplama
    sayi = int(input("\nBir sayı girin (faktöriyel hesaplanacak): "))
    fakt = 1
    for i in range(1, sayi + 1):
        fakt *= i
    print(f"{sayi}! = {fakt}")

def asal_sayilar():
    # 1'den 100'e kadar olan asal sayıları bulma (for döngüsü kullanılarak)
    print("\n1'den 100'e kadar olan asal sayılar:")
    for num in range(2, 101):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# Ana program
def main():
    yazdir_1_100()             # 1'den 100'e kadar sayılar
    yazdir_cift_sayilar()      # Çift sayılar
    faktoriyel()               # Faktöriyel hesaplama
    asal_sayilar()             # Asal sayılar

# Programı çalıştırma
main()
