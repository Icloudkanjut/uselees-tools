#!/usr/bin/python -tt

import sys, os, requests, shutil, platform, psutil, subprocess, socket, speedtest, time, os.path
from requests import get
from playsound import playsound

speed = speedtest.Speedtest()

version = "0.3"

banner = """[ Welcome to Uselees Tools by @fooster1337 on github ]
[ Why You Using This Tools? ]
[ Version : {} ]

[1] Input Identias
[2] Check tinggi / ngak
[3] Math
[4] Download File From Url
[5] You Computer (os, ip , ram usage)
[6] Internet Speed Checker 
[7] Script Deface Generator
[8] Read file
[9] Hack Satelit
[10] Play sound / music
[11] Create shorcut whatsapp
[12] Youtube Downloader
[99] About
[00] Exit
""".format(version)

daftar_satelit = """
(*) Pilih satelit yang ingin di hack :

[1] Palapa
[2] Usa 313
[3] Telkom
[4] Lapan A-3
[5] Sich-1
"""

def anu():
    print("[-- Identitas --]\n")
    nama = input("[?] Silahkan masukan nama mu: ")
    kelas = input("[?] Kelas : ")
    no_absen = input("[?] No absen : ")
    no_telp = input("[?] No telp (6285xxxx): ")
    tinggi_badan = input("[?] tinggi badan : ")

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

    saved = input("[?] Save identitas? [y/n] : ")
    if saved == "y":
        name = input("[*] Nama file yang akan disimpan : ")
        f = open(name, "w")
        f.write(saved_identitas)
        print("File saved on", name)
        input("[-] Press enter for back to main menu")
        main()

    elif saved == "n":
        print("[-] Identitas Tidak Di Save")
        input("Press enter for back to main menu")
        main()

    else:
        print("[-] Identitas Tidak Di Save")
        input("Press enter for back to main")
        main()

def math():
    print("[ x - + ÷ ] Matematika [ x - + ÷ ]\n")
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
    print("[-- Cek tinggi badan --]")
    tinggi = input("Masukan tinggi badan mu : ")
    tinggi = int(tinggi)
    if tinggi < 150:
        print("[=>] Lu pendek awk")
        input("[+] Press enter for back to main menu")
        main()
    else:
        print("[=>] Lu tinggi bang")
        input("[+] Press enter for back to main menu")
        main()

def tambah():
    print("[-- + Pertambahan + --]")
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
    print("[-- - Pengurangan - --]")
    ngurang1 = input("Masukan bilangan [1]: ")
    ngurang2 = input("Masukan bilangan [2]: ")
    hasil = int(ngurang1) - int(ngurang2)
    print('[*] Hasil Pengurangan {} - {} : {}'.format(ngurang1, ngurang2, hasil))
    input("[+] Press enter for back to main menu")
    math()

def bagi():
    print("[-- : Pembagian : --]")
    bagi1 = input("Masukan bilangan [1]: ")
    bagi2 = input("Masukan bilangan [2]: ")
    hasil = int(bagi1) / int(bagi2)
    print('[*] Hasil Pembagian {} ÷ {} : {}'.format(bagi1, bagi2, hasil))
    input("[+] Press enter for back to main menu")
    math()

def kali():
    print("[-- x Perkalian x --]")
    kali1 = input("Masukan bilangan [1]: ")
    kali2 = input("Masukan bilangan [2]: ")
    hasil = int(kali1) * int(kali2)
    print('[*] Hasil perkalian {} X {} : {}'.format(kali1, kali2, hasil))
    input("[+] Press enter for back to main menu")
    math()

def download():
    print("[+] Download File From Url [+]")
    down = input("Url File : ")
    name_file = os.path.basename(down)
    print("[*] File Name -> ", name_file)
    down2 = requests.get(down, stream = True)
    if down2.status_code == 200:
        with open(name_file, 'wb') as f:
            shutil.copyfileobj (down2.raw, f)
        print("[->] Download Success! Saved on", name_file)
        input("[+] Press enter for back to main menu")
        main()
    else:
        print("[->] Download Error!")
        input("[+] Press enter for back to main menu")
        main()

def about():
    print("Tools ini mungkin akan sedikit berguna hehe:v btw yang buat ganteng loh bisa chat ke instagram @alfrdzi_azl atau telegram @GrazzMean")
    input("[+] Press enter for back to main menu")
    main()
    
def speedcheck():
    print(f"[+] Download Speed : {'{:.2f}'.format(speed.download()/1024/1024)} Mb/s")
    print(f"[+] Upload Speed   : {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")
    input("[+] Press enter for back to main menu")
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
    print("[-- Script Deface Generator --]\n")
    judul = input("[?] Title Script Deface : ")
    nama_defacer = input("[?] Nick Defacer : ")
    email = input("[?] Email Defacer : ")
    nama_team = input("[?] Nama Team : ")
    gambar = input("[?] Link Gambar : ")
    font_color = input("[?] Font color : ")
    deskripsi = input("[?] Deskripsi : ")
    pesan = input("[?] Pesan pada script deface : ")
    bg_color = input("[?] Background color (Jika warna font hitam gunakan background putih, dan sebaliknya) : ")
    link = input("[?] Link contact (bisa berupa whatsapp, telegram atau yang lain) : ")

    scdepes = """<!--- Sc Defacer Generator By fooster1337 -->
<html>
<head>
<title>{}</title>
<link rel="icon" href="https://icons.iconarchive.com/icons/custom-icon-design/all-country-flag/256/Indonesia-Flag-icon.png">
<meta name="description" content="Hacked by {}, {}">
<meta name="keyword" content="Hacked by {}">
</head>
<body bgcolor="{}">
<font color="{}">
<center>
<img src="{}" width="250" height="none"><br><br>
<font face="courier" size="3">Hacked by {} | <font color="red">#{}</font><br>
<font face="courier" size="2">-> {} <-<br> {} / <a style="text-decoration: none; color: {};" href="{}">Contact? Click here</font><br><br>
<font face="courier" size="2">[-- Click you screen for good music --]</font>
</center>
</html>
""".format(judul, nama_defacer, deskripsi, nama_defacer, bg_color, font_color, gambar, nama_defacer, nama_team, pesan, email, font_color, link)
    
    scdepes_saved = input("Nama File Yang Akan Disimpan (depes.html) : ")
    f = open(scdepes_saved, "w")
    f.write(scdepes)
    print("[*] File Saved on", scdepes_saved)
    input("[+] Press enter for back to main menu")
    main()

def hack_satelit():
    print("[-- Hack Satelit --]")
    print(daftar_satelit)
    hack1 = input("[?] Pilih yang ingin di hack : ")
    hack2 = int(input("[?] Mau geser brp cm? : "))
    hack3 = input("[?] geser ke arah mana? [Kanan/kiri] : ")
    if hack1 == "1":
        print("\n")
        print("(*) Kode exploitasi sedang dijalankan...")
        time.sleep(4)
        print("(*) Mengubah orbit sebesar {} cm".format(hack2))
        time.sleep(5)
        print("(*) Menggeser ke arah", hack3)
        time.sleep(5)
        print("[*] Berhasil menggeser satelit Palapa sebesar {} cm ke arah {}!".format(hack2, hack3))
        print("\n")
        input("[*] Press enter for back to main menu")
        main()
    elif hack1 == "2":
        print("\n")
        print("(*) Kode exploitasi sedang dijalankan...")
        time.sleep(4)
        print("(*) Mengubah orbit sebesar {} cm".format(hack2))
        time.sleep(5)
        print("(*) Menggeser ke arah", hack3)
        time.sleep(5)
        print("[*] Berhasil menggeser satelit Usa 313 sebesar {} cm ke arah {}!".format(hack2, hack3))
        print("\n")
        input("[*] Press enter for back to main menu")
        main()
    elif hack1 == "3":
        print("\n")
        print("(*) Kode exploitasi sedang dijalankan...")
        time.sleep(4)
        print("(*) Mengubah orbit sebesar {} cm".format(hack2))
        time.sleep(5)
        print("(*) Menggeser ke arah", hack3)
        time.sleep(5)
        print("[*] Berhasil menggeser satelit Telkom sebesar {} cm ke arah {}!".format(hack2, hack3))
        print("\n")
        input("[*] Press enter for back to main menu")
        main()
    elif hack1 == "4":
        print("\n")
        print("(*) Kode exploitasi sedang dijalankan...")
        time.sleep(4)
        print("(*) Mengubah orbit sebesar {} cm".format(hack2))
        time.sleep(5)
        print("(*) Menggeser ke arah", hack3)
        time.sleep(5)
        print("[*] Berhasil menggeser satelit Lapan A-3 sebesar {} cm ke arah {}!".format(hack2, hack3))
        print("\n")
        input("[*] Press enter for back to main menu")
        main()
    elif hack1 == "5":
        print("\n")
        print("(*) Kode exploitasi sedang dijalankan...")
        time.sleep(4)
        print("(*) Mengubah orbit sebesar {} cm".format(hack2))
        time.sleep(5)
        print("(*) Menggeser ke arah", hack3)
        time.sleep(5)
        print("[*] Berhasil menggeser satelit Sich-1 sebesar {} cm ke arah {}!".format(hack2, hack3))
        print("\n")
        input("[*] Press enter for back to main menu")
        main()

    else:
        print("[!] Pilihan satelit tidak ada!")
        input("[*] Press enter for back to main menu")
        main()

def read_file():
    print("[-- Read File --]\n")
    read = input("File yang ingin dibaca : ")
    print("\n")
    f = open(read, 'r')
    print(f.read())
    print("[*] Reading file : {}".format(read))
    input("[*] Press enter for back to main menu")
    main()

def ytdownloader_check():
    print("[*] Checking youtube-dl...")
    if os.path.isfile("/usr/bin/youtube-dl"):
        print("[*] Already installed!")
        time.sleep(1.5)
    else:
        print("[x] youtube-dl is not installed, please install on you system...")
        exit()

    print("[*] Checking ffmpeg...")
    if os.path.isfile("/usr/bin/ffmpeg"):
        print("[*] Already installed")
        time.sleep(1.5)
        ytdownloader()
    else:  
        print("[x] ffmpeg is not installed, please install on you system...")
        exit()

def playsoundmusic():
    print("[-- Play Music --]")
    file_input = input("[?] Music file : ")
    print("[*] Playing music :", file_input)
    playsound(file_input)
    input("[*] Press enter for back to main menu")
    main()

def shortcutwa():
    print("[-- Shorcut Whatsapp --]")
    no = input("[?] No Wa [62xxx] : ")
    text = input("[?] Text yang akan dikirim ke nomor : ")
    link = """https://api.whatsapp.com/send?phone={}&text={}""".format(no, text)
    print("[*] Shorcut :", link)
    input("[*] Press enter for back to main menu")
    main()

def single_url_yt():
    print("[-- Single url ]")
    linkyt = input("[?] Yt Link : ")
    os.system("youtube-dl -o '(%title)s | %(upload)s.%(ext)s' --format mp4 {}".format(linkyt))
    input("[*] Press enter for back to main menu")
    main()

def down_from_list_yt():
    print("[-- Download From List --]")
    file = input("[?] Location file : ")
    f = open(file, 'r')
    line_count = 0
    for line in f:
        if line != "\n":
            line_count += 1
    f.close()
    print("[+] {} Link Found!".format(line_count))
    mp = input("[?] audio / mp4 : ")
    if mp == "audio":
        print("[*] Audio Downloading...")
        os.system("youtube-dl -o '%(title)s | %(uploader)s.%(ext)s' -x --audio-format mp3 -a {}".format(file))
        input("[*] Press enter for back to main menu")
        main()
    elif mp == "mp4":
        print("[*] MP4 Downloading...")
        os.system("youtube-dl -o '%(title)s | %(uploader)s.%(ext)s' --format mp4 -a {}".format(file))
        input("[*] Press enter for back to main menu")
        main()
    else:
        print("[!] Not found!.")
        time.sleep(2)
        down_from_list_yt()

def url_downloader_yt():
    print("[-- 2 Url Downloader --]")
    link1 = input("[?] Link 1 : ")
    link2 = input("[?] Link 2 : ")
    mp1 = input("[?] audio / MP4 : ")
    if mp1 == "audio":
        print("[*] Audio Downloading...")
        os.system("youtube-dl -x --audio-format mp3 -o '%(title)s | %(upload)s.%(ext)s' {} {}".format(link1, link2))
        input("[*] Press enter for back to main menu")
        main()
    elif mp1 == "mp4":
        print("[*] MP4 Downloading..")
        os.system("youtube-dl --format mp4 -o '%(title)s | %(upload)s.%(ext)s' {} {}".format(link1, link2))
        input("[*] Press enter for back to main menu")
        main()

    else:
        print("[!] Not found!")
        time.sleep(2)
        url_downloader_yt()

def audio_only_yt():
    print("[-- Audio only --]")
    linkyt = input("[?] Yt Link : ")
    os.system("youtube-dl -o '%(title)s | %(upload)s.%(ext)s' -x --audio-format mp3 {}".format(linkyt))
    input("[*] Press enter for back to main menu")
    main()
 
def high_q_a_yt():
    print("[-- High Quality + Audio --]")
    linkyt = input("[?] Link Yt : ")
    os.system("youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]' -o '%(title)s | %(upload)s.%(ext)s' {}".format(linkyt))
    input("[*] Press enter for back to main menu")
    main()

def ytdownloader():
    os.system("clear")
    menu = """
[1] Single url download (.mp4)
[2] Download from list (.txt) (.mp4 + audio)
[3] 2 url downloader (.mp4 + audio)
[4] Download audio only
[5] Download with High quality and audio (.mp4 + audio)
"""
    print("[-- Yt Downloader --]")
    print(menu)
    mn = input("[?] Choose : ")
    if mn == "1":
        single_url_yt()
    elif mn == "2":
        down_from_list_yt()
    elif mn == "3":
        url_downloader_yt()
    elif mn == "4":
        audio_only_yt()
    elif mn == "5":
        high_q_a_yt()
    else:
        print("[!] Not found.")
        time.sleep(1)
        ytdownloader()

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
    elif menu == "8":
        read_file()
    elif menu == "9":
        hack_satelit()
    elif menu == "10":
        playsoundmusic()
    elif menu == "11":
        shortcutwa()
    elif menu == "12":
        ytdownloader_check()
    elif menu == "99":
        about()
    elif menu == "00":
        exit()
    else:
        print("[!] Not found.")
        input("[*] Press enter for back to main menu")
        main()

if __name__ == "__main__":
    try:
        login()
    except KeyboardInterrupt:
        print("\n[!] Ctrl + C Detect...")
        sys.exit(0)
    except FileNotFoundError:
        print("[!] Error file not found!..")
        input("[+] Press enter for back to main menu")
        main()
