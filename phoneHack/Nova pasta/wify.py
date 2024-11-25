import subprocess

def get_saved_wifi_passwords():
    print("C/DEDSEC: Fetching WiFi passwords for known networks...")

    try:
        # Lista todas as redes Wi-Fi salvas
        profiles_result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True, check=True)
        profiles_output = profiles_result.stdout
        print(profiles_output)  # Adicionando para ver o que está sendo retornado

        # Extrai os nomes das redes (SSIDs)
        networks = []
        for line in profiles_output.splitlines():
            if "All User Profile" in line:
                # Captura o nome do perfil (SSID)
                networks.append(line.split(":")[1].strip())

        if not networks:
            print("C/DEDSEC: No saved WiFi networks found.")
            return

        # Para cada rede, recupera a senha (se houver)
        for network in networks:
            print(f"\nC/DEDSEC: Network: {network}")
            try:
                # Mostra os detalhes do perfil, incluindo a chave
                password_result = subprocess.run(
                    ["netsh", "wlan", "show", "profile", network, "key=clear"],
                    capture_output=True, text=True, check=True
                )
                password_output = password_result.stdout

                # Busca pela senha
                for line in password_output.splitlines():
                    if "Key Content" in line:
                        password = line.split(":")[1].strip()
                        print(f"    Password: {password}")
                        break
                else:
                    print("    Password: Not found or not set.")
            except subprocess.CalledProcessError:
                print("    Error: Could not retrieve details for this network.")
    except Exception as e:
        print(f"C/DEDSEC: Unexpected error: {e}")

    print("\nC/DEDSEC: Password retrieval complete.")

get_saved_wifi_passwords()
