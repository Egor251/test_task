import pandas as pd


class Main:
    file = 'data.csv'
    dataframe = None  # послужит заменой БД, по условию задачи файл хранилище дложен быть текстовым и так удобней

    def __init__(self):
        self.dataframe = self.read_file()  # Сразу же записываем содержимое файла в dataframe

    def read_file(self):  # Стартовая операция, загружаем df из файла

        result_data = pd.read_csv(self.file, delimiter=',')
        return result_data

    def write_file(self):  # записываем файл (будет выполняться при каждо действии)
        self.dataframe.to_csv(self.file)

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
    Main().write_file()
    print(a)
