import pandas as pd
import os 
from tabulate import tabulate
import datetime
import time
from colorama import init
from termcolor import colored

init()

def godang():
    print(colored(''' ====================================================
                                                     
░██████╗░░█████╗░██████╗░░█████╗░███╗░░██╗░██████╗░  
██╔════╝░██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔════╝░  
██║░░██╗░██║░░██║██║░░██║███████║██╔██╗██║██║░░██╗░  
██║░░╚██╗██║░░██║██║░░██║██╔══██║██║╚████║██║░░╚██╗  
╚██████╔╝╚█████╔╝██████╔╝██║░░██║██║░╚███║╚██████╔╝  
░╚═════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░  
                                                     
==================================================== ''', "green"))

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def tips():
    clear()
    godang()
    print('''
    Pilih jenis tanaman :
    1. Padi 🌾
    2. Jagung 🌽
    3. Cabai 🌶️
    4. Tomat 🍅
    ''')
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        clear()
        padi()
    if pilihan == 2:
        clear()
        jagung()
    if pilihan == 3:
        clear()
        cabe()
    if pilihan == 4:
        clear()
        tomat()

def signup(): #untuk masuk ke fitur signup
    global df1
    godang()
    print('\nREGISTRASI', end="")
    df = pd.read_csv('data_userpass.csv', usecols = ['user','pass'])
    data = df['user']
    for row in data:
        while True:
            username = input('\nMasukkan username : ')
            if username in df['user'].values:
                print('Maaf, username sudah dipakai')
            else :
                break
        password1 = input('Masukkan password : ')
        password2 = input('Konfirmasi password : ')
        if password1 != password2:
            print('Password yang anda masukkan tidak sama, silahkan coba lagi')
            clear()
            signup()
        else :
            df1 = pd.DataFrame({'user' : [username], 'pass': [password1]})
            df1.to_csv('data_userpass.csv', mode='a', index=False, header=False)
            clear()
            print('''Selamat anda sudah terdaftar'''.center(80))
            time.sleep(3)
            clear()
        login()
    
def login():
    global username1
    clear()
    godang()
    print('\nMASUK')
    df = pd.read_csv('data_userpass.csv', usecols = ['user','pass'])
    username1 = input('Masukkan username : ')
    password = input('Masukkan password : ')   
    data = df.isin([username1, password]).any().any()
    if data :
        fitur2()
    else:
        clear()
        godang()
        print("Username atau password yang anda masukkan salah")
        print("\n1. Coba lagi\n2. Kembali")
        lagi = input("\nMasukkan pilihan anda : ")
        if lagi == 1:
            clear()
            login()
        else:
            clear()
            fitur1()

def back():
    lagi = input("\n\nTekan Enter untuk kembali ke menu")
    if lagi == "":
        clear()
        fitur2()

def fitur1():
    clear()
    godang()
    print('''
    1. Sign up
    2. Log in
    3. Exit

    ''')
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        clear()
        signup()
    if pilihan == 2:
        clear()
        login()
    if pilihan == 3:
        print('See you later our farmer :D')
        exit()

def fitur2():
    clear()
    godang()
    print('''
Hello {}

    Pilih fitur :
    1. Stok barang
    2. Tips bertani
    3. Hapus akun
    4. Bantuan
    5. Log out
    
    '''.format(username1))
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        clear()
        stok()
    if pilihan == 2:
        clear()
        tips()
    if pilihan == 3:
        clear()
        hapusakun()
    if pilihan == 4:
        clear()
        bantuan()
    if pilihan == 5:
        clear()
        fitur1()

def stok():
    clear()
    godang()
    print('\n1. Info stok\n2. Tambah stok\n3. Ambil stok\n4. Kembali\n')
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        clear()
        info()
    if pilihan == 2:
        clear()
        tambah()
    if pilihan == 3:
        clear()
        ambil()
    if pilihan == 4:
        clear()
        fitur2()

def info():
    clear()
    godang()
    print('\n1. Info stok bibit\n2. Info stok pupuk\n3. Kembali\n')
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        clear()
        infobibit()
    if pilihan == 2:
        clear()
        infopupuk()
    if pilihan == 3:
        clear()
        fitur2()

def tambah():
    clear()
    godang()
    print('\n1. Tambah stok bibit\n2. Tambah stok pupuk\n3. Kembali\n')
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        clear()
        tambahbibit()
    if pilihan == 2:
        clear()
        tambahpupuk()
    if pilihan == 3:
        clear()
        fitur2()

def ambil():
    clear()
    godang()
    print('1. Ambil stok bibit\n2. Ambil stok pupuk\n3. Kembali')
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        clear()
        ambilbibit()
    if pilihan == 2:
        clear()
        ambilpupuk()
    if pilihan == 3:
        clear()
        fitur2()

def tambahbibit():
    clear()
    godang()
    df = pd.read_csv('bibit.csv', index_col=0)
    df1 = pd.DataFrame(df)
    now = datetime.datetime.now()
    tanggal = now.strftime("%Y-%m-%d %H:%M:%S")
    bibit = input("Masukkan jumlah bibit yang akan ditambah (gr) : ")
    df2 = pd.DataFrame({'Tanggal' : [tanggal], 'Penambahan bibit (gr)' : [bibit]})
    df2.to_csv('bibit.csv', mode='a', index=False, header=False)
    print('\n---Stok berhasil ditambahkan---')
    back()

def tambahpupuk():
    clear()
    godang()
    df = pd.read_csv('pupuk.csv', index_col=0)
    df1 = pd.DataFrame(df)
    now = datetime.datetime.now()
    tanggal = now.strftime("%Y-%m-%d %H:%M:%S")
    pupuk = int(input("Masukkan jumlah pupuk yang akan ditambah (kg): "))
    data = {'Tanggal' : [tanggal], 'Penambahan pupuk (kg)' : [pupuk], 'Pengambilan pupuk (kg)' : 0}
    df = pd.DataFrame(data, columns = ["Tanggal", "Penambahan pupuk (kg)", "Pengambilan pupuk (kg)", "Total"])
    df.to_csv('pupuk.csv', mode='a', index=False, header=False)
    print('\n---Stok berhasil ditambahkan---')
    back()

def infobibit():
    clear()
    godang()
    df = pd.read_csv('bibit.csv')
    head = ['Tanggal','Penambahan bibit (gr)','Pengambilan bibit (gr)','Total']
    df = df.fillna(0)
    df.index += 1
    total2 = df['Pengambilan bibit (gr)'].sum().astype('int')
    df = pd.DataFrame(df)
    df['Total']= df['Penambahan bibit (gr)'] - df['Pengambilan bibit (gr)']
    df['Total']= df['Total'].cumsum()
    total3 = df.iloc[-1]['Total'].astype('int')
    print(tabulate(df, headers=head,tablefmt="grid"))
    print('Total penggunaan bibit (gr) :', total2) 
    print('Sisa bibit (gr) :', total3)
    back()

def infopupuk():
    global total1
    clear()
    godang()
    df = pd.read_csv('pupuk.csv')
    head = ['Tanggal','Penambahan pupuk (kg)','Pengambilan pupuk (kg)','Total']
    df = df.fillna(0)
    df.index += 1
    total2 = df['Pengambilan pupuk (kg)'].sum().astype('int')
    df = pd.DataFrame(df)
    df['Total']= df['Penambahan pupuk (kg)'] - df['Pengambilan pupuk (kg)']
    df['Total']= df['Total'].cumsum()
    total1 = df.iloc[-1]['Total'].astype('int')
    print(tabulate(df, headers=head,tablefmt="grid"))
    print('Total penggunaan pupuk (kg) :', total2) 
    print('Sisa pupuk (kg) :', total1)
    back()

def ambilpupuk():
    clear()
    godang()
    now = datetime.datetime.now()
    tanggal = now.strftime("%Y-%m-%d %H:%M:%S")
    pupuk = input("Masukkan jumlah pupuk yang akan diambil (kg) : ")
    data = {'Tanggal' : [tanggal], 'Pengambilan pupuk (kg)' : [pupuk]}
    df = pd.DataFrame(data, columns = ["Tanggal", "Penambahan pupuk (kg)", "Pengambilan pupuk (kg)", "Total"])
    df.to_csv('pupuk.csv', mode='a', index=False, header=False)
    print('\n---Stok berhasil dikurangi---')
    back()

def ambilbibit():
    clear()
    godang()
    df = pd.read_csv('bibit.csv', index_col=0)
    now = datetime.datetime.now()
    tanggal = now.strftime("%Y-%m-%d %H:%M:%S")
    bibit = input("Masukkan jumlah bibit yang akan diambil (gr) : ")
    data = {'Tanggal' : [tanggal], 'Pengambilan bibit (gr)' : [bibit]}
    df = pd.DataFrame(data, columns = ["Tanggal", "Penambahan bibit (gr)", "Pengambilan bibit (gr)", "Total"])
    df.to_csv('bibit.csv', mode='a', index=False, header=False)
    print('\n---Stok berhasil dikurangi---')
    back()

def hapusakun():
    lagi = input("Apakah anda yakin ingin menghapus akun anda? [y/n] : ")
    lagi.lower()
    if lagi == "y":
        df = pd.read_csv('data_userpass.csv')
        df.drop(df.loc[df.user==username1].index, axis=0, inplace=True)
        df.to_csv('data_userpass.csv', index=False)
        clear()
        print("Akun telah terhapus".center(80))
        time.sleep(3)
        fitur1()
    else:
        clear()
        print("Terima kasih sudah tetap bersama GoDang".center(80)) 
        time.sleep(3)
        fitur2()

def padi():
    clear()
    file = open("padi.txt")
    print(file.read()) 
    back()

def jagung():
    clear()
    file = open("jagung.txt")
    print(file.read()) 
    back()

def cabe():
    clear()
    file = open("cabe.txt", errors="ignore")
    print(file.read()) 
    back()

def tomat():
    clear()
    file = open("tomat.txt", errors="ignore")
    print(file.read()) 
    back()

def bantuan():
    clear()
    godang()
    print('1. Guideline\n2. Fitur Godang \n3. Kritik dan Saran\n4. Kembali')
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        clear()
        guide()
    if pilihan == 2:
        clear()
        fitur()
    if pilihan == 3:
        clear()
        kritikdansaran()
    if pilihan == 4:
        clear()
        fitur2()

def fitur():
    clear()
    godang()
    file = open("penjelasanfitur.txt", errors="ignore")
    print(file.read()) 
    back()

def kritikdansaran():
    clear()
    godang()
    file = open('kritikdansaran.txt', "a")
    while True:
        kritik = str(input("Kritik : "))
        saran = str(input("Saran : "))
        if len(kritik)and len(saran) >0:
            file.write("\nKritik : {} \n".format(kritik))
            file.write("Saran : {}".format(saran))
            file.write("\n")
            break
        else:
            break
    file.close()
    back1()

def guide():
    clear()
    godang()
    print('''
    Pilih guideline fitur :
    1. Sign up
    2. Login
    3. Stok barang
    4. Tips bertani
    5. Hapus akun
    6. Bantuan
    ''')
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        clear()
        gsignup()
    if pilihan == 2:
        clear()
        glogin()
    if pilihan == 3:
        clear()
        gstok()
    if pilihan == 4:
        clear()
        gtips()
    if pilihan == 5:
        clear()
        ghapus()
    if pilihan == 6:
        clear()
        gbantuan()

def back1():
    lagi = input("\n\nTekan Enter untuk kembali ke fitur bantuan")
    if lagi == "":
        clear()
        bantuan()

def gsignup():
    clear()
    godang()
    file = open("GLsignup.txt", errors="ignore")
    print(file.read()) 
    back1()

def glogin():
    clear()
    godang()
    file = open("GLllogin.txt", errors="ignore")
    print(file.read()) 
    back1()

def gstok():
    clear()
    godang()
    file = open("Stokbarang.txt", errors="ignore")
    print(file.read()) 
    back1()

def gtips():
    clear()
    godang()
    file = open("tipsbertani.txt", errors="ignore")
    print(file.read()) 
    back1()

def ghapus():
    clear()
    godang()
    file = open("hapusakun.txt", errors="ignore")
    print(file.read()) 
    back1()

def gbantuan():
    clear()
    godang()
    file = open("bantuan.txt", errors="ignore")
    print(file.read()) 
    back1()

fitur1()
