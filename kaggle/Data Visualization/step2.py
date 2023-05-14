import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
pd.plotting.register_matplotlib_converters()
print("Setup Complete")

# Path of the file to read
spotify_filepath = "C:/Users/jun30/Documents/GitHub/Python/kaggle/Data Visualization/input/spotify.csv"
# Read the file into a variable spotify_data
spotify_data = pd.read_csv(
    spotify_filepath, index_col="Date", parse_dates=True)
print(spotify_data.head())
print(spotify_data.tail())
# Set the width and height of the figure
plt.figure(figsize=(14, 6))
# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
# Line chart showing daily global streams of each song
# sns.lineplot(data=spotify_data)
# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")
# Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")
# Add label for horizontal axis
plt.xlabel("Date")

print(list(spotify_data.columns))
plt.show()
