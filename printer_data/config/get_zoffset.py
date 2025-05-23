from klippy import printer
import requests

def get_z_offset_2():
    config = printer.lookup_object('configfile')
    probe = printer.lookup_object('probe')
    z_offset = probe.z_offset
    print(f"Z-offset: {z_offset}")

def get_z_offset():
    # URL de l'API Moonraker
    url = "http://localhost:7125/printer/objects/query?probe"

    # Envoyer la requête
    response = requests.get(url)
    data = response.json()

    # Extraire le Z-offset
    z_offset = data['result']['status']['probe']['z_offset']
    print(f"Z-offset: {z_offset}")

if __name__ == '__main__':
    get_z_offset()
    get_z_offset_2()