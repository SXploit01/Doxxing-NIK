import json
import os

# ANSI escape sequences for coloring #Untuk warna ygy
RESET = "\033[0m"
RED = "\033[31m"
PURPLE = "\033[35m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GREEN = "\033[32m"
BLUE = "\033[34m"

def main():
    os.system("clear")

    print(PURPLE + "⣿⡟⠁     ⠨⠝⣿⣿⣿⣿⣿⣿⡛⠭⠈⠹⣿⣿" + RESET)
    print(PURPLE + "⣿⣴⣶⣶⣦⣄  ⠈⢻⣿⣿⣿⢻⠁⣤⣶⣶⣶⣼⣿" + RESET)
    print(PURPLE + "⣿⣿⡿⢟⡛⠟⠿⢆⢻⣿⣿⣿⢧⠾⠛⠟⣛⢿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⢛⡁      ⢀⣿⣿⣿⣿⣇    ⠁⣙⠻⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣶⣷⣿⣿⠟⣿⣿⣿⠿⣿⣷⣷⣾⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣿⣿⠿⢫⡄⣿⣿⣿⣦⣝⢿⣿⣿⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⡧⢙⠛⣛⣭⣴⣧⡛⢿⠿⠿⠿⢗⣥⣶⣬⣟⠛⡛⢡⣿" + RESET)
    print(PURPLE + "⣿⡆⢣⡈⠻⣿⠿⠿⠁⢉⡉⠈⠻⠿⢿⡿⠋⡰⢁⣾⣿" + RESET)
    print(PURPLE + "⣿⣿⣆⢑⢤⣤⣤⡄⢀⣚⣛⢂⢀⣤⣤⣤⠜⢁⣾⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣦⡻⣾⣿⣿⣷⠸⠿⢃⣼⣿⣿⡾⣡⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣿⣶⡹⢿⣿⡇  ⢸⣿⡿⣟⣽⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣿⣿⣿⣷⣾⣇⡀⢀⣼⣴⣾⣿⣿⣿⣿⣿⣿" + RESET)
    print(PURPLE + "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿" + RESET)
    print(RED + " ___ __  __      ___   ___  ___  _  _  _____" + RESET) 
    print(RED + "/ __|\ \/ /___  / _ \ / __||_ _|| \| ||_   _|" + RESET)
    print(RED + "\__ \ >  <|___|| (_) |\__ \ | | | .` |  | |" + RESET)  
    print(RED + "|___//_/\_\     \___/ |___/|___||_|\_|  |_|" + RESET)                                             
    print(RESET + "===============================================================" + RESET)
    print(BLUE + "Creator : SXploit" + RESET)
    print(BLUE + "Telegram : t.me/SXploit" + RESET)
    print(BLUE + "Instagram : slmnxploit" + RESET)
    print(GREEN + "Script : Maintenance/Masih Dikembangkan!" + RESET)

    nik = input(RED + "Input NIK Target: " + RESET)

    if not nik.isdigit() or len(nik) != 16:
        print(RED + "ERROR! NIK Tidak Valid!" + RESET)
        return

    tanggal = nik[6:8]
    bulan = nik[8:10]
    tahun = nik[10:12]
    provinsi = nik[0:2]
    kabkot = nik[0:4]
    kecamatan = nik[0:6]
    uniqcode = nik[12:16]

    cekjk = int(nik[6:8])
    jeniskelamin = "LAKI-LAKI" if cekjk <= 40 else "PEREMPUAN"

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(RED + "! Data Tidak Valid !" + RESET)
        return

    provinsi = data.get("provinsi", {}).get(provinsi, provinsi)
    kabkot = data.get("kabkot", {}).get(kabkot, kabkot)
    kecamatan_data = data.get("kecamatan", {}).get(kecamatan, kecamatan)

    if isinstance(kecamatan_data, str):
        kecamatan_name, kode_pos = kecamatan_data.split("--")
    else:
        kecamatan_name, kode_pos = kecamatan, "N/A"

    print(f"{GREEN}!Tanggal Lahir: {tanggal}/{bulan}/{tahun}{RESET}")
    print(f"{GREEN}!Jenis Kelamin: {jeniskelamin}{RESET}")
    print(f"{GREEN}!Provinsi: {provinsi}{RESET}")
    print(f"{GREEN}!Kab/Kota: {kabkot}{RESET}")
    print(f"{GREEN}!Kecamatan: {kecamatan_name}{RESET}")
    print(f"{GREEN}!Kode Pos: {kode_pos}{RESET}")
    print(f"{GREEN}!Uniqcode: {uniqcode}{RESET}")

if __name__ == "__main__":
    main()