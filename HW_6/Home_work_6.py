import json
import csv

"""
Task 1
Encodings
"""
# cod_val_1 = b'r\xc3\xa9sum\xc3\xa9'
#
# decod_val_2 = cod_val_1.decode()
# print(decod_val_2)
#
# cod_val_2 = decod_val_2.encode("latin1")
# print(cod_val_2)
#
# decod_val_3 = cod_val_2.decode("latin1")
# print(decod_val_3)


"""
Task 2
Enter 4 lines to save 4 different variables.
Create a file and write 2 lines to it, close the file.
Then open and add the 2nd remaining.
As a result, 4 lines should start with a new line.
"""
# str_1 = input('Введите первую строку: ')
# str_2 = input('Введите вторую строку: ')
# str_3 = input('Введите третью строку: ')
# str_4 = input('Введите четвертую строку: ')
# file_name = open('text_hw_2.txt', 'w')
# file_name.write(str_1 + '\n' + str_2 + '\n')
# file_name.close()
# file_name = open('text_hw_2.txt', 'a')
# file_name.write(str_3 + '\n' + str_4)
# file_name.close()


"""
Task 3/4
Create a dictionary with a 6-digit number (id) as the key,
and a tuple consisting of 2 elements as values - name(str), age(int).
Make about 5-6 dictionary elements. Write this dictionary to disk in a json file.
"""

data = {
    100001: ('Oleg', 25),
    100002: ('Dime', 19),
    100003: ('Valodya', 36),
    100004: ('Vasilisa', 29),
    100005: ('Petr', 23),
    100006: ('Kostya', 28),
}
# writing data to a JSON file
with open('id_people.json', 'w') as file:
    json.dump(data, file, indent=4)

# reading a JSON file
with open('id_people.json', 'r') as file:
    data_new_json = json.load(file)
    print(data_new_json)

# writing to a CSV file
with open('file.csv', 'w', encoding='utf-8') as file:
    cols = ['id', 'name', 'age', 'phone']
    csv_file = csv.DictWriter(
        file,
        delimiter=',',
        fieldnames=cols)

    csv_file.writeheader()
    csv_file.writerow(
        {
            cols[0]: 100001,
            cols[1]: data_new_json.get('100001')[0],
            cols[2]: data_new_json.get('100001')[1],
            cols[3]: 375294561278
        }
    )

    csv_file.writerow(
        {
            cols[0]: 100002,
            cols[1]: data_new_json.get('100002')[0],
            cols[2]: data_new_json.get('100002')[1],
            cols[3]: 375299876542
        }
    )

    csv_file.writerow(
        {
            cols[0]: 100003,
            cols[1]: data_new_json.get('100003')[0],
            cols[2]: data_new_json.get('100003')[1],
            cols[3]: 375291234578
        }
    )

    csv_file.writerow(
        {
            cols[0]: 100004,
            cols[1]: data_new_json.get('100004')[0],
            cols[2]: data_new_json.get('100004')[1],
            cols[3]: 375293456782
        }
    )

    csv_file.writerow(
        {
            cols[0]: 100005,
            cols[1]: data_new_json.get('100005')[0],
            cols[2]: data_new_json.get('100005')[1],
            cols[3]: 375293645212
        }
    )

    csv_file.writerow(
        {
            cols[0]: 100006,
            cols[1]: data_new_json.get('100006')[0],
            cols[2]: data_new_json.get('100006')[1],
            cols[3]: 375294856123
        }
    )
