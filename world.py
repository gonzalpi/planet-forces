import pandas as pd
# from time import strptime
from cmath import pi, exp as e

# Import properties
properties = pd.read_csv("data/properties_normalized.csv")
# properties.Date = properties.Date.apply(lambda x: strptime(x, "%Y-%m-%d")[0:3])

# Create data frame with initial positions
world = pd.DataFrame()
world["Date"] = [properties["Date"][0]] # assuming all dates are the same
for planet in properties["Planet"]:
    if planet=="Sun": continue  # skip Sun as it's at origin
    r = properties["OrbitalRadius(AU)"][properties["Planet"]==planet].to_numpy()[0]
    ang = properties["Rotation"][properties["Planet"]==planet].to_numpy()[0]
    pos = r * e(ang * 1j)
    world["x" + planet] = [pos.imag]
    world["y" + planet] = [pos.real]
    # Adjust position so Moon revolves around Earth
    if planet=="Moon":
        world["x" + planet] += world["xEarth"]
        world["y" + planet] += world["yEarth"]