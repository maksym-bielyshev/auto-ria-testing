"""Module for the 'Base Test'."""

import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    """Base class of all tests."""

    def teardown(self) -> None:
        """Actions at the end of each test.

        :return: None
        """
        self.driver.close()

    def scroll_to_end(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
