import requests
import zipfile
import io
import os


cwd = os.getcwd()
url = 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.zip'

def main():
    print('Current Directory: %s' % cwd)
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

if __name__ == '__main__':
    main()