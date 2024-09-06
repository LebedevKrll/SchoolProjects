

'''RoundRobin prints tournament tables using Round Robin algorithm.
Works in Russian. I developed this long ago, dont want to write comments to this one'''

from copy import deepcopy

class Round_Robin:
    def __init__(self, teams, rounds=1, justice=False):
        self.teams = teams
        self.rounds = rounds
        self.justice = justice
        self.justice_num = 0

    def scheduling(self):
        ans = []
        if self.teams % 2 == 0:
            if self.teams == 2 and self.rounds > 1 and self.justice == True:
                for i in range(self.rounds):
                    ans.append([1])
                    ans.append([2])
                    ans.append("конец дня")
                    ans.append([2])
                    ans.append([1])
                    ans.append("конец дня")
                return ans[: (self.rounds * 3)]
            else:
                list_of_teams = self.Rowing()
                team1 = list_of_teams [0 : self.teams // 2]
                opponents = list_of_teams [self.teams // 2 :]
                for i in range (self.rounds):
                    for j in range(self.teams - 1):
                        ans.append(deepcopy(team1))
                        ans.append(deepcopy(opponents))
                        ans.append("конец дня")
                        rotated = self.Rotating(team1, opponents)
                        team1 = rotated [0 : self.teams // 2]
                        opponents = rotated [self.teams // 2 :]
        else:
            list_of_teams = self.Rowing()
            team1 = list_of_teams [0 : self.teams // 2 + 1]
            opponents = list_of_teams [self.teams // 2 + 1 :]
            for i in range (self.rounds):
                for j in range(self.teams):
                    ans.append(deepcopy(team1))
                    ans.append(deepcopy(opponents))
                    ans.append("конец дня")
                    rotated = self.Rotating(team1, opponents)
                    team1 = rotated [0 : self.teams // 2 + 1]
                    opponents = rotated [self.teams // 2 + 1 :]
        return ans

    def Rowing(self):
        l1 = []
        for i in range(self.teams):
            l1.append(i + 1)
        if self.teams % 2 == 1:
            l1.append('-')
        return l1

    def Rotating(self, Row1, Row2):
        if self.teams == 2:
            pass
        else:
            if self.teams % 2 == 0:
                if self.justice == True and self.justice_num % 2 == 1:
                    Row2[0] = Row1[0]
                    Row1[0] = 1
                last_Row1_elem = Row1[self.teams // 2 - 1]
                x = 2
                for i in range(self.teams // 2 - 2):
                    Row1[x] = Row1[x - 1]
                    x += 1
                x = 0
                Row1[1] = Row2[0]
                for i in range(self.teams // 2 - 1):
                    Row2[x] = Row2[x + 1]
                    x += 1
                Row2 [self.teams // 2 - 1] = last_Row1_elem
                if self.justice == True and self.justice_num % 2 == 0:
                    Row1[0] = Row2[0]
                    Row2[0] = 1
            else:
                if self.justice == True and self.justice_num % 2 == 1:
                    Row2[0] = Row1[0]
                    Row1[0] = 1
                last_Row1_elem = Row1[self.teams // 2]
                x = 2
                for i in range(self.teams // 2 - 1):
                    Row1[x] = Row1[x - 1]
                    x += 1
                x = 0
                Row1[1] = Row2[0]
                for i in range(self.teams // 2):
                    Row2[x] = Row2[x + 1]
                    x += 1
                Row2 [self.teams // 2] = last_Row1_elem
                if self.justice == True and self.justice_num % 2 == 0:
                    Row1[0] = Row2[0]
                    Row2[0] = 1
            self.justice_num += 1
        return Row1 + Row2


