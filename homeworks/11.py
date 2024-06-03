class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def code(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'E'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'F':
            self.state = 'C'
            return 10
        if self.state == 'G':
            self.state = 'H'
            return 11
        raise MealyError('code')

    def file(self):
        if self.state == 'A':
            self.state = 'G'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'G'
            return 5
        if self.state == 'F':
            self.state = 'G'
            return 8
        raise MealyError('file')

    def chalk(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'F':
            self.state = 'A'
            return 9
        raise MealyError('chalk')


def main():
    return StateMachine()


def raises(function, error):
    output = None
    try:
        output = function()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.code() == 0
    assert o.file() == 2
    assert o.chalk() == 3
    assert o.code() == 6
    assert o.chalk() == 7
    assert o.code() == 10
    assert o.code() == 4
    assert o.chalk() == 7
    assert o.chalk() == 9
    assert o.file() == 1
    assert o.code() == 11
    raises(lambda: o.file(), MealyError)
    raises(lambda: o.chalk(), MealyError)
    raises(lambda: o.code(), MealyError)

    o = main()
    assert o.code() == 0
    assert o.file() == 2
    assert o.code() == 4
    assert o.chalk() == 7
    assert o.file() == 8

    o = main()
    assert o.code() == 0
    assert o.file() == 2
    assert o.file() == 5


test()