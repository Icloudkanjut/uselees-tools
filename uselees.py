import sys, os, requests, shutil, platform, psutil, subprocess, socket, speedtest, time
from requests import get

speed = speedtest.Speedtest()

banner = """[ Welcome to Uselees Tools by @fooster1337 on github ]
[ Why You Using This Tools? ]

[1] Input Identias
[2] Check tinggi / ngak
[3] Math
[4] Download File From Url
[5] You Computer (os, ip , ram usage)
[6] Internet Speed Checker 
[7] Script Deface Generator
[99] About
[00] Exit
"""
def anu():
    print("[+] Identitas [+]\n")
    nama = input("Silahkan masukan nama mu: ")
    kelas = input("Kelas : ")
    no_absen = input("No absen : ")
    no_telp = input("No telp (6285xxxx): ")
    tinggi_badan = input("tinggi badan : ")

    no_absen = int(no_absen)
    no_telp = int(no_telp)
    tinggi_badan = int(tinggi_badan)
    kelas = int(kelas)

    print("====== Result ========")
    print("Nama         :", nama)
    print("Kelas        :", kelas)
    print("No absen     :", no_absen)
    print("No telp      :", no_telp)
    print("tinggi badan :", tinggi_badan)
    print("======= Saved ========")

    saved_identitas = """==== Identitas Saved ====
Nama         : {}
Kelas        : {}
No Absen     : {}
No Telp      : {}
Tinggi Badan : {}
=========================
    """.format(nama, kelas, no_absen, no_telp, tinggi_badan)

    saved = input("Save identitas? [y/n] : ")
    if saved == "y":
        name = input("Nama file yang akan disimpan : ")
        f = open(name, "w")
        f.write(saved_identitas)
        print("File saved on", name)
        input("Press enter for back to main menu")
        main()

    elif saved == "n":
        print("Identitas Tidak Di Save")
        input("Press enter for back to main menu")
        main()

    else:
        print("Identitas Tidak Di Save")
        input("Press enter for back to main")
        main()

def math():
    print("==== Matematika ====\n")
    print("[1] pertambahan\n[2] Pengurangan\n[3] Pembagian\n[4] Perkalian\n[0] Back to main menu")
    x = input("Choose : ")
    if x == "1":
        tambah()
    elif x == "2":
        ngurang()
    elif x == "3":
        bagi()
    elif x == "4":
        kali()
    elif x == "0":
        main()
    else:
        print("[!] Gak ada bro")
        math()

def anu2():
    print("+++ Cek tinggi badan +++")
    tinggi = input("Masukan tinggi badan mu : ")
    tinggi = int(tinggi)
    if tinggi < 150:
        print("=> Lu pendek awk")
        input("Press enter for back to main menu")
        main()
    else:
        print("=> Lu tinggi bang")
        input("Press enter for back to main menu")
        main()

def tambah():
    print("== Pertambahan ==")
    tambah1 = input("Masukan bilangan [1]: ")
    tambah2 = input("Masukan bilangan [2]: ")
    hasil = int(tambah1) + int(tambah2)
    print('Hasil dari {} + {} : {}'.format(tambah1, tambah2, hasil))
    input("Press Enter For Continue...")
    math()

def login():
    key = input("Key : ")
    if key == "whatudoing":
        print("Login Succes...")
        time.sleep(2)
        main()
    else:
        print("Key Invalid, try again")
        login()


def ngurang():
    print("== Pengurangan ==")
    ngurang1 = input("Masukan bilangan [1]: ")
    ngurang2 = input("Masukan bilangan [2]: ")
    hasil = int(ngurang1) - int(ngurang2)
    print('Hasil dari {} - {} : {}'.format(ngurang1, ngurang2, hasil))
    input('Press enter for continue...')
    math()

def bagi():
    print("== Pembagian ==")
    bagi1 = input("Masukan bilangan [1]: ")
    bagi2 = input("Masukan bilangan [2]: ")
    hasil = int(bagi1) / int(bagi2)
    print('Hasil dari {} bagi {}: {}'.format(bagi1, bagi2, hasil))
    input("Press enter for continue..")
    math()

def kali():
    print("== Perkalian ==")
    kali1 = input("Masukan bilangan [1]: ")
    kali2 = input("Masukan bilangan [2]: ")
    hasil = int(kali1) * int(kali2)
    print('Hasil {} kali {}: {}'.format(kali1, kali2, hasil))
    input("Press enter for continue")
    math()

def download():
    print("[+] Download File From Url [+]")
    down = input("Url File : ")
    name_file = os.path.basename(down)
    print("File Name -> ", name_file)
    down2 = requests.get(down, stream = True)
    if down2.status_code == 200:
        with open(name_file, 'wb') as f:
            shutil.copyfileobj (down2.raw, f)
        print("-> Download Saved on", name_file)
        input("Press enter for back to main menu")
        main()
    else:
        print("-> Download Error!")
        input("Press enter for back to main menu")
        main()

def about():
    print("Tools ini mungkin akan sedikit berguna hehe:v btw yang buat ganteng loh bisa chat ke instagram @alfrdzi_azl")
    input("Press enter for back to main menu")
    main()
    
def speedcheck():
    print(f"[+] Download Speed : {'{:.2f}'.format(speed.download()/1024/1024)} Mb/s")
    print(f"[+] Upload Speed   : {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")
    input("Press enter for back to main menu")
    main()
    
def identity():
    os_name = platform.system()
    ip = get('https://api.ipify.org').text
    ram = psutil.Process().memory_info().rss / (1024 * 1024)
    print("[+] You Computer Identity")
    print("OS           ->", os_name)
    print("IP           ->", ip)
    print("RAM USAGE    ->", ram)
    input("[+] Press enter for back to main menu")
    main()

def scriptdeface():
    print("=== Script Deface Generator ===\n")
    judul = input("Title Script Deface : ")
    nama_defacer = input("Nick Defacer : ")
    email = input("Email Defacer : ")
    thanks_to = input("Thanks To (Nick Teman, Team, Sebagainya) : ")
    nama_team = input("Nama Team : ")

    scdepes = """<!--- Sc Defacer Generator By fooster1337 -->
<html>
    <head>
        <title>{}</title>
        <meta name="keyword" content="Hacked by {}, {}">
        <meta name="description" content="Wh00pz Im S0rry">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
        <meta charset="utf-8">
    </head>
<body bgcolor="black">
<font color="white" face="courier">
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<center>
<font size="4">Hacked by {} <font color="red">#{}</font>
<font size="4">Wh00pz You Website has been hacked!</font><br><br>
<font size="2">{}</font><br><br>
<font size="2">{} | </font>
<font size="2">+ Click You Screen For Song +</font>
</center>
</html>
""".format(judul, nama_defacer, nama_team, nama_defacer, nama_team, thanks_to, email)
    
    scdepes_saved = input("Nama File Yang Akan Disimpan (depes.html) : ")
    f = open(scdepes_saved, "w")
    f.write(scdepes)
    print("File Saved on", scdepes_saved)
    input("Press Enter For Back To Main Menu")
    main()

def main():
    os.system("clear")
    print(banner)
    menu = input("root@uselees~# ")
    if menu == "1":
        anu()
    elif menu == "2":
        anu2()
    elif menu == "3":
        math()
    elif menu == "4":
        download()
    elif menu == "5":
        identity()
    elif menu == "6":
        speedcheck()
    elif menu == "7":
        scriptdeface()
    elif menu == "99":
        about()
    elif menu == "00":
        exit()
    else:
        print("[!] Pilihan Gak Ada Bro")
        input("Press enter for back to main menu")
        main()

if __name__ == "__main__":
    try:
        login()
    except KeyboardInterrupt:
        print("\n[!] Ctrl + C Detect...")
        sys.exit(0)
