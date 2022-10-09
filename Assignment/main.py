import configparser
import hashlib
import json


config=configparser.ConfigParser()
# read the configuration file
config.read('my_config.ini')
users=config.sections()

# Opening JSON file
f = open('datafile.json','r+')
data = json.load(f)


 



username = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()
password_hash = hashlib.md5(password.encode()).hexdigest()



if(username in users):
    if(config[username]['password'] == password_hash):
        print()
        print("Welcome, "+config[username]['role']+" : " + username)
        if (config[username]['role'] == 'medical practitioner'):
            print()
            print("enter 1 to read datafile")
            print("enter 2 to write to datafile")
            print()
            choice = input("Enter your choice: ").strip()
            if(choice == '1'):
                print(data)
            if(choice=='2'):
                print("Enter the patient's username: ")
                patient_username = input().strip()
                print("Enter the patient's name: ")
                name = input().strip()
                print("Enter the patient's age: ")
                age = input().strip()
                print("Enter the patient's address: ")
                address = input().strip()
                print("sickness:")
                sickness=input().strip()
                print("symptoms:")
                symptoms=input().strip()
                print("diagnosis:")
                diagnosis=input().strip()
                print("treatment:")
                treatment=input().strip()
                print("date:")
                date=input().strip()
                print("drug prescriptions:(Enter , seperated values)")
                drug=input().split(',')
                print("lab prescriptions:(Enter , seperated values)")
                lab=input().split(',')

                new_data = {
                "personal_details": {
                    "name": name,
                    "age": age,
                    "address": address
                },
                "sickness_details": {
                    "sickness": sickness,
                    "symptoms": symptoms,
                    "diagnosis": diagnosis,
                    "treatment": treatment,
                    "date": date
                },
                "drug_prescriptions":drug,
                "lab_test_prescriptions": lab
                }
                data.update({patient_username: new_data})
                f.seek(0)
                json.dump(data, f, indent = 4)
        elif (config[username]['role'] == 'clerk'):
            print()
            print("enter 1 to read datafile")
            choice = input("Enter your choice: ").strip()
            if(choice == '1'):
                print(data)
        elif (config[username]['role'] == 'patient'):
            print()
            print("enter 1 to read your medical information")
            choice = input("Enter your choice: ").strip()
            if(choice == '1'):
                print(data[username])
                
                
                


    else:
        print("Incorrect password")
else:
    print(username)
    print("User does not exist")

f.close()