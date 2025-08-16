import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# Step 3: Filter for India
india_df = df[df['location'] == 'India']

# Step 4: Select useful columns
india_df = india_df[['date', 'new_cases', 'total_deaths', 'people_vaccinated']]

# Step 5: Convert date column
india_df['date'] = pd.to_datetime(india_df['date'])

# Step 6: Plot daily new cases
plt.figure(figsize=(10,5))
sns.lineplot(data=india_df, x='date', y='new_cases')
plt.title("Daily New COVID-19 Cases in India")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.show()
# Total deaths over time
plt.figure(figsize=(10,5))
sns.lineplot(data=india_df, x='date', y='total_deaths', color='red')
plt.title("Total Deaths in India Over Time")
plt.show()

# Vaccination progress
plt.figure(figsize=(10,5))
sns.lineplot(data=india_df, x='date', y='people_vaccinated', color='green')
plt.title("Vaccination Progress in India")
plt.show()
# Find the highest number of daily cases
max_cases = df['new_cases'].max()

# Find the date when it happened
peak_date = df['new_cases'].idxmax()

# Print the result
print(f"The highest number of daily cases was {max_cases} on {peak_date}.")

# Calculate the average number of daily cases
average_cases = df['new_cases'].mean()

# Print the result
print(f"The average number of daily cases is approximately {int(average_cases)}.")

# Add a 7-day rolling average column
df['7_day_avg'] = df['new_cases'].rolling(window=7).mean()

# Plot daily cases vs. rolling average
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(df['new_cases'], label='Daily Cases', alpha=0.5)
plt.plot(df['7_day_avg'], label='7-Day Average', color='red')
plt.title('COVID-19 Daily Cases vs. 7-Day Rolling Average')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.tight_layout()
plt.show()
print("Summary of Insights:")
print(f"Peak daily cases: {max_cases} on {peak_date}")
print(f"Average daily cases: {int(average_cases)}")
print("Rolling average plot saved as 'covid_trend_plot.png'")
