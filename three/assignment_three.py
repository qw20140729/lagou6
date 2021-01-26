

class Animal(object):
    name = ''
    color = ''
    age = 1
    sex = ''
    def cry(self):
        print(f'动物{self.name}会叫...')

    def run(self):
        print(f'动物{self.name}会跑...')

class Cat(Animal):
    def __init__(self, hair):
        super().__init__(self)
        self.hair = hair

    def clutch(self):
        print('猫会捉老鼠...')

    def cry(self):
        print('喵喵叫...')
        


