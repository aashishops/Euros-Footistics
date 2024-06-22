import os
import pandas as pd
import unicodedata
import re

# Define the folder path
folder_path = r'E:\github projects\Footistics\Players data\squad'

# Initialize lists to store player names and positions
all_player_names = []
all_positions = []

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        # Read the content from the .txt file using utf-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Parse the content to extract player names and positions
        for line in lines:
            # Split the line by comma and strip any extra spaces
            parts = line.strip().split(',')
            if len(parts) > 2:
                player_name = parts[1].strip()
                position = parts[2].strip()
                all_player_names.append(player_name)
                all_positions.append(position)

# Create a DataFrame
data = {
    "Data Player Name": all_player_names,
    "Position": all_positions
}

df = pd.DataFrame(data)

# Read the fbref CSV file
fbref = pd.read_csv(r'E:\github projects\Footistics\Players data\stats.csv')

# Normalize text function
def normalize_text(text):
    # Remove accents and diacritics
    normalized_text = unicodedata.normalize('NFKD', str(text)).encode('ascii', 'ignore').decode('utf-8')
    # Remove non-alphanumeric characters
    normalized_text = re.sub(r'[^a-zA-Z0-9\s]', '', normalized_text)
    # Convert to lowercase
    normalized_text = normalized_text.lower()
    return normalized_text

# Step 3: Normalize the names in fbref and df
fbref['Normalized Fbref Player'] = fbref['Player'].apply(normalize_text)
df['Normalized Data Player Name'] = df['Data Player Name'].apply(normalize_text)

# Merge DataFrames on normalized names
merged_df = pd.merge(df, fbref, left_on='Normalized Data Player Name', right_on='Normalized Fbref Player', how='inner')


# Create a new column with matched information
merged_df['Player and Position'] = merged_df.apply(lambda row: f"{row['Player']}-{row['Position']}", axis=1)

matched_info_df = merged_df['Player and Position'].str.split('-', expand=True)

# Select only the 'Player' and 'Position' columns to save
matched_info_df = merged_df[['Player', 'Position']]


# Save matched info to a CSV file
matched_info_file = r'E:\github projects\Footistics\FInal_DF\Positions_Mapped.csv'
matched_info_df.to_csv(matched_info_file, index=False)

print("Players matched and saved successfully.")
