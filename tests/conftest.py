import pytest
import csv
from selenium import webdriver
import time
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.review_page import ReviewPage

import configparser
config = configparser.ConfigParser()
config.read('config.ini')


@pytest.fixture(scope="session")
def init_driver():
    """Remote driver initialization with required options.

    :return: None
    """
    driver = webdriver.Chrome(config['drivers']['windows'])
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    yield driver

    driver.close()


@pytest.fixture(scope='function')
def open_home_page(init_driver):
    driver = init_driver
    driver.get(config['urls']['home_page'])
    time.sleep(3)
    return HomePage(driver)


@pytest.fixture(scope='function')
def open_category_page(init_driver):
    driver = init_driver
    driver.get(config['urls']['category_page'])
    time.sleep(3)
    return CategoryPage(driver)


@pytest.fixture(scope='function')
def open_review_page(init_driver):
    driver = init_driver
    driver.get(config['urls']['review_page'])
    time.sleep(3)
    return ReviewPage(driver)


def get_test_data(file_name: str) -> list:
    """Converts file with test data to tuples list.
    :param file_name: string
    :return: test_data_list consists of tuples, each tuple is one file row.
    """
    with open(f'../tests_data/{file_name}', 'r', encoding="utf8") as file:
        reader = csv.reader(file, quoting=csv.QUOTE_ALL,
                            skipinitialspace=True, delimiter='\t')
        test_data_list = []
        for row in reader:
            test_data_list.append(tuple(row[0].strip('][').split(';')))
        return test_data_list


def get_test_data_dictreader(file, file_second=None):
    files = [file]
    if file_second is not None:
        files.append(file_second)
    test_data_list = []
    for file in files:
        fieldnames = ('language', 'data', 'expected_result')
        csv_file = open(f'../tests_data/{file}', encoding='utf8')
        input_file = csv.DictReader(csv_file, delimiter=';',
                                    fieldnames=fieldnames)
        for row in input_file:
            data = (row['language'], row['data'], row['expected_result'])
            test_data_list.append(data)
    return test_data_list
