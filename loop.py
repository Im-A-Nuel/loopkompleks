def pagar_vertikal(n):
    print('Pagar Vertikal')
    for i in range(1,n+1):
        print('#')
    print()
        
def pagar_horizon(n):
    print('Pagar Horizontal')
    for i in range(1,n+1):
        print('#',' ', end='')
    print()


def pagar_bertingkat(n):
    print('Pagar bertingkat')
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('#',' ', end='')
        print()

def persegi(n):
    print('Persegi')
    for baris in range(n):
        for kolom in range(n):
            print('#', end='')
        print()
    print()

def persegi_bolong(n):
    print('persegi bolong')
    for baris in range(1,n+1):
        if baris==1 or baris== n:
            for kolom in range(n):
                print('#', end='')
        else:
            spasi=n-2
            print('#', end='')
            for i in range(spasi):
                print(' ', end='')
            print('#', end='')
        print()
    print()
    
def huruf_x(n):
    print('huruf x')
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris == kolom:
                print('#', end='')
            elif baris+kolom==n+1:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()

def huruf_z(n):
    print('huruf z')
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris==1 or baris== n:
                print('#', end='')
            elif baris+kolom==n+1:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()

def huruf_n(n):
    print('huruf n')
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if kolom==1 or kolom== n:
                print('#', end='')
            elif baris==kolom:
                print('#', end='')
            else:
                print(' ', end='')
        print() #ganti baris
    print() #jarak ke output berikutnya(opsional)

def simbol_plus(n):
    print('simbol plus')
    tengah=(n//2)+1
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris==tengah or kolom==tengah:
                print('#', end='')         
            else:
                print(' ', end='')
        print() #ganti baris
    print() #jarak ke output berikutnya(opsional)


def segitiga_kiri(n):
    print('segitiga kiri')
    for baris in range(1,n+1):
        for kolom in range(1,baris+1):
            print('#', end='')
        print()
    print()

def segitiga_kanan(n):
    print('segitiga kanan')
    for baris in range(1,n+1):
        #hitung berapa pagar yang harus muncul
        pagar=baris
        #hitung berapa spasi yang harus muncul
        spasi=n-pagar
        #print spasi
        for kolom in range(spasi):
            print(' ', end='')
        #print pagar
        for kolom in range(pagar):
            print('#', end='')
        print()#ganti baris
    print()#opsional

def segitiga_tengah(n):
    print('segitiga tenagh')
    for baris in range(1,n+1):
        spasi=n-baris
        pagar=2*baris-1
        #print spasi
        for spasi in range(spasi):
            print(' ', end='')
        #print pagar
        for pagar in range(pagar):
            print('#', end='')
        print()#ganti baris
    print()#opsional

def zig_zag(n):
    print('zig zag')
    spasi=n-1
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris%2==1:
                #print pagar baris full
                print('#', end='')
            elif baris%4==0:
                print('#', end='')
                break
            else:
                if kolom==n :
                    print('#', end='')
                else :
                    print(' ', end='')
            
        print()
    print()
            
        

n=int(input('Masukan n : '))
pagar_vertikal(n)
pagar_horizon(n)
pagar_bertingkat(n)
persegi(n)
persegi_bolong(n)
huruf_x(n)
huruf_z(n)
huruf_n(n)
simbol_plus(n)
segitiga_kiri(n)
segitiga_kanan(n)
segitiga_tengah(n)
zig_zag(n)
