while(True):
    namaA = input('Masukkan nama : ')
    if namaA == 'STOP':
        break
    kursiA = int(input(f'Masukkan nomor kursi {namaA} : '))
    namaB = input('Masukkan nama : ')
    kursiB = int(input(f'Masukkan nomor kursi {namaB} : '))
    namaC = input('Masukkan nama : ')
    kursiC = int(input(f'Masukkan nomor kursi {namaC} : '))
    if kursiC == kursiB:
        print('Mohon maaf kursi tersebut telah terisi!')
        namaD = input('Masukkan nama : ')
        kursiD = int(input(f'Masukkan nomor kursi {namaD} : '))
        namaE = input('Masukkan nama : ')
        if namaE =='STOP':
            print(" ")
            print('List kursi yang telah terisi :')
            print(f'Kursi nomor {kursiA} telah diisi oleh {namaA}')
            print(f'Kursi nomor {kursiB} telah diisi oleh {namaB}')
            print(f'Kursi nomor {kursiD} telah diisi oleh {namaD}')
            break
    

    
       
    





