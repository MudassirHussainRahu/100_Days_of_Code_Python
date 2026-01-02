# from question_model import Question

import requests

def get_data(amount=10, category=18, difficulty="easy", type="boolean"):
    url = "https://opentdb.com/api.php"
    parameters = {
        "amount":amount,
        "category": category,
        "difficulty":difficulty,
        "type":type
    }
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["results"]


# if __name__=="__main__":
#     data = get_data()

#     print(data)

# data = [
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'The first IBM PC was released in 1981.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, 
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'The logo for Snapchat is a Bell.', 'correct_answer': 'False', 'incorrect_answers': ['True']},
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'Pointers were not used in the original C programming language; they were added later on in C++.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, 
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'A Mac is not a PC', 'correct_answer': 'False', 'incorrect_answers': ['True']}, 
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'The Windows 7 operating system has six main editions.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, 
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, 
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'Linux was first created as an alternative to Windows XP.', 'correct_answer': 'False', 'incorrect_answers': ['True']}, 
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'RAM stands for Random Access Memory.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, 
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'Ada Lovelace is often considered the first computer programmer.', 'correct_answer': 'True', 'incorrect_answers': ['False']}, 
#     {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;', 'correct_answer': 'True', 'incorrect_answers': ['False']}
#     ]

# question_list = []

# for question in data:
#     question_text = question["question"]
#     q_answer = question["correct_answer"]
#     q = Question(question_text, q_answer)
#     question_list.append(q)
