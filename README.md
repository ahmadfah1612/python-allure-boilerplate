pip install -r requirements.txt

pytest --alluredir=./allure-results -v

allure serve allure-results
