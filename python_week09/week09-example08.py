# Example 3
# https://byui-cse.github.io/cse111-course/lesson09/write_text.html
# CTREATE  TXT AND CSV FILE
import csv

def main():
    heading_list = ["Title", "Author", "Composer"]

    # Create a compound list of hymns.
    hymns_list = [
        ["O Holy Night", "John Dwight", "Adolphe Adam"],
        ["Oh, Come, All Ye Faithful", "John Wade", "John Wade"],
        ["Joy to the World", "Isaac Watts", "George Handel"],
        ["With Wondering Awe", "Anonymous", "Anonymous"]
    ]

    # Call the write_compound_list function which will
    # write the list of hymns to a file named "hymns.csv".
    write_compound_list("hymns.csv", hymns_list, heading_list)


def write_compound_list(filename, compound_list,
        heading_list=None):
    """Write the contents of a compound list into a CSV file.

    Parameters
        filename: the name of the CSV file to write
        compound_list: the list to write to the CSV file
        heading_list: a list that contains the column headings.
            If heading_list is None, this function will not
            write headings to the CSV File.
    Return: nothing
    """
    # Open the text file for writing and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "wt", newline="") as csv_file:

        # Use the csv module to create a writer object
        # that will write to the opened CSV file.
        writer = csv.writer(csv_file)

        # Write the heading_list to the CSV file.
        if heading_list is not None:
            writer.writerow(heading_list)

        # Write the contents of the list into
        # the CSV file, one row at a time.
        for row_list in compound_list:
            writer.writerow(row_list)


# Call main to start this program.
if __name__ == "__main__":
    main()