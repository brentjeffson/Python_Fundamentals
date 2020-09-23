class OnActionListener:

    def onEat(self, food):
        pass

    def onSleep(self, seconds):
        pass


class Person:

    def __init__(self):
        self._listener = None

    def rest(self):
        if self._listener is not None:
            self._listener.onSleep(2000)
        return self

    def eat(self):
        food = 'Banana'
        if self._listener is not None:
            self._listener.onEat(food)
        else:
            print('No Listener')
        return self

    def setListener(self, listener):
        self._listener = listener
        return self


class OnPersonListener(OnActionListener):

    def onEat(self, food):
        print(f'Eating {food}')

    def onSleep(self, seconds):
        print(f'Sleeping for {seconds}s')


if __name__ == '__main__':
    person = Person()

    onActionListener = OnActionListener()

    onActionListener.onEat = lambda food: {
        print(1),
        print(food),
        print(2),
        print(3)
    }


    person.setListener(onActionListener)
    person.eat().rest()