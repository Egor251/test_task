import argparse
from main import Main

parser = argparse.ArgumentParser(description='Phonebook')
parser.add_argument('-a', '--action', help='possible arguments: list, search, add, change, remove', required=True)
parser.add_argument('-l', help='last name', default=None)
parser.add_argument('-f', help='first name', default=None)
parser.add_argument('-s', help='second name', default=None)
parser.add_argument('-o', help='organisation', default=None)
parser.add_argument('-d', help='home(domestic) phone', default=None)
parser.add_argument('-m', help='mobile phone', default=None)
parser.add_argument('-c', help='new value (Use only with "-a change")', default=None)

args = parser.parse_args()
last_name = args.l
first_name = args.f
second_name = args.s
organisation = args.o
home_phone = args.d
mobile_phone = args.m
change = args.c
args_list = [last_name, first_name, second_name,organisation, home_phone, mobile_phone]
if args.action == 'list':
    Main().list()
elif args.action == 'add':
    Main().add_line(args_list)
elif args.action == 'search':  # поиск по параметрам
    line = ''
    if last_name:
        line += f"(self.dataframe['last_name'] == '{last_name}' ) &"
    if first_name:
        line += f"(self.dataframe['first_name'] == '{first_name}' ) &"
    if second_name:
        line += f"(self.dataframe['second_name'] == '{second_name}' ) &"
    if organisation:
        line += f"(self.dataframe['organisation'] == '{organisation}' ) &"
    if home_phone:
        line += f"(self.dataframe['home_phone'] == '{home_phone}' ) &"
    if mobile_phone:
        line += f"(self.dataframe['mobile_phone'] == '{mobile_phone}' ) &"
    line = line[:-1]
    Main().search(line)
elif args.action == 'change':  # Изменение значения в записи
    for item in args_list:
        if item:
            print(item)
            Main().change(item, change)
elif args.action == 'remove':  # Удаление записи
    line = ''
    if last_name:
        line += f"(Main().dataframe['last_name'] == '{last_name}' ) &"
    if first_name:
        line += f"(Main().dataframe['first_name'] == '{first_name}' ) &"
    if second_name:
        line += f"(Main().dataframe['second_name'] == '{second_name}' ) &"
    if organisation:
        line += f"(Main().dataframe['organisation'] == '{organisation}' ) &"
    if home_phone:
        line += f"(Main().dataframe['home_phone'] == '{home_phone}' ) &"
    if mobile_phone:
        line += f"(Main().dataframe['mobile_phone'] == '{mobile_phone}' ) &"
    line = line[:-1]
    Main().remove(line)
else:
    print('Wrong argument -a')
print(args)



