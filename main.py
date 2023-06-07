import requests
import zipfile
import StringIO

url = 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.zip'

def main():
    x = requests.post(url)

if __name__ == '__main__':
    main()