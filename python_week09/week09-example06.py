# Example 1
# https://byui-cse.github.io/cse111-course/lesson09/write_text.html
# CTREATE  TXT AND CSV FILE
def main():
    # Ask the user to enter a quote.
    quote = input("Please enter an inspirational quote: ")

    # Open the quotes.txt file for appending text.
    with open("quotes.txt", "at") as quotes_file:

        # Print the quote to the text file.
        print(quote, file=quotes_file)


# Call main to start this program.
if __name__ == "__main__":
    main()