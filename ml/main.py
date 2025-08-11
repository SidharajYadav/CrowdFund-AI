from src.data_preprocessing import preprocess_data
from src.model_training import train_model

# File path for dataset
file_path = 'data/kickstarter_data_full.csv'
df_cleaned = preprocess_data(file_path)
model = train_model(df_cleaned)

# Preprocess the data
df = preprocess_data(file_path)
print("Data preprocessing complete!") 

# Train the model
model = train_model(df)
print("Model training complete!") 
 
