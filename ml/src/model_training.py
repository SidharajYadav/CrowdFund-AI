# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import pickle

# def train_model(df):
#     # Features and target
#     X = df[['goal', 'duration', 'category', 'description_length']]
#     y = df['state']

#     # Split data
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     # Train model
#     model = RandomForestClassifier(n_estimators=100, random_state=42)
#     model.fit(X_train, y_train)

#     # Test model
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     print(f"Model Accuracy: {accuracy * 100:.2f}%")

#     # Save the model
#     with open('campaign_success_model.pkl', 'wb') as file:
#         pickle.dump(model, file)
#     print("Model saved successfully!")

#     return model



import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
import pickle
from sklearn.preprocessing import LabelEncoder

def train_model(df):
    print("Starting model training...")

    # Check if necessary columns are in the data
    print("Columns in the dataset:", df.columns)

    # Calculate 'duration' if it's not available
    if 'duration' not in df.columns:
        print("Calculating 'duration' column...")
        df['launched_at'] = pd.to_datetime(df['launched_at'])
        df['deadline'] = pd.to_datetime(df['deadline'])
        df['duration'] = (df['deadline'] - df['launched_at']).dt.days  # duration in days

    # Calculate 'description_length' if it's not available
    if 'description_length' not in df.columns:
        print("Calculating 'description_length' column...")
        df['description_length'] = df['blurb'].apply(lambda x: len(str(x)) if pd.notnull(x) else 0)

    # Features and target
    X = df[['goal', 'duration', 'category', 'description_length']]  # Assuming 'description_length' is already numeric
    y = df['state']

    # Handle categorical data in 'category' column
    print("Encoding categorical 'category' column...")
    label_encoder = LabelEncoder()
    X['category'] = label_encoder.fit_transform(X['category'])

    # Split data
    print("Splitting the data into train and test...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    print("Training the model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Test model
    print("Making predictions...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Save the model
    print("Saving the model...")
    model_dir = 'models'
    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, 'campaign_success_model.pkl')
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)
    print(f"Model saved successfully at {model_path}")

    return model

if __name__ == "__main__":
    # Load your dataset (make sure the path is correct)
    df = pd.read_csv('D:/Devops/CrowdFundAI/ml/data/kickstarter_data_full.csv')
    train_model(df)

