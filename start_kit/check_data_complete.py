import json
import os
import pandas as pd

# Path to the metadata and video folder
file_path = 'WLASL_v0.3.json'
video_folder_path = 'videos'  # Change this to your video folder path

with open(file_path) as ipf:
    content = json.load(ipf)

# Create a list to store gloss and the count of instances with videos
gloss_video_data = []

for ent in content:
    gloss = ent['gloss']
    instances = ent['instances']
    
    # Count the number of instances with a corresponding video file
    count_with_video = sum(1 for inst in instances if os.path.exists(os.path.join(video_folder_path, f"{inst['video_id']}.mp4")))
    gloss_video_data.append({'Gloss': gloss, 'Instances with Video': count_with_video})

# Create a pandas DataFrame
df = pd.DataFrame(gloss_video_data)

# Calculate summary statistics
average_instances = df['Instances with Video'].mean()
min_instances = df['Instances with Video'].min()
max_instances = df['Instances with Video'].max()

# Add summary row
summary = pd.DataFrame({
    'Gloss': ['Summary'],
    'Instances with Video': [f'Avg: {average_instances:.2f}, Min: {min_instances}, Max: {max_instances}']
})

# Append the summary to the DataFrame
df = pd.concat([df, summary], ignore_index=True)

df.to_csv('gloss_summary.csv', index=False)

df
