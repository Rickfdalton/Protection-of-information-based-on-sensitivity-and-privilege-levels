import configparser
config = configparser.ConfigParser()
# Connection for the doctor
config['John'] = {'username': 'john',
                     'password': '5f4dcc3b5aa765d61d8327deb882cf99',
                     'role': 'medical practitioner',
                     'privileges': 'read,write datafile'}
# Connection for the clerk
config['Tommy'] = {'username': 'tommy',
                     'password': '5f4dcc3b5aa765d61d8327deb882cf99',
                     'role': 'clerk',
                     'privileges':'read datafile'}
# Connection for the patient
config['Billy'] = {'username': 'billy',
                     'password': '5f4dcc3b5aa765d61d8327deb882cf99',
                     'role': 'patient',
                     'privileges':'read only his/her details'}


with open('my_config.ini', 'w') as configfile:
    config.write(configfile)