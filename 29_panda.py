import pandas as pd

# Create a dataframe from a csv file
df = pd.read_csv('fifa_world_cup_2022_tweets.csv')

# Display the first few rows of the dataframe
print(df.head())

# Delete rows with NA values in any column
df.dropna(inplace=True)

# Delete rows with NA values in specific columns
df.dropna(subset=['Date Created', 'Source of Tweet'], inplace=True)

# Fill NA values with random values
df.fillna(value=pd.np.random.randn(), inplace=True)

# Fill NA values with the mean of the column
df.fillna(value=df.mean(), inplace=True)

# Fill NA values with the median of the column
df.fillna(value=df.median(), inplace=True)

# Display statistical information about the dataframe
print(df.describe())
