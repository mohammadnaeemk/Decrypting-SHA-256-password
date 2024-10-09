import hashlib
import csv

row_list = [
    ["danial", "99b057c8e3461b97f8d6c461338cf664bc84706b9cc2812daaebf210ea1b9974"],
    ["elham", "85432a9890aa5071733459b423ab2aff9f085f56ddfdb26c8fae0c2a04dce84c"]
]

# create csv
with open('users&pass.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

doc = dict()

def hash_password_hack():
    # تولید هش برای شماره‌های 1000 تا 9999
    for i in range(1000, 9999):
        hashNumber = hashlib.sha256(str(i).encode()).hexdigest()
        doc[hashNumber] = i

    # read data
    with open('users&pass.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # check row
            if len(row) >= 2 and row[1] in doc:
                print("hello mr %s with hashCode %s . your password is : %s" % (row[0], row[1], doc[row[1]]))
            else:
                print("Invalid data or missing hash for %s" % row[0])

hash_password_hack()

