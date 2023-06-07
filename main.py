import requests
import zipfile
import io
import os


cwd = os.getcwd()
url = 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.zip'

url_dict = {
    '1' : 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.zip',
    '2' : 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.shp'
}

def main():
    print('Current Directory: %s' % cwd)
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

if __name__ == '__main__':
    main()