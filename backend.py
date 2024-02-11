import spb_data    # spb_data.py MUST be in the SAME FOLDER as this file!
                    # spb_data.py contains the data
import datetime     # We areusing date times for this assessment, and it is
                    # available in the column_output() fn, so do not delete this line

# Data variables
#col variables contain the format of each data column and help display headings
#db variables contain the actual data
col_customers = spb_data.col_customers
db_customers = spb_data.db_customers
col_services = spb_data.col_services
db_services = spb_data.db_services
col_parts = spb_data.col_parts
db_parts = spb_data.db_parts
#col_bills is useful for displaying the headings when listing bills
col_bills = spb_data.col_bills


def next_id(db_data):
    #Pass in the dictionary that you want to return a new ID number for, this will return a new integer value
    # that is one higher than the current maximum in the list.
    return max(db_data.keys())+1

def column_output(db_data, cols, format_str):
    # db_data is a list of tuples.
    # cols is a dictionary with column name as the key and data type as the item.
    # format_str uses the following format, with one set of curly braces {} for each column:
    #   eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
    #   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    #   The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
    #       format_str = "{: <5}  {: ^10}  {: >15}"
    #   Make sure the column is wider than the heading text and the widest entry in that column,
    #       otherwise the columns won't align correctly.
    # You can also pad with something other than a space and put characters between the columns, 
    # eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
    #       format_str = "{:.<5} | {:.^10} | {:.>15}"
    print(format_str.format(*cols))
    for row in db_data:
        row_list = list(row)
        for index, item in enumerate(row_list):
            if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
                row_list[index] = ""       # Replaces them with an empty string
            elif isinstance(item, datetime.date):    # If item is a date, convert to a string to avoid formatting issues
                row_list[index] = str(item)
        print(format_str.format(*row_list))


def list_customers():
    # List the ID, name, telephone number, and email of all customers

    # Use col_Customers for display
   
    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    #Iterate over all the customers in the dictionary
    for customer in db_customers.keys():
        #append to the display list the ID, Name, Telephone and Email
        display_list.append((customer,
                             db_customers[customer]['details'][0],
                             db_customers[customer]['details'][1],
                             db_customers[customer]['details'][2]))
    format_columns = "{: >4} | {: <15} | {: <12} | {: ^12}"
    print("\nCustomer LIST\n")    # display a heading for the output
    column_output(display_list, col_customers, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output



def list_parts():
    # List the ID, name, cost of all parts
    #pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)
    display_part = []
    for part_id in db_parts.keys():
        display_part.append((part_id,
                             db_parts[part_id][0],
                             db_parts[part_id][1]))
    format_part_columns = "{: >4} | {: >15} | {: >9} "
    display_part.sort(key=lambda a: a[1])
    print("\n Parts LIST\n")
    column_output(display_part, col_parts, format_part_columns) 

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output
    

def list_services():
    # List the ID, name, cost of all services
    #pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)
    display_services = []
    for services_id in db_services.keys():
        display_services.append((services_id,
                             db_services[services_id][0],
                             db_services[services_id][1]))
    format_services_columns = "{: >4} | {: >20} | {: >9} "
    display_services.sort(key=lambda a: a[1])
    print("\n Services LIST\n")
    column_output(display_services, col_services, format_services_columns) 

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output

def add_customer():
    # Add a customer to the db_customers database, use the next_id to get an id for the customer.
    # Remember to add all required dictionaries.
    name = str(input("Please enter your name: "))
    phone_number = str(input("Please enter your phone number: "))
    email = str(input("Please enter your email address: "))
    customer_id = next_id(db_customers)
    #dataTime = datetime.date.today()
    # tuple_service = tuple()
    # tuple_parts = tuple()
    # total_price = 0
    # pad_Boolean = False
    db_customers[customer_id] ={
        'details':[name, phone_number, email],
        # 'jobs':{datetime.date(dataTime.year,dataTime.month,dataTime.day):[tuple_service, tuple_parts, total_price, pad_Boolean]}
        'jobs': {}
        }

    #pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def add_job():
    # Add a Job to a customer
    # Remember to validate part and service ids5
    dataTime = datetime.date.today()
    customer_id = int(input("Please enter the customer ID: "))
    tuple_service = input("Enter the service ID or Press Enter to continue: ").split(',')
    tuple_parts = input("Enter the parts ID or Press Enter to continue: ").split(',')
    service_prince = 0
    part_price = 0
    total_price = 0
    pad_Boolean = False
    
    for i in range(len(tuple_service)):
        #if tuple_service[i].isnumeric() == True:
        service_prince += db_services[int(tuple_service[i])][1]

            
    for a in range(len(tuple_parts)):
        #if tuple_parts[a].isnumeric() == True:
        part_price += db_parts[int(tuple_parts[a])][1]
            
    total_price = part_price + service_prince
    db_customers[customer_id]['jobs'][datetime.date(dataTime.year,dataTime.month,dataTime.day)]=[
        tuple(tuple_service), tuple(tuple_parts), total_price, pad_Boolean
        ]
    

    #pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def bills_to_pay():
    #pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)
    anpay_list = []
    for key in db_customers.keys():
        for min_key in db_customers[key]['jobs'].keys():
            if db_customers[key]['jobs'][min_key][-1] == False:
                anpay_list.append((
                    min_key.strftime('%Y-%m-%d'),
                    db_customers[key]['details'][0],
                    db_customers[key]['details'][1]
                    ))
    bil_to_pay = {'Date': str, 'Name': str, 'Phone numbrt': str}
    format_services_columns = "{: >10} | {: >20} | {: >15} "
    print("\n Unpaid Bills\n")
    column_output(anpay_list, bil_to_pay, format_services_columns) 

    input("\nPress Enter to continue.")
    
    
                

def pay_bill():
    #pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)
    customer_anpay_list = []
    cutomer_id = int(input("Please enter customer Id to pay bill:"))
    for mn_key in db_customers[cutomer_id]['jobs'].keys():
        if db_customers[cutomer_id]['jobs'][mn_key][-1] == False:
            service_unpay =''
            for ser in db_customers[cutomer_id]['jobs'][mn_key][0]:
                service_unpay += str(ser) + '  '
            part_unpay = ''
            for part in db_customers[cutomer_id]['jobs'][mn_key][1]:
                part_unpay += str(part) + '  '
                
            customer_anpay_list.append((
                mn_key.strftime('%Y-%m-%d'),
                service_unpay,
                part_unpay,
                db_customers[cutomer_id]['jobs'][mn_key][-2]
                ))
            
    bil_unpay = {'Date': str, 'Service': str, 'part': str, 'Total price': int}
    format_unpaid_columns = "{: >10} | {: >20} | {: >15} | {: >15}"
    print("\n Unpaid Bills under customer "+str(cutomer_id)+" \n")
    column_output(customer_anpay_list, bil_unpay, format_unpaid_columns) 

    paid = input("Pay bill ? Y/N ")
    if paid.upper() == "Y":
        date_price = float(input("please enter price to pay that bill: "))
        for m in db_customers[cutomer_id]['jobs'].keys():
            if db_customers[cutomer_id]['jobs'][m][-2] == date_price:
                db_customers[cutomer_id]['jobs'][m][-1] = True

        
            

# function to display the menu
def disp_menu():
    print("==== WELCOME TO SELWYN PANEL BEATERS ===")
    print(" 1 - List Customers")
    print(" 2 - List Services")
    print(" 3 - List Parts")
    print(" 4 - Add Customer")
    print(" 5 - Add Job")
    print(" 6 - Display Unpaid Bills")
    print(" 7 - Pay Bill")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()
response = input("Please enter menu choice: ")

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X"
while response.upper() != "X":
    if response == "1":
        list_customers()
    elif response == "2":
        list_services()
    elif response == "3":
        list_parts()
    elif response == "4":
        add_customer()
    elif response == "5":
        add_job()
    elif response == "6":
        bills_to_pay()
    elif response == "7":
        pay_bill()
    else:
        print("\n***Invalid response, please try again (enter 1-6 or X)")

    print("")
    disp_menu()
    response = input("Please select menu choice: ")

print("\n=== Thank you for using Selywn Panel Beaters! ===\n")
