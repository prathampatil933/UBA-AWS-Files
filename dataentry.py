import secrets
import boto3
import random
import string

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

#define numbers
reqemail=2
requser=5
reqaccount=7

# Define the table name
table_name = 'Accounts'
table_name2 = 'tester'

en1 = ['HDFC', 'SBI', 'ICICI', 'BOM', 'KOTAK']
en2 = ['PUNE', 'MUMBAI', 'DELHI', 'KOLKATTA', 'CHENNAI']
en3 = ['HDFC001', 'SBI002', 'ICICI909', 'BOM078', 'KOTAK088']
en4 = ['yes', 'yes']

def generate_account_number(length):
    characters = string.digits 
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

def generate_random_email(length):
    characters = string.ascii_letters 
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

def generate_random_mobile_number(length):
    characters = string.digits 
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

def generate_random_atm_number(length):
    characters = string.digits 
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

def generate_random_balance(length):
    characters = string.digits 
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

def generate_random_name(length):
    characters = string.ascii_letters
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits 
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string


en5 = [generate_random_email(5) + '@gmail.com' for _ in range(reqemail)]


# Insert 1000 items into the DynamoDB table
for _ in range(reqaccount):
    temp=random.choice(en1);
    item1 = {
        'Acc_no': {'S': generate_account_number(10)},
        'atmno': {'S': generate_random_atm_number(4)},
        'balance': {'N': generate_random_balance(5)},
        'bank': {'S': temp},
        'branch': {'S': random.choice(en2)},
        'ifsc': {'S': temp + generate_random_atm_number(5)},
        'phno': {'S': generate_random_mobile_number(10)},
        #'uid': {'S': generate_random_email(5)+'@gmail.com'}
        'uid' : {'S':random.choice(en5)}
    }

    response = dynamodb.put_item(
        TableName=table_name,
        Item=item1
    )

for _ in range(requser):
    item2 = {
        #'uid': {'S': generate_random_email(5)+'@gmail.com'},
        'uid' : {'S':random.choice(en5)},
        'accounts': {'S': generate_account_number(10)},
        'isvalid': {'S': random.choice(en4)},
        'name': {'S': generate_random_name(5)},
        'password': {'S': generate_random_password(5)}
    }

    response = dynamodb.put_item(
        TableName=table_name2,
        Item=item2
    )

print("Items inserted successfully.")