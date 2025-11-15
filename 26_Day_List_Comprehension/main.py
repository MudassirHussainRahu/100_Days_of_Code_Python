import random
import pandas as pd

# List and Dictionary Comprehension
# Python Sequences (list, range, string, tuple)

def main():

    # Traditional Way
    numbers = [1,2,3]
    new_list = []
    for n in numbers:
        add_1 = n + 1
        new_list.append(add_1)

    # print(numbers)
    # print(new_list)

    # list comprehension
    numbers = [1,2,3]
    new_list = [ num+1 for num in numbers ]
    # print(numbers)
    # print(new_list)

    name = "Mudassir"
    new_list = [ letter for letter in name ]
    # print(name)
    # print(new_list)


    first_four_numbers = range(1,5)
    new_list = [ n*2 for n in first_four_numbers ]
    # print(first_four_numbers)
    # print(new_list)

    # Long names ( > 4 characters ) short names ( <=4 characters )
    names = [ "Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie" ]
    short_names = [ name for name in names if len(name)<= 4 ] 
    # print(names)
    # print(short_names)
    long_names = [ name.upper() for name in names if len(name) > 4 ]
    # print(long_names)


    # squared numbers and even numbers

    numbers = [1,1,2,3,5,8,13,21,34,55]
    squared_numbers = [ n**2 for n in numbers ]
    # print(squared_numbers)

    even_numbers = [ n for n in numbers if n%2 == 0 ]
    # print(even_numbers)

    # numbers common in both files (file1 and file2)

    with open("file1.txt") as file:
        f1 = file.read()
    
    with open("file2.txt") as file:
        f2 = file.read()
    
    f1 = f1.strip().split("\n")
    f2 = f2.strip().split("\n")
    
    result = [ int(n) for n in f1 if n in f2 ]
    # print(result)


    # Dictionary Comprehension
    names = [ "Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie" ]
    student_scores = {
        name:random.randint(1,100) for name in names
    }

    # print(student_scores)

    passed_students = {
        name:score for name, score in student_scores.items() if score >= 60
    }
    # print(passed_students)


    # words and there length
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    result = {
        word:len(word) for word in sentence.split()
    }
    # print(result)


    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }

    weather_f = {
        day:(9*temp/5)+32 for day,temp in weather_c.items()
    }
    # print(weather_f)

    student_dict = {
        "student": ["Angela", "James", "Lily"],
        "score": [56, 76, 98]
    }

    student_data_frame = pd.DataFrame(student_dict)

    # print(student_data_frame)

    # for key, value in student_data_frame.items():
        # print(value)

    for (index, row) in student_data_frame.iterrows():
        print(row.score)




if __name__ == '__main__':
    main()

