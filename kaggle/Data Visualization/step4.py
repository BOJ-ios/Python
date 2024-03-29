import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
pd.plotting.register_matplotlib_converters()
print("Setup Complete")
# Path of the file to read
insurance_filepath = "C:/Users/jun30/Documents/GitHub/Python/kaggle/Data Visualization/input/insurance.csv"
# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)
print(insurance_data.head())
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
sns.scatterplot(
    x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])
plt.show()
