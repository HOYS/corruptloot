import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load rclc loot from json export
loot = pd.read_json('jruegloot.json')

# Clear some random trash we dont care about looking at
loot = loot[loot.response != "Banking"]
loot = loot[loot.response != "Disenchant"]
loot = loot[loot.response != "Greed/OS"]
loot = loot[loot.response != "Offspec"]

# filter to only aq40
loot = loot[loot.instance == "Ahn'Qiraj Temple-40 Player"]

# rmeove server name suffix
loot['player'] = loot['player'].str.replace('-Herod', '')

# convert date field to pandas date time
loot['date'] = pd.to_datetime(loot['date'])


# Define some times
start = pd.to_datetime('2020-7-29')
end = pd.to_datetime('2022-7-29')
start_remove = pd.to_datetime('1990-7-29')

# mask the data frame with times
mask = (loot['date'] > start) & (loot['date'] <= end)

# filter data frame based on mask conditions
loot = loot.loc[mask]

# plot it
pd.value_counts(loot['player']).plot.bar()

# show it
plt.show()