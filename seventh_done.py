class Animal:
    num = 0
    def __init__(self, name, sound='не знаю что'):
        self.name = name
        self.sound = sound
        Animal.num = Animal.num + 1

    def voice(self):
        pass

    @staticmethod
    def printNum():
        print("Количество животных - ", Animal.num)

class Dog(Animal):
    def voice(self):
        print('%s делает %s' % (self.name, self.sound))


class Sova(Animal):
    def voice(self):
        print('%s делает %s' % (self.name, self.sound))


class Lev(Animal):
    def __init__(self, name, sound = 'не знаю что'):
        Animal.__init__(self, name, 'АаАаАаАаАаА')

    def voice(self):
        print('Хочте я вам покажу як %s рычит - %s' % (self.name, self.sound))


dog = Dog('Собака', 'гав-гва')
dog.voice()

sova = Sova('Сова', 'уу-уу')
sova.voice()

lev = Lev('Лев')
lev.voice()

Animal.printNum()
