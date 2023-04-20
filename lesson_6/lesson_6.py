import re

text = 'AV Analytics Vidhya AV'

result = re.match(r'AV', text)
# print(result)


result = re.match(r'Analytics', text)
# print(result)


result = re.search(r'Analytics', text)
# print(result)


result = re.findall(r'AV', text)
# print(result)


result = re.findall(r'A[a-zA-Z]', text)
# print(result)


result = re.split(r' ', text)
# print(result)


result = re.sub(r' ', ':', text)
# print(result)


result = re.sub(r'[Aai]', 'hello', text)
# print(result)

# (0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(1[0-9]{3}|20[0-2][0-9])

with open('lesson_6/test_regs.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    # print(content)

    beeline_list = re.findall(r"\+996 (?:77\d|22\d)[ \d]{9}", content)
    print(beeline_list)

    megacom_list = re.findall(r"\+996 (?:55\d|99\d|75\d)[ \d]{9}", content)
    print(megacom_list)

    nur_telecom_list = re.findall(r"\+996 (?:50\d|70\d)[ \d]{9}", content)
    print(nur_telecom_list)

    # fruit_list = re.findall(r'fruits\[\d+\] = [а-я"";]+', content)
    # for fruit in fruit_list:
    #     print(fruit)
