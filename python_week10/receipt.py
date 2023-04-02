import csv
from datetime import datetime


def main():
    try:

        PRODUCT_NUM_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2
        QUANTITY = 1

        products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)
        # print("All Products")
        # print(products_dict)
        print("Inkom Emporium")
        print()
        with open("request.csv", "rt") as dentists_file:
            reader = csv.reader(dentists_file)
            next(reader)
            number_items = 0
            Subtotal = 0
            # print("Requested Items")

            for row_list in reader:
                product_number = row_list[PRODUCT_NUM_INDEX]
                requested_quantity = int(row_list[QUANTITY])
                number_items += requested_quantity

                # if product_number in products_dict:
                #     value = products_dict[product_number]
                #     product_name = value[NAME_INDEX]
                #     product_price = float(value[PRICE_INDEX])
                #
                #     Subtotal += requested_quantity * product_price
                #     Sales_Tax = Subtotal * 0.06
                #     Total = Subtotal + Sales_Tax
                # else:
                #     print("No such student")

                # if product_number in products_dict:
                value = products_dict[product_number]
                product_name = value[NAME_INDEX]
                product_price = float(value[PRICE_INDEX])
                Subtotal += requested_quantity * product_price
                Sales_Tax = Subtotal * 0.06
                Total = Subtotal + Sales_Tax

                print(f"{product_name}: {requested_quantity} @ {product_price}")
        print()
        print(f" Number of Items:{number_items}")
        print(f" Subtotal:{Subtotal:.2f}")
        print(f" Sales Tax:{Sales_Tax:.2f}")
        print(f" Total:{Total:.2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium.")

        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:  %a %b %d %I:%M:%S %Y}")
        print()

        print("Please complete an online survey")
        survey = input("(YES = 1 /NO = 2):")
        if survey == "1":
            print("Responds from 0 to 20: ")
            survey1 = input("1.- Rate the attention in the store in a general way:")
            survey2 = input("2.- The store has good discounts:")
            survey3 = input("3.- Attention is quick:")
            survey4 = input("4.- The salesperson attends kindly:")
            survey5 = input("5.- You would recommend buying in this store:")
            print()

            print("thank you very much for your time, this survey will help us to serve you better, come back soon!:")
        elif survey == "2":
            print("Thank you very much for your purchase, come back soon! : ")
        else:
            print("Please enter the correct data ( 1 or 2): ")

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

    except FileNotFoundError as not_found_err:
        print(not_found_err)

    except PermissionError as perm_err:
        print(perm_err)


def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary


if __name__ == "__main__":
    main()
