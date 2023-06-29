class Animal:
    def __init__ (self, name, sound = None):
        self.name = name
        self.sound = sound
    def voice(self):
        pass

class Dog(Animal):
    def __init__ (self, name, sound = None):
        Animal.__init__(self, name, 'гав-гав')
    def voice(self):
        print('%s делает %s' % (self.name, self.sound))

class Sova(Animal):
    def __init__ (self, name, sound = None):
        Animal.__init__(self, name, 'уу-уу')
    def voice(self):
        print('%s делает %s' % (self.name, self.sound))

class Lev(Animal):
    def __init__ (self, name, sound = None):
        Animal.__init__(self, name, 'АаАаАаАаАаА')
    def voice(self):
        print('Хочте я вам покажу як %s рычит - %s' % (self.name, self.sound))


dog = Dog('Собака')
dog.voice()

sova = Sova('Сова')
sova.voice()

lev = Lev('Лев')
lev.voice()
