class ThreeMethods:

    def __init__(self, text):
        self.text = text

    def dictionary_list(self):
        dicts_text = {}
        for i in self.text:
            dicts_text.update({i: 1})
        print(dicts_text)

    def set_list(self, set_text):
        self.text = set_text
        set_text = set(set_text)
        str_text = ""
        for i in set_text:
            str_text += i
        print(str_text)

    def text_list(self, text):
        self.text = text
        text = list(text)
        # set_text = set(set_text)
        str_text = ""
        for i in text.copy():
            if text.count(i) > 1:
                text.remove(i)
            else:
                str_text += i
        print(str_text)

    def dict_values(self, values_3):
        self.text = values_3
        x = []
        for i in values_3.items():
            x.append(i)
            x.sort(reverse=True)
            for j in x:
                if x.index(j) > 2:
                    x.remove(j)
        values_3 = dict(x)
        print(values_3)


car_1 = ThreeMethods("python")
car_1.dictionary_list()
k = {1: 1, 8: 8, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 24: 24}
car_1.dict_values(k)
car_1.set_list("HelloArmenia")
car_1.text_list("HelloArmenia")

