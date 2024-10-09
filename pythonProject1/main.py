import hashlib
import csv
row_list = [
    ["name", 123],
    ["ahmad",725],
    ["Mohammad" ,4921],
    ["Reza",8915],
]
with open('users&pass.csv' , mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
    file.close()

doc = dict()
def hash_password_hack():
    for i in range(1000,9999):
        hashNumber = hashlib.shake_256(str(i))
        doc[hashNumber] = i
    print(doc)


hash_password_hack()