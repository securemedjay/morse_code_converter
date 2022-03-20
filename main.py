import pandas

data = pandas.read_csv("morse.csv")
data_dict = {value.string: value.morse_code for (key, value) in data.iterrows()}
is_continue = True


def return_morse(word):
    morse_word = ""
    for char in word:
        morse_letter = str(data_dict[char])
        morse_word += f"{morse_letter} "

    return morse_word


while is_continue:
    user_input = input("Enter the word you want to convert to morse code: ").upper()
    converted = return_morse(user_input)
    print(f"Morse Code: {converted}")
    status = input("Continue? (Enter Y/N): ").upper()
    if status == "N":
        is_continue = False
