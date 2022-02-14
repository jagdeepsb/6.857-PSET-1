import numpy as np
from table import Table

class CipherText():
    def __init__(self, percent):
        with open('cipher.txt') as f:
            lines = f.readlines()
                    
        self.cipher = []        
        for i, line in enumerate(lines):
            numbers = line[:-1].split(' ')
            for number in numbers:
                self.cipher.append(int(number))
        
        length = max(32, int(len(self.cipher)*percent))
        self.cipher = self.cipher[0:length]

    def length(self,):
        return len(self.cipher)
        
    def __getitem__ (self, index):
        return self.cipher[index]

class Solver():
    def __init__(self,):

        self.cipher = CipherText(1.0)

    def decode(self, key):
        
        table = Table()
        m = []
        for i, c_i in enumerate(self.cipher):
            m_i = table.decrypt(key[i%32], c_i)
            m.append(m_i)
        return m
    def decode_and_print(self, key):

        m = self.decode(key)

        chars = "abcdefghijklmnopqrstuvwxyz .,!?\n"
        m_alpha = []
        for m_i in m:
            m_alpha_i = chars[m_i]
            m_alpha.append(m_alpha_i)

        for i, letter in enumerate(m_alpha):
            print(f'{letter} ({i%32})  ', end='')

    def decode_and_print_all(self, key):

        m = self.decode(key)

        chars = "abcdefghijklmnopqrstuvwxyz .,!?\n"
        m_alpha = []
        for m_i in m:
            m_alpha_i = chars[m_i]
            m_alpha.append(m_alpha_i)

        for i, letter in enumerate(m_alpha):
            print(letter, end='')

if __name__ == "__main__":
    solver = Solver()

    # key = [7, 22, 0, 24, 7, 7, 17, 3, 15, 27, 12, 10, 31, 16, 16, 0, 16, 2, 31, 25, 21, 16, 4, 31, 29, 31, 3, 1, 31, 4, 11, 18]
    key = [24, 9, 13, 7, 24, 24, 5, 6, 18, 25, 5, 29, 2, 25, 21, 2, 25, 0, 1, 17, 26, 30, 8, 22, 17, 22, 6, 11, 22, 8, 1, 19]
    solver.decode_and_print_all(key)
