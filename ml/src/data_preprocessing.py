import pandas as pd
from sklearn.preprocessing import LabelEncoder
   
def preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path, low_memory=False) 

    # Keep relevant columns based on your dataset
    relevant_columns = [
        'goal', 'pledged', 'state', 'deadline', 'created_at', 'launched_at', 'category', 'blurb' 
    ]
    df = df[relevant_columns] 

    # Drop rows with missing values in relevant columns
    df = df.dropna(subset=['goal', 'pledged', 'state', 'deadline', 'created_at', 'launched_at'])

    # Keep only successful or failed campaigns
    df = df[df['state'].isin(['successful', 'failed'])]

    # Convert 'deadline' and 'launched_at' to datetime
    df['deadline'] = pd.to_datetime(df['deadline'], errors='coerce')
    df['launched_at'] = pd.to_datetime(df['launched_at'], errors='coerce')

    # Ensure 'goal' and 'pledged' are numeric
    df['goal'] = pd.to_numeric(df['goal'], errors='coerce')
    df['pledged'] = pd.to_numeric(df['pledged'], errors='coerce')

    # Label encode the 'category' column
    label_encoder = LabelEncoder()
    df['category'] = label_encoder.fit_transform(df['category'])

    # Derive additional features
    df['duration'] = (df['deadline'] - df['launched_at']).dt.days
    df['description_length'] = df['blurb'].str.len()
    
    # Convert 'state' to binary (1 for successful, 0 for failed)
    df['state'] = df['state'].map({'successful': 1, 'failed': 0})

    # Drop unnecessary columns and keep only relevant ones for analysis
    df = df[['goal', 'pledged', 'state', 'duration', 'category', 'description_length']]

    # Return the cleaned dataset
    return df 
