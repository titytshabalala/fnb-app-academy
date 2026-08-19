#  Build a command-line contact list
# Store contacts as a list of dictionaries

# Create variables to be stored in the dictionary
name = ''
email = ''
phone = ''

#  Create a list ot hold the contacts
contact_list =[]

# add a contact
def add():
    name = input()
    email = input()
    phone = input()

    contact_list.append(contact = {

    })
    print(f"Contact '{name}' has been added successfully!")

def search(name):
    pass

def delete(name):
    pass

def view_all():
    for contact in contact_list:
        for key, value in contact.items():
            print(f"{key}:\t{value}")






while True:
    decision = input('1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit').lower().strip()

    # Conditional loop to get selection
    if decision == 'exit' or '5':
        break
    elif decision == '4' or decision == 'view all':
        view_all()
    elif decision == '3' or decision == 'delete':
        delete()
    elif decision =='2' or decision == 'search':
        search()
    elif decision =='1' or decision == 'add':
        add()
    else:
        print("Incorrect selection... Try again!")