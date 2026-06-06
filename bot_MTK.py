import subprocess
import re
import sys
import time

def solve_math(question):
    """
    Fungsi adaptif untuk mendeteksi bangun datar DAN jenis operasi (Luas/Keliling)
    """
    q_lower = question.lower()
    
    try:
        # Deteksi jenis operasi
        is_luas = "luas" in q_lower
        is_keliling = "keliling" in q_lower
        
        # 1. PERSEGI PANJANG
        if "persegi panjang" in q_lower:
            p = int(re.search(r"panjang (\d+)", q_lower).group(1))
            l = int(re.search(r"lebar (\d+)", q_lower).group(1))
            if is_luas:
                return p * l
            elif is_keliling:
                return 2 * (p + l)
                
        # 2. PERSEGI
        elif "persegi" in q_lower:
            s = int(re.search(r"sisi (\d+)", q_lower).group(1))
            if is_luas:
                return s * s
            elif is_keliling:
                return 4 * s
                
        # 3. SEGITIGA
        elif "segitiga" in q_lower:
            if is_luas:
                a = int(re.search(r"alas (\d+)", q_lower).group(1))
                t = int(re.search(r"tinggi (\d+)", q_lower).group(1))
                return (a * t) // 2
            elif is_keliling:
                # Jika ada variasi soal keliling segitiga sama sisi/sembarang
                # Sediakan fallback atau cari semua angka di dalam soal
                angka = [int(x) for x in re.findall(r"(\d+)\s*cm|\b(\d+)\b", q_lower) if x]
                return sum(angka)
                
        # 4. LINGKARAN
        elif "lingkaran" in q_lower:
            r = int(re.search(r"jari-jari (\d+)", q_lower).group(1))
            if is_luas:
                return (22 * r * r) // 7
            elif is_keliling:
                return (2 * 22 * r) // 7
                
    except Exception as e:
        print(f"\n[Bot Error] Gagal memproses struktur geometri: {e}")
        
    return None

def jalankan_bot():
    # Path relatif menuju file .exe di dalam project Anda
    exe_path = r"nikko_puzzle_windows_amd64\nikko_puzzle_windows_amd64.exe"
    
    print("[*] Menginisialisasi subprocess pipe...")
    try:
        process = subprocess.Popen(
            [exe_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, 
            text=True,
            bufsize=1,
            encoding='utf-8',
            errors='ignore'
        )
    except PermissionError:
        print("[Error] Akses ditolak! Jalankan VS Code sebagai Administrator atau cek hak akses .exe.")
        return
    except FileNotFoundError:
        print(f"[Error] File .exe tidak ditemukan di: {exe_path}")
        return

    buffer = ""
    menu_terpilih = False
    nama_terkirim = False
    nim_terkirim = False

    print("[*] Bot aktif. Menunggu trigger program...\n")
    
    while True:
        char = process.stdout.read(1)
        if not char:
            print("\n[*] Aliran data dari program target terhenti.")
            break
            
        buffer += char
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Opsi Menu CLI
        if "Pilihan [1/2]:" in buffer and not menu_terpilih:
            time.sleep(0.05)
            process.stdin.write("2\n")
            process.stdin.flush()
            menu_terpilih = True
            buffer = ""

        # Pengisian Nama
        elif "Nama Lengkap:" in buffer and not nama_terkirim:
            if buffer.strip().endswith("Nama Lengkap:"):
                time.sleep(0.05)
                process.stdin.write("Cevin Nur Andika\n")
                process.stdin.flush()
                nama_terkirim = True
                buffer = ""

        # Pengisian NIM (Pastikan digit akhir NIM Anda sesuai ketentuan tugas genap/ganjil)
        elif "NIM:" in buffer and not nim_terkirim:
            if buffer.strip().endswith("NIM:"):
                time.sleep(0.05)
                process.stdin.write("2100000002\n")  # Ganti dengan NIM asli Anda (Hanya Angka)
                process.stdin.flush()
                nim_terkirim = True
                buffer = ""

        # Penyelesaian Soal Otomatis
        elif "Answer:" in buffer:
            if buffer.strip().endswith("Answer:"):
                lines = buffer.split("\n")
                soal_ditemukan = ""
                for line in reversed(lines):
                    if "[Question" in line:
                        soal_ditemukan = line
                        break
                
                if soal_ditemukan:
                    jawaban = solve_math(soal_ditemukan)
                    if jawaban is not None:
                        process.stdin.write(f"{jawaban}\n")
                        process.stdin.flush()
                    else:
                        # Fallback jika regex meleset agar tidak langsung kena timeout 1 detik
                        process.stdin.write("0\n")
                        process.stdin.flush()
                
                buffer = ""

if __name__ == "__main__":
    jalankan_bot()