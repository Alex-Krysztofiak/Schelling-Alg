"""
Alex Krysztofiak, Tien Dam, Jason Rosales
"""
import mesa
from agents import Group_one

from model import TeamModel


def get_happy_agents(model):
    """
    Display a text count of how many happy agents there are.
    """
    return f"Happy agents: {model.happy}"


def draw(agent):
    """
    Portrayal Method for canvas
    """
    if agent is None:
        return
    if agent.type == 0:
        return
    portrayal = {"Shape": "rect", "w": .7, "h": .7, "Filled": "true", "Layer": 0}

    if agent.type == 1:
        #red
        portrayal["Color"] = ["#FF0000", "#FF0000"]
        portrayal["stroke_color"] = "#00FF00"
    if agent.type == 2:
        #blue
        portrayal["Color"] = ["#0000FF", "#0000FF"]
        portrayal["stroke_color"] = "#001292"
    if agent.type == 3:
        #green
        portrayal["Color"] = ["#23D523", "#23D523"]
        portrayal["stroke_color"] = "#207620"
    if agent.type == 4:
        #purple
        portrayal["Color"] = ["#412076", "#412076"]
        portrayal["stroke_color"] = "#350A7A"
    return portrayal

model_params = {
    "height": mesa.visualization.Slider("Height", 70, 10, 70, 10),
    "width": mesa.visualization.Slider("Width", 70, 10, 70, 10),
    "density": mesa.visualization.Slider("Agent density", 0.8, 0.1, 0.9, 0.1),
    "homophily": mesa.visualization.Slider("Homophily", 3, 1, 8, 1),
    #"density_team_one": mesa.visualization.Slider("Agent 1 density", 0.8, 0.1, 1.0, 0.1),
    #"density_team_two": mesa.visualization.Slider("Agent 2 density", 0.8, 0.1, 1.0, 0.1),
    #"density_team_three": mesa.visualization.Slider("Agent 3 density", 0.8, 0.1, 1.0, 0.1),
    #"density_team_four": mesa.visualization.Slider("Agent 4 density", 0.8, 0.1, 1.0, 0.1),
    "torus": mesa.visualization.Checkbox("torus", True),
    "moore": mesa.visualization.Checkbox("moore", True),
}
canvas_element = mesa.visualization.CanvasGrid(draw, 70, 70, 700, 700)
happy_chart = mesa.visualization.ChartModule([{"Label": "happy", "Color": "Black"}])



server = mesa.visualization.ModularServer(TeamModel,[canvas_element, get_happy_agents, happy_chart], "Team", model_params,)