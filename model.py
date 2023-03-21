"""
Alex Krysztofiak, Tien Dam, Jason Rosales
"""
import mesa

from scheduler import RandomActivationByTypeFiltered
from agents import *
import random



class TeamModel(mesa.Model):

    def __init__(
         self,
        width = 100,
        height = 100,
        density = .8,
        homophily = 3,
        
        initial_team_one = 50,
        initial_team_two = 50,
        initial_team_three = 50,
        initial_team_four = 50,

        density_team_one = .8,
        density_team_two = .8,
        density_team_three = .8,
        density_team_four = .8, 

        torus = True,
        moore = True

        
    ):

        super().__init__()
        #Set the parameters
        self.width = width
        self.height = height
        self.density = density
        self.homophily = homophily
        self.density_team_one = density_team_one
        self.density_team_two = density_team_two
        self.density_team_three = density_team_three
        self.density_team_four = density_team_four

        #These are initial densities of the groups
        self.initial_team_one = initial_team_one
        self.initial_team_two = initial_team_two
        self.initial_team_three = initial_team_three
        self.initial_team_four = initial_team_four

        self.torus= torus
        self.moore = moore

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, torus)

        self.happy = 0
        self.datacollector = mesa.DataCollector(
            {"happy": "happy"},  # Model-level count of happy agents
            # For testing purposes, agent's individual x and y
            {"x": lambda a: a.pos[0], "y": lambda a: a.pos[1]},
        )


        #======================================
        #
        #
        #put agents down
        #This works decently well
        """for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if self.random.random() < self.density:
                if self.random.random() < self.density_team_one:
                    agent_type = 1
                if self.random.random() < self.density_team_two:
                    agent_type = 2
                if self.random.random() < self.density_team_three:
                    agent_type = 3
                if self.random.random() < self.density_team_four:
                    agent_type = 4
                
            #unique_id, pos, model, agent_type, moore=moore
                agent = Group_one((x, y), self, agent_type, homophily, True)
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)"""
        #
        #
        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if self.random.random() < self.density:
                agent_type = random.randint(0,4)

                agent = Group_one((x, y), self, agent_type, homophily, moore)
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)
        #
        #
        """for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if self.random.random() < self.density:
                for i in range(self.initial_team_one):
                    if self.random.random() < self.density_team_one:
                        agent_type = 1
                for i in range(self.initial_team_two):
                    if self.random.random() < self.density_team_two:
                        agent_type = 2
                for i in range(self.initial_team_three):
                    if self.random.random() < self.density_team_three:
                        agent_type = 3
                for i in range(self.initial_team_four):
                    if self.random.random() < self.density_team_four:
                        agent_type = 4
 

                
            #unique_id, pos, model, agent_type, moore=moore
                agent = Group_one((x, y), self, agent_type, homophily, True)
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)   """
        #
        #===========================================



        self.running = True
        self.datacollector.collect(self)

    def step(self):
        """
        Run one step of the model. If All agents are happy, halt the model.
        """
        self.happy = 0  # Reset counter of happy agents
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

        if self.happy == self.schedule.get_agent_count():
            self.running = False