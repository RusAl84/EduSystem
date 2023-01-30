import json


def load_data():
    content = ""
    with open('data.json', 'r', encoding='utf-8') as f:
        content = f.read()
    # print(content)
    test_data = json.loads(content)
    return test_data


def get_question(test_data, num):
    str1 = test_data[num]['question1']
    answers = test_data[num]['answers']
    for answer in answers:
        num += 1
        str1 += f" {num} - {answer[0]}"
    str1 += "Введите номер верного ответа:"


if __name__ == '__main__':
    test_data = load_data()
    quest = test_data[0]
    print(quest["quest"])
    answers = quest["answers"]
    num = 0
    for answer in answers:
        num += 1
        print(f"{num} {answer[0]}")
    print("Введите номер верного ответа:")

    answer_num = int(input())-1

    if answer_num < 1 and answer_num > len(answers):
        print("Не правильно")
    elif answers[answer_num][1] == True:
        print("Правильно")
    else:
        print("Не правильно")
