from ui import *
from commands import tree
from auth import login
import datetime

COMMANDS = {
    "LIHAT": "Menampilkan isi direktori",
    "MASUK": "Masuk direktori",
    "MUNDUR": "Kembali",
    "POSISI": "Path aktif",
    "BUKA": "Buat folder",
    "BAKAR": "Hapus folder (PEJABAT)",
    "KEBUN": "Tree direktori",
    "TANAM": "Buat file",
    "PANEN": "Baca file",
    "RAWAT": "Edit file",
    "TEBANG": "Hapus file",
    "CANGKOK": "Copy file",
    "PINDAH": "Pindah file",
    "GANTI": "Rename file",
    "BERSIHKAN": "Clear layar",
    "CLS": "Alias clear",
    "WAKTU": "Waktu",
    "SIAPA": "User aktif",
    "INFO_SAWIT": "Info sistem",
    "NEOFETCH": "Info ala Linux",
    "SU": "Ganti user",
    "SUDO": "Mode pejabat",
    "BANTUAN": "Daftar command",
    "SAWIT": "Easter egg 🌴",
    "EXIT": "Keluar OS",
    "PULANG": "Keluar OS"
}

def shell(fs, users, system, save_fs):
    user = "nugra"
    role = users[user]["role"]
    cwd = ["/", "home", "nugra"]
    history = []

    def curdir():
        d = fs
        for p in cwd:
            d = d[p]
        return d

    def pwd():
        return "/" if cwd == ["/"] else "/".join(cwd)

    banner()

    while True:
        cmd = input(prompt(user, role, pwd())).strip()
        history.append(cmd)
        if not cmd:
            continue
        a = cmd.split()
        c = a[0].upper()

        try:
            if c == "LIHAT":
                print("  ".join(curdir().keys()))

            elif c == "MASUK":
                if a[1] in curdir():
                    cwd.append(a[1])

            elif c == "MUNDUR":
                if len(cwd) > 1:
                    cwd.pop()

            elif c == "POSISI":
                print(pwd())

            elif c == "BUKA":
                curdir()[a[1]] = {}

            elif c == "BAKAR":
                if role == "pejabat":
                    del curdir()[a[1]]
                else:
                    print("Akses ditolak")

            elif c == "KEBUN":
                tree(curdir())

            elif c == "TANAM":
                curdir()[a[1]] = ""

            elif c == "PANEN":
                print(curdir()[a[1]])

            elif c == "RAWAT":
                print("Edit (:simpan)")
                isi = []
                while True:
                    l = input()
                    if l == ":simpan":
                        break
                    isi.append(l)
                curdir()[a[1]] = "\n".join(isi)

            elif c == "TEBANG":
                del curdir()[a[1]]

            elif c == "GANTI":
                curdir()[a[2]] = curdir().pop(a[1])

            elif c in ["BERSIHKAN", "CLS"]:
                banner()

            elif c == "SIAPA":
                print(user, f"({role})")

            elif c == "INFO_SAWIT":
                for k, v in system.items():
                    print(f"{k}: {v}")

            elif c == "NEOFETCH":
                neofetch(system, user)

            elif c == "SU":
                u, r = login(users)
                if u:
                    user, role = u, r

            elif c == "BANTUAN":
                for k, v in COMMANDS.items():
                    print(f"{k:<12} : {v}")

            elif c in ["EXIT", "PULANG"]:
                save_fs(fs)
                print("Keluar dari SaWiTOS 🌴")
                break

            elif c == "SAWIT":
                print("🌴 Sawit adalah masa depan bangsa 🌴")

            else:
                print("Command tidak dikenal")

        except Exception as e:
            print("Error:", e)
