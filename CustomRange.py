

'''This module consists of class CustomRange
It does the same thing as built in python function range()'''

import math


class CustomRange:
    '''custom range that works the same way as original one'''
    def __init__(self, *args):
        for i in args:
            if type(i) is not int:
                raise TypeError(f'\'{type(i).__name__}\' \
object cannot be interpreted as an integer')
        if len(args) < 1:
            raise TypeError('range expected 1 arguments, got 0')
        if len(args) > 3:
            raise TypeError(
                f'range expected at most 3 arguments, got {len(args)}'
            )
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        if len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        if len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1

    def count(self, value):
        '''counts how many times the value is in the Range'''
        if value in self:
            return 1
        return 0

    def index(self, key):
        '''founds the index of the value in Range'''
        if key in self:
            return int((key - self.start) / self.step)
        raise ValueError(f'{key} is not in range')

    def __str__(self):
        '''makes your Range type string'''
        return self.__repr__()

    def __repr__(self) -> str:
        '''allows you to print your Range'''
        if self.step == 1:
            return f'range({self.start}, {self.stop})'
        return f'range({self.start}, {self.stop}, {self.step})'

    def __len__(self) -> int:
        '''counts the amount of elements in your Range'''
        if self.stop < self.start and self.step > 0 or self.stop > self.start and self.step < 0:
            return 0
        return math.ceil((self.stop - self.start) / self.step)

    def __contains__(self, other) -> bool:
        '''checks if value is in Range'''
        if (other - self.start) % self.step != 0:
            return False
        if self.stop > self.start:
            if self.start <= other < self.stop:
                return True
            return False
        if self.stop < other <= self.start:
            return True
        return False

    def __getitem__(self, index) -> int:
        '''returns item on the index'''
        try:
            if type(index) != int:
                raise TypeError(f'range indices \
must be integers or slices, not {type(index).__name__}')
            if abs(index) > len(self):
                raise IndexError('range object index out of range')
            if index < 0:
                index += len(self)
            return self.start + self.step * index
        except TypeError:
            raise TypeError(f'range indices \
must be integers or slices, not {type(index).__name__}')

    def __iter__(self):
        return Iter(self.start, self.stop, self.step)


class Iter:
    '''Help custom range become an iterable object'''
    def __init__(self, start, stop, step):
        self.stop = stop
        self.step = step
        self.start = self.current = start

    def __iter__(self):
        '''iterates'''
        return self

    def __next__(self):
        '''returns next value for iterator'''
        if self.stop > self.start and self.step > 0:
            if self.current >= self.stop:
                self.current = self.start
                raise StopIteration
        else:
            if self.current <= self.stop:
                print(self.stop, self.start, self.step, self.current)
                self.current = self.start
                raise StopIteration
        ans = self.current
        self.current += self.step
        return ans

