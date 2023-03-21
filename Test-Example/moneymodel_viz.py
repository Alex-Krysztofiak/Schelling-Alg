from moneymodel import *
import numpy as np
import mesa
from mesa.visualization.ModularVisualization import VisualizationElement, CHART_JS_FILE

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.wealth > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    return portrayal




grid = mesa.visualization.CanvasGrid(agent_portrayal, 25, 25, 500, 500)
server = mesa.visualization.ModularServer(
    MoneyModel, [grid], "Money Model", {"N": 100, "width": 25, "height": 25}
)



server.port = 8521 # The default
server.launch()