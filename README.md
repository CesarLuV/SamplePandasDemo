# SamplePandasDemo
Sample demo of manage, process and analize files with Python and Pandas.

# Clone the Project

In the folder where you want to work, open a terminal and write the following command:
```
git clone https://github.com/CesarLuV/SamplePandasDemo.git
```

# Create a virtual Environment (Unix Based Systems)

Run the following commands:

1. `cd SamplePandasDemo`
2. `python3 -m venv .env`
3. `source .env/bin/activate`

**Note**: To exit the virtual environment, in the terminal run the command `deactivate`

# Update your pip version
Once you have activated the virtual environment, to verify you are up to date with python installer package, you should run the following command:
```
python3 -m pip install --upgrade pip
```

# Install the requirements
Once you have activated the virtual environment, run the following command:
```
pip3 install -r requirements.txt
```

# Running the project
Execute the following command:

```uvicorn main:app --reload```

As is the default port, you should be able to see the running project on: 
```http://127.0.0.1:8000```


# Verify the PEP8 Standar for Python files
Located where *SamplePandasDemo* project folder is, run the following comands:
```
pycodestyle --first common/utils.py
pycodestyle --show-source --show-pep8 main.py
```

The above commands will indicate wich possible PEP8 coding standard metrics should be modified for the maximum readability of the souece code.

**NOTE**: That lines of the code are just examples and should be aplied for all files.
