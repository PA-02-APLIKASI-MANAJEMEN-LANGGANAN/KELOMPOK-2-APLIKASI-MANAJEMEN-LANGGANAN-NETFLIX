import json
import os
from prettytable import PrettyTable
import pwinput
import time
from colorama import Fore, Back, Style, init 

os.system("cls") 
init(autoreset=True)
 
def load_users():
    try:
        with open('user_langganan.json', 'r') as file:
            users = json.load(file)
        return users
    except FileNotFoundError:
        print(Fore.RED+"File tidak ditemukan. Buat file terlebih dahulu.")
        return []
    except json.JSONDecodeError:
        print(Fore.RED+"Error: File JSON rusak.")
        return []

def load_langganan():
    try:
        with open('langganan.json', 'r') as file:
            langganan = json.load(file)
        return langganan
    except FileNotFoundError:
        print(Fore.RED+"File tidak ditemukan. Buat file terlebih dahulu.")
        return {}
    except json.JSONDecodeError:
        print(Fore.RED+"Error: File JSON rusak.")
        return {}

def simpan_users(users):
    try:
        with open('user_langganan.json', 'w') as file:
            json.dump(users, file, indent=2)
    except Exception as e:
        print(Fore.RED+f"Error menyimpan users: {e}")

def simpan_langganan(langganan):
    try:
        with open('langganan.json', 'w') as file:
            json.dump(langganan, file, indent=2)
    except Exception as e:
        print(Fore.RED+f"Error menyimpan langganan: {e}")
users = load_users() 
langganan_netflix = load_langganan()

def registrasi():
    try:
        print(Fore.BLUE+"+=================================================+")
        print(Fore.BLUE+"|                REGISTRASI AKUN                  |")
        print(Fore.BLUE+"+=================================================+")
        while True:
            username = str(input(Fore.YELLOW + "Masukkan username: "))
            if not username.isalnum():
                print(Fore.RED + "Username hanya boleh berupa huruf & angka")
                continue
            if len(username) > 10:
                print(Fore.RED + "Username maksimal 10 karakter")
                continue
            if any(user['username'] == username for user in users):
                print(Fore.RED + "Username sudah ada")
                continue
            break
        password = pwinput.pwinput(Fore.YELLOW + "Masukkan password: ")
        while True:
            print (Fore.YELLOW + "Verifikasi password")
            password_verif = pwinput.pwinput(Fore.YELLOW + "Masukkan password: ")
            if password != password_verif:
                print(Fore.RED+"Password tidak sesuai.")
                continue
            break
        role = "pengguna"
        new_user = {
            "ID": len(users) + 1,
            "username": username,
            "password": password,
            "role": role,
            "paket berlangganan": "",
            "saldo": 0,
            "status_langganan": "nonaktif"
        }
        users.append(new_user)
        simpan_users(users)
        print (Fore.GREEN + "Memproses Data...")
        print(Fore.GREEN + "1...")
        time.sleep(1)
        print(Fore.GREEN + "2...")
        time.sleep(1)
        print(Fore.GREEN + "3...")
        time.sleep(1)
        print(Fore.GREEN + "Registrasi berhasil! Data pengguna telah disimpan.")
    except KeyboardInterrupt:
        print(Fore.RED+"Jangan tekan ctrl C ya!")
    except EOFError:
        print(Fore.RED+"Jangan tekan ctrl Z ya!")
    except Exception as e:
        print(Fore.RED+f"Error registrasi: {e}")

def login():
    try:
        print(Fore.BLUE+"+=================================================+")
        print(Fore.BLUE+"|                LOGIN AKUN                       |")
        print(Fore.BLUE+"+=================================================+")
        kesempatan = 3
        while kesempatan > 0:
            username = str(input(Fore.YELLOW + "Masukkan username: "))
            password = pwinput.pwinput(Fore.YELLOW + "Masukkan password: ")
            for user in users:
                if user.get('username') == username and user.get('password') == password:
                    print(Fore.GREEN + f"Login berhasil! Selamat datang, {username}.")
                    print(Fore.GREEN + f"Role: {user.get('role')}")
                    return user, user.get('role')
            kesempatan -= 1
            print(Fore.RED + f"Username atau password salah. Sisa kesempatan: {kesempatan}")
        print(Fore.RED+"Terlalu banyak coba. Program berhenti.")
        print(Fore.GREEN + "1...")
        time.sleep(1)
        print(Fore.GREEN + "2...")
        time.sleep(1)
        print(Fore.GREEN + "3...")
        time.sleep(1)
        return None, None     
    except KeyboardInterrupt:
        print(Fore.RED+"Jangan tekan ctrl C ya!")
    except EOFError:
        print(Fore.RED+"Jangan tekan ctrl Z ya!")
    except Exception as e:
        print(Fore.RED+f"Error login: {e}")
        return None, None

def top_up(user):
    try:
        if user["saldo"] < 0:
            user["saldo"] = 0
        print(Fore.GREEN + f"Saldo Anda saat ini: Rp{user['saldo']:,}")
        mau_topup = str(input(Fore.YELLOW + "Mau top-up saldo? (y/n): "))
        if mau_topup.lower() == "y":
            while True:
                try:
                    saldo = int(input(Fore.YELLOW + "Masukkan jumlah top-up: "))
                    if saldo < 10000:
                        print("Minimal top-up adalah Rp10.000.")
                        continue
                    elif saldo > 1000000:
                        print("Maksimal top-up adalah Rp1.000.000.")
                        continue
                    user["saldo"] += saldo
                    simpan_users(users)
                    print(Fore.GREEN + "Print Invoice Top-up Anada")
                    print(Fore.GREEN + "1...")
                    time.sleep(1)
                    print(Fore.GREEN + "2...")
                    time.sleep(1)
                    print(Fore.GREEN + "3...")
                    time.sleep(1)
                    print(Fore.GREEN + f"Top-up berhasil! Saldo sekarang: Rp{user['saldo']:,}")
                    print(Fore.BLUE + "+================= INVOICE TOP-UP ================+")
                    print(Fore.BLUE + f"Jumlah Top-up: Rp{saldo:,}")
                    print(Fore.BLUE + f"Saldo Sekarang: Rp{user['saldo']:,}")
                    print(Fore.BLUE + "+===============================================+")
                    break
                except ValueError:
                    print(Fore.RED+"Masukkan angka yang valid.")
                    continue
        else:
            print(Fore.RED+"Top-up dibatalkan.")
    except KeyboardInterrupt:
        print(Fore.RED+"Jangan tekan ctrl + C ya!")
    except EOFError:
        print(Fore.RED+"Jangan tekan ctrl + Z ya!")
    except Exception as e:
        print(Fore.RED+f"Error top-up: {e}")

def tampilkan_langganan():
    try:
        if not langganan_netflix:
            print(Fore.RED + "Tidak ada data langganan.")
            return
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Harga", "Kualitas", "Jumlah Device"]
        for id, detail in langganan_netflix.items():
            tabel.add_row([id, detail["nama"], detail["harga"], detail["kualitas"], detail["jumlah_device"]])
        print(tabel)
    except Exception as e:
        print(Fore.RED+f"Error tampilkan langganan: {e}")

def menu_admin():
    global peran_pengguna, user_login
    while True:
        print(Fore.BLUE+"+=================================================+")
        print(Fore.BLUE+"|              Selamat Datang Admin               |")
        print(Fore.BLUE+"+=================================================+")
        admin = PrettyTable()
        admin.field_names = ["No.", "Menu"]
        admin.add_row([1, "Tambah Langganan"])
        admin.add_row([2, "Lihat Langganan"])
        admin.add_row([3, "Ubah Langganan"])
        admin.add_row([4, "Hapus Langganan"])
        admin.add_row([5, "Ajuan Pengguna"])
        admin.add_row([6, "Logout"])
        print(Fore.BLUE+ admin.get_string())
        try:
            pilihan = str(input(Fore.YELLOW + "Pilih menu: "))
            if pilihan == "1":
                tambah_langganan()
            elif pilihan == "2":
                lihat_langganan()
            elif pilihan == "3":
                ubah_langganan()
            elif pilihan == "4":
                hapus_langganan()
            elif pilihan == "5":
                ajuan_pengguna()
            elif pilihan == "6":
                print(Fore.GREEN + "Pengguna kembali ke halaman login.")
                peran_pengguna = None
                user_login = None
                break
            else:
                print(Fore.RED+"Input tidak valid.")
        except KeyboardInterrupt:
            print(Fore.RED+"Jangan tekan ctrl C ya!")
        except EOFError:
            print(Fore.RED+"Jangan tekan ctrl Z ya!")
        except Exception as e:
            print(Fore.RED+f"Error menu admin: {e}")
            print("Tolong masukkan angka!")
            print("Pengguna kembali ke halaman login.")
            peran_pengguna = None
            user_login = None
            break

def menu_pengguna():
    global peran_pengguna, user_login
    while True:
        print(Fore.BLUE+"+=================================================+")
        print(Fore.BLUE+"|            Selamat Datang Pengguna              |")
        print(Fore.BLUE+"+=================================================+")
        pengguna = PrettyTable()
        pengguna.field_names = ["No.", "Menu"]
        pengguna.add_row([1, "Tambah Berlangganan"])
        pengguna.add_row([2, "Lihat Berlangganan Saya"])
        pengguna.add_row([3, "Hapus Berlangganan Saya"])
        pengguna.add_row([4, "Top up & Cek Saldo"])
        pengguna.add_row([5, "Logout"])
        print(Fore.BLUE+ pengguna.get_string())
        try:
            pilihan = str(input(Fore.YELLOW + "Pilih menu: "))
            if pilihan == "1":
                tambah_berlangganan(user_login)
            elif pilihan == "2":
                lihat_berlangganan_saya(user_login)
            elif pilihan == "3":
                hapus_berlangganan_saya(user_login)
            elif pilihan == "4":
                top_up(user_login)  
            elif pilihan == "5":
                print(Fore.GREEN + "Pengguna kembali ke halaman login.")
                break
                peran_pengguna = None
                user_login = None
            else:
                print(Fore.RED+"Input tidak valid.")
        except KeyboardInterrupt:
            print(Fore.RED+"Jangan tekan ctrl C ya!")
        except EOFError:
            print(Fore.RED+"Jangan tekan ctrl Z ya!")
        except Exception as e:
            print(Fore.RED+f"Error menu pengguna: {e}")
            print(Fore.RED+"Tolong masukkan angka!")
            print(Fore.RED+"Pengguna kembali ke halaman login.")
            break

def tambah_langganan():
    try:
        tampilkan_langganan()
        id_baru = str(max(int(k) for k in langganan_netflix.keys()) + 1)
        nama = str(input(Fore.YELLOW + "Nama paket: "))
        harga = int(input(Fore.YELLOW + "Harga: "))
        kualitas = str(input(Fore.YELLOW + "Kualitas: "))
        jumlah_device = int(input(Fore.YELLOW + "Jumlah device: "))
        langganan_netflix[id_baru] = {"nama": nama, "harga": harga, "kualitas": kualitas, "jumlah_device": jumlah_device}
        simpan_langganan(langganan_netflix)
        print(Fore.GREEN + "Langganan berhasil ditambahkan.")
    except ValueError:
        print(Fore.RED+"Masukkan data yang valid.")
    except KeyboardInterrupt:
        print(Fore.RED+"Jangan tekan ctrl C ya!")
    except EOFError:
        print(Fore.RED+"Jangan tekan ctrl Z ya!")
    except Exception as e:
        print(Fore.RED+f"Error tambah langganan: {e}")

def lihat_langganan():
    try:
        tampilkan_langganan()
    except Exception as e:
        print(Fore.RED+f"Error lihat langganan: {e}")

def ubah_langganan():
    try:
        tampilkan_langganan()
        id_ubah = str(input(Fore.YELLOW + "ID Langganan yang diubah: "))
        if id_ubah not in langganan_netflix:
            print("ID tidak ditemukan.")
            return
        detail = langganan_netflix[id_ubah]
        tabel = PrettyTable()
        tabel.field_names = ["Nama", "Harga", "Kualitas", "Jumlah Device"]
        tabel.add_row([detail["nama"], detail["harga"], detail["kualitas"], detail["jumlah_device"]])
        print(Fore.GREEN + "Data saat ini:")
        print(tabel)
        nama_baru = str(input(Fore.YELLOW + "Nama paket baru (kosongkan jika tidak ubah): "))
        harga_baru_str = input(Fore.YELLOW + "Harga baru (kosongkan jika tidak ubah): ")
        kualitas_baru = str(input(Fore.YELLOW + "Kualitas baru (kosongkan jika tidak ubah): "))
        jumlah_device_baru_str = input(Fore.YELLOW + "Jumlah device baru (kosongkan jika tidak ubah): ")
        harga_baru = int(harga_baru_str) if harga_baru_str.strip() else None
        jumlah_device_baru = int(jumlah_device_baru_str) if jumlah_device_baru_str.strip() else None
        ada_perubahan = False
        if nama_baru and nama_baru != detail["nama"]:
            langganan_netflix[id_ubah]["nama"] = nama_baru
            ada_perubahan = True
        if harga_baru is not None and harga_baru != detail["harga"]:
            langganan_netflix[id_ubah]["harga"] = harga_baru
            ada_perubahan = True
        if kualitas_baru and kualitas_baru != detail["kualitas"]:
            langganan_netflix[id_ubah]["kualitas"] = kualitas_baru
            ada_perubahan = True
        if jumlah_device_baru is not None and jumlah_device_baru != detail["jumlah_device"]:
            langganan_netflix[id_ubah]["jumlah_device"] = jumlah_device_baru
            ada_perubahan = True
        if ada_perubahan:
            simpan_langganan(langganan_netflix)
            print(Fore.GREEN + "Langganan berhasil diubah.")
        else:
            print(Fore.RED+"Tidak ada perubahan.")
    except ValueError:
        print(Fore.RED+"Masukkan data yang valid.")
    except KeyboardInterrupt:
        print(Fore.RED+"Jangan tekan ctrl C ya!")
    except EOFError:
        print(Fore.RED+"Jangan tekan ctrl Z ya!")
    except Exception as e:
        print(Fore.RED+f"Error ubah langganan: {e}")

def hapus_langganan():
    try:
        while True:
            tampilkan_langganan()
            id_hapus = str(input(Fore.YELLOW + "ID Langganan yang dihapus: "))
            if id_hapus not in langganan_netflix:
                print("Harap masukkan ID yang benar.")
                continue
            detail = langganan_netflix[id_hapus]
            tabel = PrettyTable()
            tabel.field_names = ["ID", "Nama", "Harga", "Kualitas", "Jumlah Device"]
            tabel.add_row([id_hapus, detail["nama"], detail["harga"], detail["kualitas"], detail["jumlah_device"]])
            print(Fore.GREEN + "Data yang akan dihapus:")
            print(tabel)
            konfirmasi1 = str(input(Fore.YELLOW + "Konfirmasi hapus langganan? (y/n): "))
            if konfirmasi1.lower() == "y":
                konfirmasi2 = str(input(Fore.YELLOW + "Konfirmasi lagi? (y/n): "))
                if konfirmasi2.lower() == "y":
                    del langganan_netflix[id_hapus]
                    simpan_langganan(langganan_netflix)
                    print(Fore.GREEN + "Langganan berhasil dihapus.")
                else:
                    print(Fore.GREEN + "Dibatalkan.")
            else:
                print(Fore.GREEN + "Dibatalkan.")
            lagi = str(input(Fore.YELLOW + "Ingin hapus lagi? (y/n): "))
            if lagi.lower() == 'y':
                continue
            elif lagi.lower() == 'n':
                print(Fore.GREEN + "Kembali ke menu utama.")
                break
            else:
                print (Fore.RED+"Input tidak valid")
                continue
    except ValueError:
        print(Fore.RED+"Masukkan data yang valid.")
    except KeyboardInterrupt:
        print(Fore.RED+"Jangan tekan ctrl C ya!")
    except EOFError:
        print(Fore.RED+"Jangan tekan ctrl Z ya!")
    except Exception as e:
        print(Fore.RED+f"Error hapus langganan: {e}")

def ajuan_pengguna():
    try:
        ada_ajuan = False
        for user in users:
            if user["role"] == "pengguna" and user["status_langganan"] == "pending":
                ada_ajuan = True
                print(Fore.GREEN + f"Ajuan dari {user['username']}: Paket {user['paket berlangganan']}")
                setuju = str(input(Fore.YELLOW + "Setujui? (y/n): "))
                if setuju.lower() == "y":
                    user["status_langganan"] = "aktif"
                    simpan_users(users)
                    print(Fore.GREEN + "Ajuan disetujui.")
                else:
                    user["status_langganan"] = "nonaktif"
                    user["paket berlangganan"] = ""
                    simpan_users(users)
                    print(Fore.GREEN + "Ajuan ditolak.")
        if not ada_ajuan:
            print(Fore.GREEN + "Tidak ada ajuan dari pengguna")
    except KeyboardInterrupt:
        print(Fore.RED+"Jangan tekan ctrl C ya!")
    except EOFError:
        print(Fore.RED+"Jangan tekan ctrl Z ya!")
    except Exception as e:
        print(Fore.RED+f"Error ajuan pengguna: {e}")

def tambah_berlangganan(user):
    try:
        tampilkan_langganan()
        id_langganan = str(input(Fore.YELLOW + "ID Langganan: "))
        if id_langganan not in langganan_netflix:
            print(Fore.GREEN + "ID Langganan tidak ditemukan.")
            return
        detail_langganan = langganan_netflix[id_langganan]
        harga = int(detail_langganan["harga"])
        if user["saldo"] < harga:
            print(Fore.GREEN + "Saldo tidak cukup. Top-up dulu.")
            menu_pengguna ()
        elif user["saldo"] > harga:
            konfirmasi1 = str(input(Fore.YELLOW + "Konfirmasi tambah langganan? (y/n): "))
            if konfirmasi1 == "y":
                konfirmasi2 = str(input(Fore.YELLOW + "Konfirmasi lagi? (y/n): "))
                if konfirmasi2 == "y":
                    user["saldo"] -= harga
                    user["paket berlangganan"] = detail_langganan["nama"]
                    user["status_langganan"] = "pending"
                    simpan_users(users)
                    print(Fore.GREEN + "Ajuan berlangganan dikirim ke admin.")
                    print(Fore.GREEN + "Print Invoice Paket Berlangganan Anada")
                    print(Fore.GREEN + "1...")
                    time.sleep(1)
                    print(Fore.GREEN + "2...")
                    time.sleep(1)
                    print(Fore.GREEN + "3...")
                    time.sleep(1)
                    print(Fore.BLUE + "+============= INVOICE BERLANGGANAN =============+")
                    print(Fore.BLUE + f"Paket: {detail_langganan['nama']}")
                    print(Fore.BLUE + f"Harga: Rp{harga:,}")
                    print(Fore.BLUE + f"Saldo Sekarang: Rp{user['saldo']:,}")
                    print(Fore.BLUE + "+===============================================+")
            else:
                print(Fore.GREEN + "Dibatalkan.")
        else:
            print(Fore.RED+"Dibatalkan.")
    except ValueError:
        print(Fore.RED+"Masukkan data yang valid.")
    except KeyboardInterrupt:
        print(Fore.RED+"Jangan tekan ctrl C ya!")
    except EOFError:
        print(Fore.RED+"Jangan tekan ctrl Z ya!")
    except Exception as e:
        print(Fore.RED+f"Error tambah berlangganan: {e}")

def lihat_berlangganan_saya(user):
    try:
        if user["paket berlangganan"]:
            tabel = PrettyTable()
            tabel.field_names = ["Paket", "Status", "Saldo"]
            tabel.add_row([user["paket berlangganan"], user["status_langganan"], user["saldo"]])
            print(tabel)
        else:
            print(Fore.RED+"Tidak ada langganan.")
    except Exception as e:
        print(Fore.RED+f"Error lihat berlangganan saya: {e}")
    except KeyboardInterrupt:
        print(Fore.RED+"Jangan tekan ctrl C ya!")
    except EOFError:
        print(Fore.RED+"Jangan tekan ctrl Z ya!")

def hapus_berlangganan_saya(user):
    try:
        if user["paket berlangganan"]:
            print(Fore.GREEN + f"Data langganan: {user['paket berlangganan']}")
            konfirmasi1 = str(input(Fore.YELLOW + "Yakin hapus langganan? (y/n): Uang tidak dikembalikan."))
            if konfirmasi1 == "y":
                konfirmasi2 = str(input(Fore.YELLOW + "Konfirmasi lagi? (y/n): "))
                if konfirmasi2 == "y":
                    user["paket berlangganan"] = ""
                    user["status_langganan"] = "nonaktif"
                    simpan_users(users)
                    print(Fore.GREEN + "Langganan dihapus.")
                else:
                    print(Fore.RED+"Dibatalkan.")
            else:
                print(Fore.RED+"Dibatalkan.")
        else:
            print(Fore.RED+"Tidak ada langganan.")
    except Exception as e:
        print(Fore.RED+f"Error hapus berlangganan saya: {e}")
peran_pengguna = None
user_login = None

while True:
    print(Fore.BLUE+"+=================================================+")
    print(Fore.BLUE+"|   Selamat Datang di Aplikasi Manajemen Netflix  |")
    print(Fore.BLUE+"+=================================================+")
    menu = PrettyTable()
    menu.field_names = ["No.", "Menu"]
    menu.add_row([1, "Login"])
    menu.add_row([2, "Registrasi"])
    menu.add_row([3, "Leave"])
    print(Fore.BLUE+ menu.get_string())
    try:
        pilihan = int(input(Fore.YELLOW + "Pilih: "))
        if pilihan == 1:
            user_login, peran_pengguna = login()
            if user_login is None or peran_pengguna is None:
                print(Fore.GREEN + "Login gagal.")
                continue
            elif peran_pengguna == "Admin":
                menu_admin()
                peran_pengguna = None
                user_login = None
            elif peran_pengguna == "pengguna":
                menu_pengguna()
                peran_pengguna = None
                user_login = None
            else:
                print(Fore.GREEN + "Peran tidak dikenali.")
                continue
        elif pilihan == 2:
            registrasi()
        elif pilihan == 3:
            print (Fore.BLUE+"+=================================================+")
            print (Fore.BLUE+"|    TERIMAKASIH SUDAH MENGGUNAKAN SISTEM 👋      |")
            print (Fore.BLUE+"+=================================================+")
            break
        else:
            print(Fore.GREEN + "Input Tidak Valid.")
            continue
    except Exception as e:
        print(Fore.GREEN + f"Error umum: {e}")
        print(Fore.GREEN + "Program akan kembali ke awal.")
        peran_pengguna = None
        user_login = None
