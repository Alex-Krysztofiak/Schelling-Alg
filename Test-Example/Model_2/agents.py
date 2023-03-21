"""
Alex Krysztofiak, Tien Dam, Jason Rosales
"""
"""
=====================

There is 4 different types of Agents for 4 different football teams.
Each class is a seperate  team, this allows for teams to have different amount of fans as well as different variables for how many neighbors tgey need to be happy

"""

import mesa

from walker import RandomWalker 
"""Also import the other types of sorting"""
walkerModel = RandomWalker
#RandomWalker is a mesa.Agent so it will 

class Group_one(mesa.Agent):

    TEAM = [1,2,3,4]
    moore = True

    def __init__(self, pos, model, agent_type, homophily, moore):
        super().__init__(pos, model)
        self.pos = pos
        self.type = agent_type
        self.homophily = homophily
        self.moore = moore

   
    def step(self):
        similar = 0
        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.type == self.type:
                similar += 1

        # If unhappy, move:
        if similar < self.homophily:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1
""" 
class Group_two(mesa.Agent):
    def __init__(self, unique_id, pos, model, agent_type, homophily, moore):
        super().__init__(unique_id, pos, model, agent_type, moore=moore)
        self.pos = pos
        self.type = agent_type
        self.homophily = homophily


    def step(self):
        similar = 0
        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.type == self.type:
                similar += 1

        # If unhappy, move:
        if similar < self.homophily:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1


class Group_three(mesa.Agent):
    def __init__(self, unique_id, pos, model, agent_type, homophily, moore):
        super().__init__(unique_id, pos, model, agent_type, moore=moore)
        self.pos = pos
        self.type = agent_type
        self.homophily = homophily

    def step(self):
        similar = 0
        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.type == self.type:
                similar += 1

        # If unhappy, move:
        if similar < self.homophily:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1

class Group_four(mesa.Agent):
    def __init__(self, unique_id, pos, model, agent_type, homophily, moore):
        super().__init__(unique_id, pos, model, agent_type, moore=moore)
        self.pos = pos
        self.type = agent_type
        self.homophily = homophily


    def step(self):
        similar = 0
        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.type == self.type:
                similar += 1

        # If unhappy, move:
        if similar < self.homophily:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1

 """