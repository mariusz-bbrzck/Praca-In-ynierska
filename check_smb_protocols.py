import subprocess

def check_smb_protocols(ip_range):
    try:
        # Wywołanie polecenia nmap w celu skanowania portów SMB na podanym zakresie adresów IP
        command = ['sudo', 'nmap', '-p', '139,445', '--script', 'smb-protocols', '-oN', 'smb_report.txt', ip_range]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Sprawdzenie czy wystąpił błąd podczas wykonania polecenia
        if error:
            print("Wystąpił błąd podczas wykonania polecenia nmap:", error.decode())
            return

        # Wyświetlenie wyniku skanowania
        print(output.decode())
        
    except Exception as e:
        print("Wystąpił błąd:", e)

if __name__ == "__main__":
    ip_range = input("Podaj zakres adresów IP do sprawdzenia (w formacie CIDR np. 192.168.1.0/24): ")
    check_smb_protocols(ip_range)

