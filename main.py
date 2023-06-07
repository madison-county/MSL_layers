import requests
import zipfile
import io

url = 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.zip'

def main():
    r = requests.get(url)

if __name__ == '__main__':
    main()