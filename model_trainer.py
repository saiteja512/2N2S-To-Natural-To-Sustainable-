import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    """
    Loads the rainwater data, trains a linear regression model,
    and saves it to a file.
    """
    # Load the dataset
    try:
        data = pd.read_csv('rainwater_data.csv')
    except FileNotFoundError:
        print("Error: rainwater_data.csv not found. Please make sure the dataset is in the same directory.")
        return

    # --- Feature Engineering ---
    # Our goal is to predict the *next day's* tank level.
    # The features will be:
    # 1. Today's tank level
    # 2. Today's water usage
    # 3. The *forecasted* rainfall for tomorrow.
    
    # Create the target variable: the tank level of the next day
    data['next_day_tank_level'] = data['tank_level_liters'].shift(-1)
    
    # Drop the last row as it will have a NaN value for the target
    data.dropna(inplace=True)

    # Define features (X) and target (y)
    features = ['tank_level_liters', 'water_usage_liters', 'forecasted_rainfall_mm']
    target = 'next_day_tank_level'

    X = data[features]
    y = data[target]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model (optional, but good practice)
    score = model.score(X_test, y_test)
    print(f"Model trained successfully.")
    print(f"Model R^2 score (accuracy): {score:.2f}")

    # Save the trained model to a file
    joblib.dump(model, 'rainwater_model.pkl')
    print("Model saved as 'rainwater_model.pkl'")

if __name__ == '__main__':
    train_model()
