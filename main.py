import requests
import zipfile
import io
import os

cwd = os.getcwd()
layer_path = '/mnt/c/Users/jboyk/code_stuff/MSL_Data/'

MSDI_PATH = 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/MSDI'
NON_MSDI_PATH = 'https://ftpgeoinfo.msl.mt.gov/Data/Spatial/NonMSDI'

url_dict = {
    '1' : f'{MSDI_PATH}/Cadastral/Parcels/Madison/Madison_GDB.zip',
    '2' : f'{MSDI_PATH}/Cadastral/Parcels/Madison/Madison_SHP.zip',
    '3' : f'{MSDI_PATH}/Hydrography/NHDH_MT_Shape_20221025.zip',
    '4' : f'{NON_MSDI_PATH}/Wells/GWIC_wells.gdb.zip',
    '5' : f'{NON_MSDI_PATH}/Wells/GWIC_wells.shp.zip',
    '6' : f'{MSDI_PATH}/Imagery/2021_NAIP/UTM_County_Mosaics/Madison.sid',
    '7' : f'{MSDI_PATH}/Wetlands/MontanaWetlandRiparian_GDB.zip',
    '8' : f'{MSDI_PATH}/Wetlands/MontanaWetlandRiparian_SHP.zip',
    '9' : f'{MSDI_PATH}/Cadastral/ConservationEasements/MTConservationEasements_GDB.zip'
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
                    z.extractall(path=layer_path)
                    file_name = url.split('/')
                    print(f'{file_name[-1]} - Layer downloaded')

        except UnboundLocalError as e:
            print('Error - Incorrect input: %s' % e)
        except Exception as e:
            print('General exception caught: %s' % e)

def help_prompt():
    print('1 for Parcel GDB\n2 for Parcel SHP\n3 For Hydrography SHP\n4 for GWIC Wells GBD\n5 for GWIC Wells SHP\n6 for 2021 NAIP Imagery SID\
           \n7 for Wetland Riparian GDB\n8 For Wetland Riparian SHP\nOr type "h" for help.\n(Ctrl + C to exit runtime.)\n')

if __name__ == '__main__':
    main()