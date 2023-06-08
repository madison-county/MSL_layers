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

    valid_input = False

    print('Enter 1 for Parcel GDB\nEnter 2 for Parcel SHP\nOr type "h" for help.\n(Ctrl + C to exit runtime.)\n')
    while not valid_input:
        layer_choice = input('\n')
        try:
            if layer_choice.lower() == 'h':
                print ('1 for Parcel Data GDB\n2 for Parcel Data SHP.\n')

            for key in url_dict:
                if key == layer_choice:
                    url = url_dict[key]
                    #valid_input = True
                    print('Retrieving Data Layer at: \n %s' % url)
                    r = requests.get(url)
                    z = zipfile.ZipFile(io.BytesIO(r.content))
                    z.extractall()

        except UnboundLocalError as e:
            print('Error - Incorrect input: %s' % e)
        except Exception as e:
            print('General exception caught: %s' % e)

def help_prompt():
    pass

if __name__ == '__main__':
    main()