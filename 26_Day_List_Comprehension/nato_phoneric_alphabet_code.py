import pandas as pd

df_alphabets = pd.read_csv("nato_phonetic_alphabet.csv")

# print(df_alphabets.head(10))

nato_phoneric_alphabets_dict = {
    row.letter:row.code for (index, row) in df_alphabets.iterrows()
}

# print(nato_phoneric_alphabets_dict)

while True:
    word = input("Enter a word or exit:")
    if word == "exit":
        print("Exiting!!!!!")
        break
    
    phonetic_code = []
    for letter in word:
        code = nato_phoneric_alphabets_dict[letter.upper()]
        phonetic_code.append(code)

    print(phonetic_code)