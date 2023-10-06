# Fantasy Football

Playing with some data from Fantasy Football from the league I'm playing.

My team is Steely Dan Fan Club an this is our logo

![My Logo](./steely-dan-fan-club_cropped.png)

League's data extracted using [espnfantasyfootball](https://github.com/tbryan2/espnfantasyfootball).

## Initiate


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/players.csv")
mt = pd.read_csv("data/matches.csv")
```

## Some Variables to work with


```python
my_team = "Steely Dan Fan Club"
last_full_week = 4
```

## Prepare

Rename columns


```python
df.rename(columns={
    "Week": "week",
    "PlayerName": "name",
    "PlayerScoreActual": "score",
    "PlayerScoreProjected": "projected",
    "PlayerFantasyTeam": "team_index",
    "PlayerRosterSlot": "position",
    "TeamName": "team",
    "FullName": "user"
}, inplace=True)
mt.rename(columns={
    "Week": "week",
    "Name1": "team1",
    "Score1": "score1",
    "Name2": "team2",
    "Score2": "score2",
    "Type": "type"
}, inplace=True)
```

Filter only played weeks


```python
df = df[df.week<=last_full_week]
mt = mt[mt.week<=last_full_week].drop_duplicates()
```

## Working Data


```python
df.info()
df.head()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 909 entries, 0 to 908
    Data columns (total 8 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   week        909 non-null    int64  
     1   name        909 non-null    object 
     2   score       909 non-null    float64
     3   projected   909 non-null    float64
     4   team_index  909 non-null    int64  
     5   position    909 non-null    object 
     6   team        909 non-null    object 
     7   user        909 non-null    object 
    dtypes: float64(2), int64(2), object(4)
    memory usage: 63.9+ KB





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>week</th>
      <th>name</th>
      <th>score</th>
      <th>projected</th>
      <th>team_index</th>
      <th>position</th>
      <th>team</th>
      <th>user</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Davante Adams</td>
      <td>15.60</td>
      <td>21.204351</td>
      <td>1</td>
      <td>WR</td>
      <td>Team Theis</td>
      <td>Maya Theis</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Patrick Mahomes</td>
      <td>18.54</td>
      <td>24.679680</td>
      <td>1</td>
      <td>QB</td>
      <td>Team Theis</td>
      <td>Maya Theis</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Aaron Jones</td>
      <td>28.70</td>
      <td>16.338186</td>
      <td>1</td>
      <td>RB</td>
      <td>Team Theis</td>
      <td>Maya Theis</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>T.J. Hockenson</td>
      <td>12.00</td>
      <td>13.890898</td>
      <td>1</td>
      <td>TE</td>
      <td>Team Theis</td>
      <td>Maya Theis</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>Brandon Aiyuk</td>
      <td>37.90</td>
      <td>11.752372</td>
      <td>1</td>
      <td>WR</td>
      <td>Team Theis</td>
      <td>Maya Theis</td>
    </tr>
  </tbody>
</table>
</div>




```python
mt.info()
mt.head()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 28 entries, 0 to 27
    Data columns (total 6 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   week    28 non-null     int64  
     1   team1   28 non-null     object 
     2   score1  28 non-null     float64
     3   team2   28 non-null     object 
     4   score2  28 non-null     float64
     5   type    28 non-null     object 
    dtypes: float64(2), int64(1), object(3)
    memory usage: 1.5+ KB





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>week</th>
      <th>team1</th>
      <th>score1</th>
      <th>team2</th>
      <th>score2</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Team Johnson</td>
      <td>141.64</td>
      <td>Team Quirk</td>
      <td>160.76</td>
      <td>Regular</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Steely Dan Fan Club</td>
      <td>132.24</td>
      <td>Team Sand</td>
      <td>61.10</td>
      <td>Regular</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Team Amar</td>
      <td>106.98</td>
      <td>Team Calzaretta</td>
      <td>77.76</td>
      <td>Regular</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>Team DarkBrandon</td>
      <td>89.34</td>
      <td>Team Theis</td>
      <td>133.44</td>
      <td>Regular</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>Team Bernier-Simard</td>
      <td>112.28</td>
      <td>Team FortyTwo</td>
      <td>120.94</td>
      <td>Regular</td>
    </tr>
  </tbody>
</table>
</div>



# Metrics, Tables and Charts

Teams wins and total scores


```python
wins = pd.Series(np.where(mt.score1 > mt.score2, mt.team1, mt.team2)).value_counts()
scores = df[df.position!='Bench'].groupby(['team']).score.sum().sort_values(ascending=False)

pd.concat({'wins': wins, 'total_scores': scores}, axis=1).sort_values(['wins', 'total_scores'], ascending=False)

# To get the average point per match (week) per team
# df[df.position!='Bench'].groupby(['week', 'team']).score.sum().groupby('team').mean().sort_values(ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wins</th>
      <th>total_scores</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Team Vitale</th>
      <td>4</td>
      <td>560.82</td>
    </tr>
    <tr>
      <th>Team Theis</th>
      <td>3</td>
      <td>571.44</td>
    </tr>
    <tr>
      <th>Team Amar</th>
      <td>3</td>
      <td>476.48</td>
    </tr>
    <tr>
      <th>Team Johnson</th>
      <td>2</td>
      <td>513.84</td>
    </tr>
    <tr>
      <th>Team Calzaretta</th>
      <td>2</td>
      <td>466.66</td>
    </tr>
    <tr>
      <th>Team dawkins</th>
      <td>2</td>
      <td>466.50</td>
    </tr>
    <tr>
      <th>Steely Dan Fan Club</th>
      <td>2</td>
      <td>447.54</td>
    </tr>
    <tr>
      <th>Team Quirk</th>
      <td>2</td>
      <td>436.66</td>
    </tr>
    <tr>
      <th>Team timewonder</th>
      <td>2</td>
      <td>419.52</td>
    </tr>
    <tr>
      <th>Team Bernier-Simard</th>
      <td>2</td>
      <td>405.48</td>
    </tr>
    <tr>
      <th>Team DarkBrandon</th>
      <td>1</td>
      <td>518.68</td>
    </tr>
    <tr>
      <th>Team FortyTwo</th>
      <td>1</td>
      <td>464.72</td>
    </tr>
    <tr>
      <th>Team Sand</th>
      <td>1</td>
      <td>464.46</td>
    </tr>
    <tr>
      <th>Team Rose42</th>
      <td>1</td>
      <td>410.64</td>
    </tr>
  </tbody>
</table>
</div>



Comparing players performances throughout the season


```python
def plot_players_score_throughout_season(df, ax, players, title="Players performances throughout the season"):
    """ Given the DataFrame, the axes, and the players names, plot the scores of the players throughout the weeks of the season in the axes
    """
    
    df[df.name.isin(players)][['week', 'name', 'score']]\
        .pivot(columns="name", index="week", values="score")\
        .plot(ax=ax)
    
    ax.set_title(title)
    ax.legend(title=None)
    # ax.set_ylim(bottom=0)
    # Set xticks to be only integers
    from matplotlib.ticker import MaxNLocator
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```


```python
rbs = ["Bijan Robinson", "Miles Sanders"]
wrs = ["Amon-Ra St. Brown", "Chris Olave", "Amari Cooper", "Amari Cooper", "Jakobi Meyers", "DeVante Parker", "Zay Jones"]
qbs = ["Tua Tagovailoa", "Jordan Love"]

fig, ax = plt.subplots(figsize=(16,4), ncols=3)

plot_players_score_throughout_season(df[(df.team==my_team)], ax[0], rbs, title="Running Back performances")
plot_players_score_throughout_season(df[(df.team==my_team)], ax[1], qbs, title="Quarterbacks performances")
plot_players_score_throughout_season(df[(df.team==my_team)], ax[2], wrs, title="Wide Receivers performances")
ax[2].legend(fontsize="x-small")
```




    <matplotlib.legend.Legend at 0x7f73f696f880>




    
![png](Fantasy%20Football_files/Fantasy%20Football_18_1.png)
    


Comparing projections with actual scores


```python
fig, axs = plt.subplots(figsize=(14, 6), ncols=2)

df['projection_error'] = df.projected - df.score

sns.scatterplot(data=df[df.position!='Bench'], x='score', y='projected', hue='position', ax=axs[0])
axs[0].set_title("Scatter of projected score VS actual score")
# Y axis limits to the same as X axis limits
axs[0].set_ylim(bottom=axs[0].get_xlim()[0], top=axs[0].get_xlim()[1])

df['projection_error'].plot.hist(bins=20, ax=axs[1])
axs[1].set_title("Histogram of projection error (projected - actual score)")

```




    Text(0.5, 1.0, 'Histogram of projection error (projected - actual score)')




    
![png](Fantasy%20Football_files/Fantasy%20Football_20_1.png)
    


Comparing positions scores across teams, in Week 1


```python
week = 1
position = 'RB'

rb_score_week_1 = df[(df.week==week) & (df.position==position)][["team", "name", "score"]]\
    .sort_values(by="team")\
    .set_index(["team", "name"])

fig, ax = plt.subplots(figsize=(12, 4))
rb_score_week_1.plot.bar(ax=ax, legend=False)

ax.set_title(f"{position} scores in week {week}")

plt.show()
```


    
![png](Fantasy%20Football_files/Fantasy%20Football_22_0.png)
    



```python

```
