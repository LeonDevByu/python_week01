# Example 2
# https://byui-cse.github.io/cse111-course/lesson09/write_text.html
# CTREATE  TXT AND CSV FILE
def main():
    # Create a list that contains types of small boats.
    boat_list = ["canoe", "kayak", "skiff", "dinghy"]

    # Write the list to a file named small_boats.txt
    write_list("small_boats.txt", boat_list)


def write_list(filename, text_list):
    """Write the contents of a list into a text file.

    Parameters
        filename: the name of the text file to write
        text_list: the list to write to the text file
    Return: nothing
    """
    # Open the text file for writing and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "wt") as text_file:

        # Print the contents of the list into
        # the text file, one line at a time.
        for element in text_list:
            print(element, file=text_file)


# Call main to start this program.
if __name__ == "__main__":
    main()