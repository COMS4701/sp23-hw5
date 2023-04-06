# COMS W4701 AI HW5 Programming


### Setup
1. Create and activate your virtual environment (make sure your python is at version 3.8 or higher).
```
# using venv
python -m venv .venv
source .venv/bin/activate   

# on windows
python -m venv .venv
.venv\scripts\activate

# alternatively, using conda
conda create -n hw5env python=3.8 pip
conda activate hw5env
```

2. Install poetry
```
pip install poetry
```

3. Install the `hw5` package
```
poetry install
```

###  Running your implementation
You may run the main program with
```
python main.py
```
