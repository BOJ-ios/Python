import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
pd.plotting.register_matplotlib_converters()
print("Setup Complete")

# Path of the file to read
flight_filepath = "C:/Users/jun30/Documents/GitHub/Python/kaggle/Data Visualization/input/flight_delays.csv"
# Read the file into a variable flight_data
flight_data = pd.read_csv(flight_filepath, index_col="Month")
print(flight_data)
# Set the width and height of the figure
plt.figure(figsize=(10, 6))
# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])
# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")
plt.show()

# Set the width and height of the figure
plt.figure(figsize=(14, 7))
# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")
# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)
# Add label for horizontal axis
plt.xlabel("Airline")
plt.show()
