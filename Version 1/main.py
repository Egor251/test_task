import pandas as pd


class Main:
    file = 'data.txt'
    dataframe = None  # послужит заменой БД, по условию задачи файл хранилище дложен быть текстовым и так удобней

    def __init__(self):
        self.dataframe = self.read_file()  # Сразу же записываем содержимое файла в dataframe

    def read_file(self):  # Стартовая операция, загружаем df из файла
        with open(self.file, encoding='UTF-8') as f:
            data = f.readlines()
            # временные списки для формирования DataFrame
            num = []
            last_name = []
            first_name = []
            second_name = []
            organisation = []
            home_phone = []
            mobile_phone = []
            # формирование DataFrame
            for line in data:
                pos = line.split(',,')
                last_name.append(pos[0])
                first_name.append(pos[1])
                second_name.append(pos[2])
                organisation.append(pos[3])
                home_phone.append(pos[4])
                mobile_phone.append(pos[5].replace('\n', ''))

            # Удобнее сначала подготовить dict, а потом формировать dataframe
            result_dict = {'last_name': last_name,
                           'first_name': first_name,
                           'second_name': second_name,
                           'organisation': organisation,
                           'home_phone': home_phone,
                           'mobile_phone': mobile_phone}

            result_data = pd.DataFrame(result_dict)

            #print(result_data)
        return result_data

    def write_file(self):  # записываем файл (будет выполняться при каждо действии)
        data = self.dataframe
        with open(self.file, 'w', encoding='UTF-8') as f:
            totalline = ''
            for i in range(len(data)):
                line = ''
                item = data.loc[i].values.tolist()
                for val in item:
                    line += val + ',,'
                line += '\n'
                totalline += line
            f.write(totalline)

    def add_line(self, line):  # Добавляем новую запись
        new_line = {'last_name': [line[0]],
                    'first_name': [line[1]],
                    'second_name': [line[2]],
                    'organisation': [line[3]],
                    'home_phone': [line[4]],
                    'mobile_phone': [line[5]]
                    }
        self.dataframe = pd.concat([self.dataframe, pd.DataFrame(new_line)], ignore_index=True)
        self.write_file()
        return 1

    def list(self):
        for i in range(len(self.dataframe)):
            print(self.dataframe.loc[i])

    def search(self, ask):
        # Возможно не самое удачное решение, зато элегантное
        res = eval(f"self.dataframe.loc[{ask}]")
        print(res)


if __name__ == '__main__':
    a = Main().read_file()

