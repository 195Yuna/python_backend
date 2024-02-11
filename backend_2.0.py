import spb_data
import datetime

# Data variables
col_customers, db_customers = spb_data.col_customers, spb_data.db_customers
col_services, db_services = spb_data.col_services, spb_data.db_services
col_parts, db_parts = spb_data.col_parts, spb_data.db_parts
col_bills = spb_data.col_bills


def next_id(db_data):
    return max(db_data.keys()) + 1


def column_output(db_data, cols, format_str):
    print(format_str.format(*cols))
    for row in db_data:
        row_list = [item if item is not None else "" for item in row]
        row_list = [str(item) if isinstance(item, datetime.date) else item for item in row_list]
        print(format_str.format(*row_list))


def list_customers():
    display_list = [
        (
            customer,
            db_customers[customer]['details'][0],
            db_customers[customer]['details'][1],
            db_customers[customer]['details'][2]
        )
        for customer in db_customers.keys()
    ]
    format_columns = "{: >4} | {: <15} | {: <12} | {: ^12}"
    print("\nCustomer LIST\n")
    column_output(display_list, col_customers, format_columns)
    input("\nPress Enter to continue.")


def list_parts():
    display_part = [
        (part_id, db_parts[part_id][0], db_parts[part_id][1])
        for part_id in db_parts.keys()
    ]
    format_part_columns = "{: >4} | {: >15} | {: >9} "
    display_part.sort(key=lambda a: a[1])
    print("\n Parts LIST\n")
    column_output(display_part, col_parts, format_part_columns)
    input("\nPress Enter to continue.")


def list_services():
    display_services = [
        (services_id, db_services[services_id][0], db_services[services_id][1])
        for services_id in db_services.keys()
    ]
    format_services_columns = "{: >4} | {: >20} | {: >9} "
    display_services.sort(key=lambda a: a[1])
    print("\n Services LIST\n")
    column_output(display_services, col_services, format_services_columns)
    input("\nPress Enter to continue.")


def add_customer():
    name = input("Please enter your name: ")
    phone_number = input("Please enter your phone number: ")
    email = input("Please enter your email address: ")
    customer_id = next_id(db_customers)
    db_customers[customer_id] = {
        'details': [name, phone_number, email],
        'jobs': {}
    }


def add_job():
    customer_id = int(input("Please enter the customer ID: "))
    tuple_service = input("Enter the service ID or Press Enter to continue: ").split(',')
    tuple_parts = input("Enter the parts ID or Press Enter to continue: ").split(',')
    service_price = sum(db_services[int(ser)][1] for ser in tuple_service)
    part_price = sum(db_parts[int(part)][1] for part in tuple_parts)
    total_price = part_price + service_price
    data_time = datetime.date.today()
    db_customers[customer_id]['jobs'][data_time] = [
        tuple(tuple_service), tuple(tuple_parts), total_price, False
    ]


def bills_to_pay():
    unpaid_list = [
        (
            min_key.strftime('%Y-%m-%d'),
            db_customers[key]['details'][0],
            db_customers[key]['details'][1]
        )
        for key in db_customers.keys()
        for min_key in db_customers[key]['jobs'].keys()
        if not db_customers[key]['jobs'][min_key][-1]
    ]
    bill_columns = {'Date': str, 'Name': str, 'Phone number': str}
    format_unpaid_columns = "{: >10} | {: >20} | {: >15} "
    print("\n Unpaid Bills\n")
    column_output(unpaid_list, bill_columns, format_unpaid_columns)
    input("\nPress Enter to continue.")


def pay_bill():
    customer_unpaid_list = [
        (
            mn_key.strftime('%Y-%m-%d'),
            ', '.join(map(str, db_customers[cutomer_id]['jobs'][mn_key][0])),
            ', '.join(map(str, db_customers[cutomer_id]['jobs'][mn_key][1])),
            db_customers[cutomer_id]['jobs'][mn_key][-2]
        )
        for cutomer_id in db_customers.keys()
        for mn_key in db_customers[cutomer_id]['jobs'].keys()
        if not db_customers[cutomer_id]['jobs'][mn_key][-1]
    ]
    unpaid_columns = {'Date': str, 'Service': str, 'Part': str, 'Total price': int}
    format_unpaid_columns = "{: >10} | {: >20} | {: >15} | {: >15}"
    print("\n Unpaid Bills under customer\n")
    column_output(customer_unpaid_list, unpaid_columns, format_unpaid_columns)
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
