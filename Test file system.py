import os
import pickle

# Define the name and path of the file to save the data
file_name = "data.pkl"
file_path = os.path.join(os.getcwd(), file_name)

# Define the default value of the variable if the file doesn't exist
default_data = {'resin have': 20}

# Check if the file exists and load the data if it does
if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
else:
    # Save the default data to the file if it doesn't exist
    with open(file_path, 'wb') as file:
        pickle.dump(default_data, file)
    # Set the data variable to the default data
    data = default_data

# Do whatever you need with the data variable
print(data.get('resin have'))

# Save the data variable to the file before closing the program
with open(file_path, 'wb') as file:
    pickle.dump(data, file)
