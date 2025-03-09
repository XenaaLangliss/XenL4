import os
import subprocess
import time

# Cek apakah berjalan di Termux atau Linux (Ubuntu)
def detect_system():
    if "com.termux" in os.environ.get("HOME", ""):
        return "Termux"
    else:
        return "Linux (Ubuntu)"

# Jalankan perintah di shell
def run_command(command, description):
    print(f"\n\033[33m[+] {description}...\033[0m")
    time.sleep(1)  # Jeda agar proses terlihat lebih jelas
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"\033[32m[✓] {description} berhasil!\033[0m")
    except subprocess.CalledProcessError:
        print(f"\033[31m[!] Gagal menjalankan: {command}\033[0m")

# Install package di Termux atau Linux
def install_package(package, description):
    system = detect_system()
    if system == "Termux":
        run_command(f"pkg install -y {package}", description)
    else:
        run_command(f"sudo apt install -y {package}", description)

# Install pip dependencies
def install_pip(package):
    run_command(f"pip3 install {package}", f"Instalasi Python package: {package}")

# Install semua dependensi
def install_dependencies():
    os_type = detect_system()
    print(f"\n\033[34m[+] Detected OS: {os_type}\033[0m\n")
    time.sleep(1)

    # Update package list
    install_package("", "Memperbarui daftar paket")

    # Install Python dan dependencies
    system = detect_system()
    if system == "Termux":
        install_package("python python-pip net-tools", "Menginstal Python dan Net-tools")
        install_package("tsu", "Menginstal tsu untuk akses root di Termux (jika diperlukan)")
    else:
        install_package("python3 python3-pip net-tools tcpdump iftop", "Menginstal Python, Net-tools, tcpdump, dan iftop")

    # Install library Python
    install_pip("psutil")
    install_pip("requests")

    # Jika di Termux, gunakan `termux-wake-lock` agar tidak sleep saat proses berjalan
    if system == "Termux":
        run_command("termux-wake-lock", "Mengaktifkan termux wake-lock agar tidak sleep")

    print("\n\033[32m[✓] Instalasi selesai! \033[0m")

# Jalankan script
if __name__ == "__main__":
    install_dependencies()
