import random

def generate_test(data_path, result_path, num_choice):
    test_data = open(data_path, "r")
    questions = open(result_path, "w")

    # Initialize a capital dictionary
    capitals = {}

    # Read form test data and save to dictionary     
    for line in test_data:
        splitted = line.split(",")
        country = splitted[0]
        city = splitted[1].strip()
        capitals[country] = city   


    cities = list(capitals.values())

    for country in capitals.keys():

        # Write answer header
        questions.write(rf"{country},")

        # Write correct answer
        correct_city = capitals[country]
        questions.write(f"{correct_city}")

        # Separate answer part and question part by "*"
        # Format: [country], [correct_answer] * [choice1], [chioce2], [choice3], [choice4]
        questions.write("*")

        # Choose additional 3 wrong answer
        wrong_cities = cities.copy()
        wrong_cities.remove(correct_city)
        wrong_ans = random.sample(wrong_cities, num_choice - 1)

        # Combine into multiple choices
        ans_list = wrong_ans.copy()
        ans_list.append(correct_city)
        
        # Shuffle choice
        random.shuffle(ans_list)

        # Print out multiple choices:
        for choice in ans_list:
            questions.write(rf"{choice},")

        questions.write("\n")

        
    # Closing files
    test_data.close()
    questions.close()


def change_to_html(text):
    text = text.replace("\\n", "<br>")
    return text


def check_and_continue(choice, correct_choice):
    return choice == correct_choice



def get_question(questions_bank_path, question_num):
    with open(questions_bank_path) as questions:
        return questions.readlines()[question_num]

if __name__ == "__main__":
    number = 1

    # Get question data
    question = get_question("questions.txt", number)

    # Split question data into variables to add to 4 answer buttons
    # Question data format: [country], [correct_answer]*[choice1], [chioce2], [choice3], [choice4],
    splitted = question.split("*")
    country, correct_city = splitted[0].split(",")
    choices = splitted[1].strip().split(",")[0:-1]
    print(correct_city)
    