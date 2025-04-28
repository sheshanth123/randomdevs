# create venev
cd your_project_directory

python -m venv venv

source venv/bin/activate  # Use `venv\Scripts\activate` on Windows

python -m unittest test_calc.py

deactivate


# unit test vs pytest
https://www.geeksforgeeks.org/difference-between-pytest-and-unittest/


# get coverage report
coverage run -m unittest test_calc.py

coverage report

coverage html
