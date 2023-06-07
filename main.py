import requests
import zipfile
import io
import os


cwd = os.getcwd()

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

    try:
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
    except UnboundLocalError as e:
        print('Error - Incorrect input: %s' % e)

if __name__ == '__main__':
    main()