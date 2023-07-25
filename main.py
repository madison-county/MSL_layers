import requests
import zipfile
import io
import os

cwd = os.getcwd()

url_dict = {
    '1' : 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.zip',
    '2' : 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_SHP.zip',
    '3' : 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI/Hydrography/NHDH_MT_Shape_20221025.zip',
    '4' : 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/NonMSDI/Wells/GWIC_wells.gdb.zip',
    '5' : 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/NonMSDI/Wells/GWIC_wells.shp.zip'
}

def main():

    valid_input = False

    help_prompt()
    while not valid_input:
        layer_choice = input('\n')
        try:
            if layer_choice.lower() == 'h':
                help_prompt()

            for key in url_dict:
                if key == layer_choice:
                    url = url_dict[key]
                    #valid_input = True
                    print('Retrieving Data Layer at: \n %s' % url)
                    r = requests.get(url)
                    z = zipfile.ZipFile(io.BytesIO(r.content))
                    z.extractall()
                    file_name = url.split('/')
                    print(f'{file_name[-1]} - Layer downloaded')

        except UnboundLocalError as e:
            print('Error - Incorrect input: %s' % e)
        except Exception as e:
            print('General exception caught: %s' % e)

def help_prompt():
    print('1 for Parcel GDB\n2 for Parcel SHP\n3 For Hydrography SHP\n4 for GWIC Wells GBD\n5 for GWIC Wells SHP\nOr type "h" for help.\n(Ctrl + C to exit runtime.)\n')

if __name__ == '__main__':
    main()