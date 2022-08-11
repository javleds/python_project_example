# Project example

This project was created to test the service injection in python
using pytest for functional testing and venv.

## Requirements
- python ^3.8.10
- pip

## Venv setup
- Go to the project root directory
- Run `python3 -m venv venv`
- Enable the venv by running: `source venv/bin/activate`
- Now we are ready to follow the Dev setup section.

## Dev setup
- Create a copy of the `config.ini.dist` file as `config.ini` and replace the required values: `cp config.ini.dist config.ini` 
- Install the project dependencies by running: `pip install -r requirements.txt`
- Execute the app: `python src/__main__.py`