import os

files = os.listdir('C:\\Users\\Cyber\\Music')

print(files)

os.makedirs('C:\\Users\\Cyber\\Music\\Projetos-Python', exist_ok=True)
print("Directory created.") 