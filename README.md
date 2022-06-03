# Initial Setup

### Create conda virtual environment
conda create -n wineq python=3.7 -y

### Activate created conda environment
conda activate wineq

### Run requirements.txt file
pip install -r requirements.txt

### Create template.py to create project folder structure
python template.py

### Initialize project folder with git and also initialize dvc
git init
dvc init

### Add given data to dvc
dvc add data_given/winequality.csv

### Create remote project folder on github and push the local repo to the remote
git remote add origin https://github.com/chandramohantn/simple-dvc-app.git
git branch -M main
git push origin main

### Create get_data.py, load_data.py and split_data.py
### get_data.py will fetch the csv data and saves it to the project data folder mentioned in the params.yaml
### load_data.py will load the raw data and change the column headers and saves it back to the folder mentioned in the params.yaml
### split_data.py will split the processed data to train and test based on the split ratio mentioned in the params.yaml
python src/get_data.py
python src/load_data.py
python src/split_data.py


