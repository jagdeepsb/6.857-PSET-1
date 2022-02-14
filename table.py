import numpy as  np



class Table():
    def __init__(self,):

        with open('table.txt') as f:
            lines = f.readlines()
            
        NUM_ELS = 32
        self.table = np.zeros((NUM_ELS, NUM_ELS), dtype=np.int32)
        for i, line in enumerate(lines):
            numbers = line[:-1].split(' ')
            for j, number in enumerate(numbers):
                self.table[i][j] = int(number)


        self.inverse_table =  np.zeros((NUM_ELS, NUM_ELS), dtype=np.int32)
        for i in range(NUM_ELS):
            for j in range(NUM_ELS):
                value = int(self.table[i][j])
                self.inverse_table[i][value] = j

    def encrypt(self, k, m):
        return self.table[k][m]

    def decrypt(self, k, c):
        return self.inverse_table[k][c]


if __name__ == "__main__":
    table = Table()
    k = [1,2,3,4,5,6]
    m = [1,2,3,4,5,6]
    c = []
    m_back = []
    for i in range(len(k)):
        c.append(table.encrypt(k[i], m[i]))
        m_back.append(table.decrypt(k[i], c[-1]))
    print(c)
    print(m)
    print(m_back)
