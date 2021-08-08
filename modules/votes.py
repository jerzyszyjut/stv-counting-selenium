def fileLength(fname):
    with open(fname, encoding='utf-8') as f:
        for i, l in enumerate(f):
            pass
    return i


class Votes:
    file = ''
    path = ''

    votes = []
    codes = {}
    candidates = []

    def __init__(self, path):
        self.path = path
        self.file = open(path, 'r', encoding='utf-8')
        self.file.readline()  # Pops header

        self.readVotes()
        self.getCandidates()

        self.checkVotes()

    def __del__(self):
        self.file.close()

    def readVotes(self):
        for i in range(fileLength(self.path)):
            line = self.file.readline()
            if '\n' in line:
                line = line.replace('\n', '')
            line = line.replace('"', '')
            line = line.split(',')

            self.codes[line[2]] = line[1]
            self.votes.append(line[3:])

    def getCandidates(self):
        for i in self.votes:
            for j in i:
                if (j not in self.candidates) and not j == '':
                    self.candidates.append(j)

    def checkVotes(self):
        for i in range(len(self.votes)):
            seen = []
            for j in self.votes[i]:
                if j in seen:
                    print(f'Vote no. {i} is not valid!')
                    seen.append(j)
