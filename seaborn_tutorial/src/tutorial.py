#Creates graphs and formats CSV file containing pokemon data using pandas and
#Seaborn for graphing
# Pandas for managing datasets
import pandas as pd
from matplotlib import pyplot as plt
# Seaborn for plotting and styling
import seaborn as sns
# Read dataset , index_col=0
df = pd.read_csv('../data/Pokemon.csv', index_col=0)
#pokemon colors to color data on graph
pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                    ]

# Display first 5 observations
# print(df.head())

# Recommended way
sns.lmplot(x="Attack", y="Defense", data=df).fig.show()
# Alternative way
# sns.lmplot(x=df.Attack, y=df.Defense)
# Scatterplot arguments
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, # No regression line
           hue='Stage')   # Color by evolution stage
# Tweak using Matplotlib
plt.ylim(0, None)
plt.xlim(0, None)
# Boxplot
# sns.boxplot(data=df)
# Pre-format DataFrame
stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
 
# New boxplot using stats_df
# sns.boxplot(data=stats_df)
# Set theme
sns.set_style('whitegrid')
#graph to show variance between pokemon defence/attack based on type
# Violin plot with Pokemon color palette
sns.violinplot(x='Type 1', y='Attack', data=df,
               palette=pkmn_type_colors)  # Set color palette

# Swarm plot with Pokemon color palette
sns.swarmplot(x='Type 1', y='Attack', data=df,
              palette=pkmn_type_colors)
#Creating violin plot with swarm plot within it for better visualization
# Set figure size with matplotlib
plt.figure(figsize=(10, 6))

# Create plot
sns.violinplot(x='Type 1',
               y='Attack',
               data=df,
               inner=None,  # Remove the bars inside the violins
               palette=pkmn_type_colors)

sns.swarmplot(x='Type 1',
              y='Attack',
              data=df,
              color='k',  # Make points black
              alpha=0.7)  # and slightly transparent

# Set title with matplotlib
plt.title('Attack by Type')

# Melt DataFrame
melted_df = pd.melt(stats_df,
                    id_vars=["Name", "Type 1", "Type 2"],  # Variables to keep
                    var_name="Stat")  # Name of melted variable
melted_df.head()

# Swarmplot with melted_df
sns.swarmplot(x='Stat', y='value', data=melted_df,
              hue='Type 1')

# 1. Enlarge the plot
plt.figure(figsize=(10, 6))

sns.swarmplot(x='Stat',
              y='value',
              data=melted_df,
              hue='Type 1',
              dodge=True,  # 2. Separate points by hue
              palette=pkmn_type_colors)  # 3. Use Pokemon palette

# 4. Adjust the y-axis
plt.ylim(0, 260)

# 5. Place legend to the right
plt.legend(bbox_to_anchor=(1, 1), loc=2)

plt.show()
