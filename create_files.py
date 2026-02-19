import os

base_path = r"C:\Users\Kavita Shewale\Desktop\Python_Assignment"
folder_name = "practice"

full_path = os.path.join(base_path, folder_name)

# Create folder
os.makedirs(full_path, exist_ok=True)

# Create 10 empty Python files
for i in range(1, 11):
    open(os.path.join(full_path, f"file{i}.py"), "w").close()

print("Folder and 10 Python files created successfully!")
