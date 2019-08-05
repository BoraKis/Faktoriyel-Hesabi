faktoriyel=1
while True:
    sayi=int(input("Lütfen herhangi bir sayı giriniz="))
    if(sayi>= 0):
        for i in range(1,sayi + 1):
            faktoriyel = faktoriyel * i

        print("Faktoriyel", faktoriyel)
    elif(sayi<0):
        for i in range(-1,sayi,-1):
            faktoriyel=faktoriyel*i

        print("Faktoriyel",faktoriyel)
        break
