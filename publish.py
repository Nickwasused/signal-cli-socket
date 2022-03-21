import os 

print("Don´t forget to change the Version in setup.py")

os.remove("./dist")

os.system("python setup.py bdist_wheel")
os.system("python -m twine upload dist/*")