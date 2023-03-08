import pandas as pd
from sklearn.tree import DecisionTreeRegressor
# save filepath to variable for easier access
melbourne_file_path = "C:/Users/jun30/Documents/GitHub/Python/kaggle/Intro_to_Machine_Learning/melb_data.csv"
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
print(round(melbourne_data['Rooms'].mean()))
print()
print(melbourne_data.columns)
print()

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom',
                      'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print(X.describe())
print()
print(X.head())
print()

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)
# Fit model
melbourne_model.fit(X, y)
print("Making predictions for the following 5 houses:")
print(X.head())
print()
print("The predictions are")
print(melbourne_model.predict(X.head()))
print()
