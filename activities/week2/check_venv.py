import os

if os.environ.get('VIRTUAL_ENV'):
    print("Virtual environment is activated.")
else:
    print("Virtual environment is not activated.")
