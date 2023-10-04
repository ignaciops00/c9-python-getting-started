from dotenv import load_dotenv
load_dotenv()
import os

database = os.getenv('DATABASE')
print(database)
