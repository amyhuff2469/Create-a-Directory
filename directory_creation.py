#imports
import pandas as pd
import os

# Read the .csv file into a dataframe
df = pd.read_csv('C:\\Users\\AmyHuff\\OneDrive - Aptive Resources\\Desktop\\FERSS_locations.csv')
   
df.head()

# Create a function to create four static subfolders that will live inside the Data subfolder (see next step)
def create_level3_subfolders(parent_folder_path):
    level3_subfolders = ['Raw','External','Interim','Final']
    
    for subfolder in level3_subfolders:
        subfolder_path = os.path.join(parent_folder_path, subfolder)
        
        # Create a conditional statement to see if the folder already exists
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            print(f"Created static subfolder: {subfolder_path}")
        else:
            print(f"Static subfolder already exists: {subfolder_path}")

# Create a function to create two static subfolders that will live inside each site subfolder
def create_level2_subfolders(parent_folder_path):
    level2_subfolders = ['Archive','Data']
    
    for subfolder in level2_subfolders:
        subfolder_path = os.path.join(parent_folder_path, subfolder)
        
        # Create a conditional statement to see if the folder already exists
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            print(f"Created static subfolder: {subfolder_path}")
        else:
            print(f"Static subfolder already exists: {subfolder_path}")

        #Create a conditional statement to run the "create_level3_subfolders" function if the folder name is Data
        if subfolder == 'Data':  
            create_level3_subfolders(subfolder_path)
            
# Create subfolders for each site based on the ID column. Also check the status of each row. If Closed, move to the Closed Assignment subfolder.
def create_folders_from_dataframe(df, base_directory, inactive_subfolder):
    
    # Create base directory if it doesn't exist
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)
        print(f"Created base directory: {base_directory}")
    else:
        print(f"Base directory already exists: {base_directory}")

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract the unique ID and status from the row
        unique_id = row['ID']
        assignment_status = row['Status']
        
        # Define the subfolder name and path. Determine where it will go based on the Status column.
        if assignment_status == 'Active':
            subfolder_name = f"{unique_id}"
            subfolder_path = os.path.join(base_directory, subfolder_name)
        else:
            subfolder_name = f"{unique_id}"
            subfolder_path = os.path.join(base_directory, inactive_subfolder, subfolder_name)

        # Create the main subfolder if it doesn't already exist
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            print(f"Created subfolder: {subfolder_path}")
        else:
            print(f"Subfolder already exists: {subfolder_path}")

        # Create static subfolders inside each created subfolder
        create_level2_subfolders(subfolder_path)

# Create a function to create an inactive assignment subfolder. 
def create_inactive_subfolder(base_directory, inactive_subfolder):
    inactive_path = os.path.join(base_directory, inactive_subfolder)

    if not os.path.exists(inactive_path):
        os.makedirs(inactive_path)
        print(f"Created inactive subfolder: {inactive_path}")
    else:
        print(f"Inactive subfolder already exists: {inactive_path}")

# Define directories
base_directory = 'FERSS_Locations'
inactive_subfolder = "Closed Assignments"

# Create inactive subfolder directory
create_inactive_subfolder(base_directory, inactive_subfolder)

# Create folders from DataFrame and static subfolders
create_folders_from_dataframe(df, base_directory, inactive_subfolder)

