class Team:
    def __init__(self, name, team, toleration, leftNeighbor, rightNeighbor, topNeighbor, bottomNeighbor, isValid):
        self.name = name
        self.team = team
        self.toleration = toleration
        self.leftNeighbor = leftNeighbor
        self.rightNeighbor = rightNeighbor
        self.topNeighbor = topNeighbor
        self.bottomNeighbor = bottomNeighbor
        self.isValid = isValid
    def __str__(self):
        return f"{self.name}({self.toleration})"   

Team1 = Team("Eagles", 10)
Team2 = Team("Giants", 17)

print(Team1, Team2)
print("Input name, toleration, other stuff")
