import os
import subprocess

print("Starting YouTube data pipeline...")

# Step 1: Fetch data
subprocess.run(["python", "scripts/fetch_youtube_data.py"], check=True)

# Step 2: Clean data
subprocess.run(["python", "scripts/data_cleaning.py"], check=True)

# Step 3: EDA On  data
subprocess.run(["python", "scripts/eda_analysis.py"], check=True)

# Step 4: Export data
subprocess.run(["python", "scripts/export_data.py"], check=True)

print("Pipeline completed successfully! Data refreshed.")
