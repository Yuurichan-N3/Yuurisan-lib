import os
import sys
from datetime import datetime
import pyfiglet
from colorama import Fore, Style, init

# Biar warna terminal otomatis keriset ke normal setelah print
init(autoreset=True)

def banner(nama_bot):
    # Bersihkan layar (Support Windows nt)
    os.system("cls" if os.name == "nt" else "clear")
    
    # Bikin ASCII Art
    ascii_art = pyfiglet.figlet_format("Yuurisandesu", font="standard").rstrip("\n")
    
    # Print baris per baris sesuai warna
    print(Fore.CYAN + Style.BRIGHT + ascii_art)
    print(Fore.MAGENTA + Style.BRIGHT + f"Welcome to Yuuri's {nama_bot}")
    print(Fore.GREEN + Style.BRIGHT + "Ready to hack the world?")
    print(Fore.YELLOW + Style.BRIGHT + f"Current time: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")

def set_title(nama_bot):
    # Set nama di tab atas terminal
    sys.stdout.write(f"\033]2;{nama_bot} by : 佐賀県産 (YUURI)\007")
    sys.stdout.flush()
