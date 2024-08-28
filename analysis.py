import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'la_liga_stats.csv'  # Replace with your file path
df = pd.read_csv(file_path)

print("First few rows of the dataset:")
print(df.head())


print("\nData types and missing values:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())


print("\nMissing values per column:")
print(df.isnull().sum())

df.dropna(inplace=True)

df['date'] = pd.to_datetime(df['date'])

# Confirm changes
print("\nData types after cleaning:")
print(df.info())


df['total_goals'] = df['home_team_goal'] + df['away_team_goal']

plt.figure(figsize=(10, 6))
sns.histplot(df['total_goals'], bins=20, kde=True)
plt.title('Distribution of Total Goals in La Liga Matches')
plt.xlabel('Total Goals')
plt.ylabel('Frequency')
plt.show()

avg_home_goals = df['home_team_goal'].mean()
avg_away_goals = df['away_team_goal'].mean()

print(f'\nAverage Home Goals: {avg_home_goals}')
print(f'Average Away Goals: {avg_away_goals}')

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['home_team_goal', 'away_team_goal']])
plt.title('Home vs. Away Goals Comparison')
plt.ylabel('Goals')
plt.xticks([0, 1], ['Home Goals', 'Away Goals'])
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(df['home_possession'], label='Home Possession', shade=True)
sns.kdeplot(df['away_possession'], label='Away Possession', shade=True)
plt.title('Home vs. Away Possession Distribution')
plt.xlabel('Possession (%)')
plt.ylabel('Density')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['home_fouls', 'away_fouls']])
plt.title('Home vs. Away Fouls Comparison')
plt.ylabel('Number of Fouls')
plt.xticks([0, 1], ['Home Fouls', 'Away Fouls'])
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['home_yellow_cards', 'away_yellow_cards']])
plt.title('Home vs. Away Yellow Cards')
plt.ylabel('Number of Yellow Cards')
plt.xticks([0, 1], ['Home', 'Away'])
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['home_red_cards', 'away_red_cards']])
plt.title('Home vs. Away Red Cards')
plt.ylabel('Number of Red Cards')
plt.xticks([0, 1], ['Home', 'Away'])
plt.show()

team_performance = df.groupby('home_team')[['home_team_goal', 'away_team_goal']].mean()

plt.figure(figsize=(12, 8))
team_performance.sort_values('home_team_goal', ascending=False).plot(kind='bar', figsize=(10, 6))
plt.title('Average Goals Scored by Teams (Home and Away)')
plt.ylabel('Average Goals')
plt.xlabel('Team')
plt.show()

team_goals = df.groupby('home_team')['home_team_goal'].sum() + df.groupby('away_team')['away_team_goal'].sum()

plt.figure(figsize=(10, 10))
plt.pie(team_goals, labels=team_goals.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Paired", len(team_goals)))
plt.title('Distribution of Total Goals by La Liga Teams')
plt.axis('equal') 
plt.show()
