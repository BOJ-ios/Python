import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# save filepath to variable for easier access
melbourne_file_path = "C:/Users/jun30/Documents/GitHub/Python/kaggle/Intro_to_Machine_Learning/melb_data.csv"
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
print(round(melbourne_data['Rooms'].mean()))
print()
print(melbourne_data.columns)
print()

melbourne_features = ['Rooms', 'Bathroom',
                      'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
y = melbourne_data.Price
print(X.describe())
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

predicted_home_prices = melbourne_model.predict(X)
print(mean_absolute_error(y, predicted_home_prices))
print()

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)
# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
print()
