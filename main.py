import requests
import zipfile
import io
import os


cwd = os.getcwd()
url = 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.zip'

url_dict = {
    '1' : 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.zip',
    '2' : 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_SHP.zip'
}

def main():
    layer_choice = input('Enter 1 for Parcel GDB\nEnter 2 for Parcel SHP\n')

    for key in url_dict:
        if key == layer_choice:
            url = url_dict[key]
            print(url) 

    print('Current Directory: %s' % cwd)
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

if __name__ == '__main__':
    main()