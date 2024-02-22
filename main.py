import random
import sys
import time

def ke(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)

lobang = """ 
Harap baca dulu:

Udin terjebak dalam hutan dan Udin menemukan lobang tapi Udin bingung 😕. Nih, mau milih yang mana, bisa kah Anda bantu? Silakan!

------------------------------------
|    1     |     2     |    3      |
|          |           |           |  
------------------------------------
"""

def main():
    acak = random.randint(1, 3)
    print(lobang)
    user1 = int(input("Tebak lobang mana yang benar untuk dilewati (1, 2, 3): "))
    time.sleep(2)
    user2 = input(f"Wah, udah milih aja nih! Milih yang {user1} lagi yakin nih {user1} itu pilihan yang tepat? Mau ganti ketik 'y' (y/t): ")

    if user2.lower() == 'y':
        time.sleep(1)
        user3 = int(input('Ok, mau ganti nomor apa nih bro (1, 2, 3): '))
        print(f"Ok, kamu pilih {user3}\n")
        time.sleep(1)
        print("Yakin bro? Saya kunci jawaban kamu ya")
        time.sleep(1)
        print(f"Tadi jawabannya {user3}. Ok, saya kunci jawaban kamu.\n")
        time.sleep(0.65)
        print('Dan jawabannya adalah...')
        time.sleep(1)
        ke('dededenggggggggg..................\n')
        time.sleep(1)

        if user3 == acak:
            print(f'Duarrrrrrrrrrrrr')
            time.sleep(2)
            print(f'dan jawabannya adalah {acak} Horeeeeeee selamat mas brooo!!!!! Akhirnya Udin selamat juga yaa, Alhamdulillah ')
        else:
            print(f'Duarrrrrrrrrrrrr\n')
            time.sleep(2)
            print(f"Yahahahhahah, kamu salah. Jawabannya {user3} salah. Nomor yang benar itu {acak} bro, Udin jadinya dimakan sama anak kondang 🐍 dong ): ")
    else:
        print('Wah, Anda ini langsung ngegas saja ya bro, rileks bro, buru-buru amat milihnya wkwkw \n')
        time.sleep(3)
        print("Gw konci yaa jawabannya")
        time.sleep(1)

        if user1 == acak:
            print("Dan jawabannya adalah...\n")
            time.sleep(1)
            print(f'Benarrrrrrrrr, jawabannya adalah {user1} kerennnn!!! Alhamdulillah Udin selamat yaaa')
        else:
            print("Dan jawabannya adalah...\n")
            time.sleep(1)
            print(f"Salah...... masa jawabannya {user1} salahlah bego... hahahha nomor yang bener adalah {acak} bro, Udin jadinya dimakan sama anak kondang 🐍 dong ):")

if __name__ == "__main__":
    main()
