import requests
import time
import os
from colorama import Fore

print("===========================================")
print('BOT AUTO CHAT DISCORD BY Thirteen𝕏')
print("===========================================\n")

time.sleep(1)

channel_id = input("Masukkan ID channel: ")
waktu1 = int(input("Set Waktu Kirim Pesan: "))

time.sleep(1)
print("Loading...")
time.sleep(1)
print("Loading...")
time.sleep(1)
print("Loading...")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

# Membaca pesan dari file dan menyimpannya dalam list
with open("pesan.txt", "r") as f:
    words = [line.strip() for line in f.readlines()]

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

# Memulai iterasi pesan secara berurutan
index = 0  # Menetapkan nilai awal untuk index

while True:
    # Memastikan ID channel tidak memiliki spasi di awal/akhir
    channel_id = channel_id.strip()

    # Mengambil pesan berdasarkan index saat ini
    payload = {
        'content': words[index]
    }

    headers = {
        'Authorization': authorization
    }

    try:
        # Mengirim pesan
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        if r.status_code == 200:
            print(Fore.WHITE + "Sent message: ")
            print(Fore.YELLOW + payload['content'])
        else:
            print(Fore.RED + f"Failed to send message: {r.status_code}")
        
        # Update index untuk pesan selanjutnya
        index += 1
        if index >= len(words):
            index = 0  # Reset index ke awal jika sudah mencapai akhir list

        # Tunggu sebelum mengirim pesan berikutnya
        time.sleep(waktu1)

    except Exception as e:
        print(Fore.RED + f"Error occurred: {e}")
        time.sleep(waktu1)
