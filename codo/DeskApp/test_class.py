class MyList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def count_space(self):
        return self.count(" ")


text = list(" 23 sdf")
print(text.count(" "))

text2 = MyList(" 23 sdf")
print(text2.count_space())

print(text, text2)