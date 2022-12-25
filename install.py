from dotenv import load_dotenv

load_dotenv()
path = input("enter path to resources folder with ending '/': ")

with open(".env", 'w+') as env:
    env.writelines([f"AXES_ROOT='{path}'InputAxes"])