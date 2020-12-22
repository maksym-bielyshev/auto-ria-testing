from _pytest.fixtures import FixtureRequest
from selenium.webdriver.chrome.options import Options
import pytest
import csv
from selenium import webdriver


@pytest.fixture(scope="function")
def init_driver(request: FixtureRequest) -> None:
    """Remote driver initialization with required options.

    :param request: FixtureRequest
    :return: None
    """
    options = Options()
    driver = webdriver.Chrome()

    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver


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
