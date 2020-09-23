
class Signal:

    def connect(self, fn):
        self.fn = fn

    def emit(self, *args, **kwargs):
        self.fn(*args, **kwargs)


class Actions:

    eat_signal = Signal()
    pee_signal = Signal()

    @property
    def eating(self):
        return self.eat_signal

    @property
    def peeing(self):
        return self.pee_signal


class Person(Actions):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def send_signal(self, signal_type):
        fn = getattr(self, signal_type).emit()

    def eat(self):
        # self.eating.emit()  # works
        self.send_signal('eating')
        return self

    def pee(self):
        self.peeing.emit()
        return self


def on_eat(*args, **kwargs):
    print('Eating on progress')


def on_peeing(*args, **kwargs):
    print('Peeing on progress')

if __name__ == '__main__':
    person = Person('Brent Jeffson Florendo', 21)
    person.eating.connect(lambda : on_eat(on_eat=True))
    person.peeing.connect(lambda : on_peeing(on_pee=True))
    person.eat()

















