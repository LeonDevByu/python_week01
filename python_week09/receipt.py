import csv


def main():
    PRODUCT_NUM_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY = 1

    products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)
    print("All Products")
    print(products_dict)

    with open("request.csv", "rt") as dentists_file:
        reader = csv.reader(dentists_file)
        next(reader)

        print("Requested Items")
        for row_list in reader:

            product_number = row_list[PRODUCT_NUM_INDEX]
            requested_quantity = int(row_list[QUANTITY])

            if product_number in products_dict:
                value = products_dict[product_number]
                product_name = value[NAME_INDEX]
                product_price = value[PRICE_INDEX]

                print(f"{product_name}: {requested_quantity} @ {product_price}")
            # print(f"{product_name} : {requested_quantity} @ {product_price}")
        # print(f"{product_name} : {requested_quantity} @ {product_price}")




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
