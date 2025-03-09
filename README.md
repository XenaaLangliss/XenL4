# **🔥 XenaaLangliss v1 -  Layer 4 Attack Tool 🔥**
**⚡ Powerful | 🚀 Fast | 🎯 Accurate**

XenaaLangliss v1 adalah **Layer 4 Attack Tool (UDP & TCP Flooder)** yang dapat digunakan untuk **pengujian keamanan jaringan**.
Dilengkapi dengan **log serangan real-time, auto-monitoring IP, dan multi-threading** untuk performa maksimal!

> **🚨 PERINGATAN:** Script ini hanya untuk **pengujian keamanan & pembelajaran**.

> **⚠️ Penyalahgunaan dapat melanggar hukum di negara Anda!**

---

## **🚀 Fitur Unggulan**
✅ **Serangan UDP & TCP** dengan **kecepatan tinggi**  
✅ **Auto-detect sistem** (Termux / Ubuntu)  
✅ **Multi-threading** untuk memaksimalkan performa  
✅ **Auto Monitoring** IP & Port target setelah serangan selesai  
✅ **Script auto-install dependencies** dengan sekali klik  
✅ **Log serangan** untuk melihat hasil secara real-time  
✅ **Ringan & Mudah digunakan**  

---

## **📥 Instalasi & Penggunaan**

### **1️⃣ Install Python & Pip**
Pastikan **Python 3** sudah terinstal di sistem Anda!  
- **Ubuntu/Linux:**  
  ```bash
  sudo apt update && sudo apt install -y python3 python3-pip git
  ```  
- **Termux (Android):**  
  ```bash
  pkg update && pkg install -y python python-pip git
  ```

### **2️⃣ Clone Repository**
```bash
git clone https://github.com/XenaaLangliss/XenL4
cd XenL4
```

### **3️⃣ Jalankan Install Script**
```bash
python3 install.py
```
💡 **Script ini akan otomatis menginstall semua dependensi!**  

### **4️⃣ Jalankan Serangan DDoS**
Gunakan perintah berikut:  
```bash
python3 Xen.py <waktu> <ip> <port> <packet> <threads> <mode>
```
📝 **Contoh:**  
```bash
python3 Xena.py 60 192.168.1.1 80 1024 5 udp
```
> 🔥 **UDP & TCP Attack dalam hitungan detik!**

---

## **🖥️ Monitoring Target Secara Real-Time**
📊 **Setelah serangan selesai, script akan otomatis menampilkan monitoring IP & Port target!**  
> Untuk **Ubuntu**, akan menggunakan `iftop` & `tcpdump`.  
> Untuk **Termux**, akan menggunakan metode alternatif karena paket tersebut tidak tersedia.

---

## ⚠️ Peringatan
> Script ini bersifat open-source dan dibuat untuk tujuan edukasi serta pengujian keamanan. Anda diperbolehkan untuk memodifikasi dan mendistribusikan script ini sesuai dengan ketentuan lisensi yang berlaku.

> Penggunaan alat ini sepenuhnya menjadi tanggung jawab pengguna!
Kami tidak bertanggung jawab atas segala bentuk penyalahgunaan yang bertentangan dengan hukum atau merugikan pihak lain. Gunakan hanya untuk pengujian keamanan, riset pribadi, dan pembelajaran di lingkungan yang diizinkan.

**Jangan gunakan untuk aktivitas ilegal!**
