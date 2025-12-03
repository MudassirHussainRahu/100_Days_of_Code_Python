# Errors

# # FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()


# KeyError
# value = some_dict["non_existent_key"] 

# IndexError
fruit_list = ["Apple", "Banana", "Orange"]
# fruit = fruit_list[3]


# TypeError
text = "abc"
# print(text + 5)  

# Catching Exceptions
# try: (something that might cause an exception)
# except: ( Do this if there was an exception )
# else: ( DO this if there were not exceptions )
# finally: ( Do this not matter what happens )

# FileNotFoundError

# try:
#     file = open("a_file.txt")
#     a_dictionary = { 
#         "key": "value"
#     }
#     print(a_dictionary["key"])

# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")

# except KeyError as error_message:
#     print(f"The key {error_message} does not exit.")

# else:
#     content = file.read()
#     print(content)

# finally:
#     file.close()
#     print("File was closed.")


fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(f"IndexError: {index} out of range.")
    else:
        print(fruit + " pie")
    finally:
        print("Program Ended.")


# make_pie(4)


facebook_posts = [
    {"Likes": 21,  "Comments": 2},
    {"Likes": 13,  "Comments": 2, "Shares":1},
    {"Likes": 33,  "Comments": 8, "Shares":3},
    {"Comments": 4, "Shares":2},
    {"Comments": 1, "Shares":1},
    {"Likes": 19,  "Comments": 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        likes = post["Likes"]
    except KeyError:
        print(f"POST DATA: {post}")
        print("This post hove no likes.")
    else:
        print(f"POST DATA: {post}")
        print(f"This post has {post["Likes"]} likes.")
        total_likes += likes

print(f"{total_likes} Total Likes.")

