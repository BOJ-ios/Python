import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
pd.plotting.register_matplotlib_converters()
print("Setup Complete")
# Path of the file to read
iris_filepath = "C:/Users/jun30/Documents/GitHub/Python/kaggle/Data Visualization/input/iris.csv"
# Read the file into a variable iris_data
iris_data = pd.read_csv(iris_filepath, index_col="Id")
# Print the first 5 rows of the data
print(iris_data.head())
# Histogram
# sns.histplot(iris_data['Petal Length (cm)'], kde=True)
# Histograms for each species
sns.histplot(data=iris_data, x='Petal Length (cm)', hue='Species')

# KDE plot
# sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)
# KDE plots for each species
# sns.kdeplot(data=iris_data, x='Petal Length (cm)', hue='Species', shade=True)

# sns.jointplot(x=iris_data['Petal Length (cm)'],
#              y=iris_data['Sepal Width (cm)'], kind="kde")

# Add title
plt.title("Histogram of Petal Lengths, by Species")
plt.show()
