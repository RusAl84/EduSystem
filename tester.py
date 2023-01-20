import json
content = ""
with open('data.json', 'r', encoding='utf-8') as f:
    content = f.read()
print(content)
data = json.loads(content)
quest = data[0]
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
elif answers[answer_num][1] == 1:
    print("Правильно")
else:
    print("Не правильно")
