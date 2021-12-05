class StringCheck(str):
    def __init__(self, string):
        self.string = string

    def repeat_check(self, s):
        self.s = s
        if type(self.s) != str:
            return False
        if len(self.s) == 0:
            return False
        n = []
        for i in self.string:
            if i not in n:
                n.append(i)
        n = ''.join(n)
        d = len(n)
        if n == self.s[-d:]:
            return True
        else:
            return False

    def palindrom_check(self):
        self.string = self.string.lower().replace(' ', '')
        s2 = ''
        z = 0
        while z < len(self.string):
            s2 += self.string[-z - 1]
            z += 1
        if s2 == self.string:
            return True
        else:
            return False


while True:
    string = StringCheck(input("Введіть рядок: "))
    print("Перевірка на повторення:", string.repeat_check(input("Введіть елемент для перевірки: ")))
    print("Перевірка на паліндром:", string.palindrom_check())