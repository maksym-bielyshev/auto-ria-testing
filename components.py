# from selenium.webdriver import Remote
#
# class InputFieldComponent:
#     """An input field to fill with data from user."""
#
#     def __init__(self, driver: Remote, input_field_locator: tuple,
#                  parent_element: WebElement = None
#                  ) -> None:
#         """Initialize the input field.
#         :param driver: Remote
#         :param input_field_locator: tuple
#         :return: None
#         """
#         self._driver = driver
#         self.input_field_locator = input_field_locator
#         self.parent_element = parent_element
#
#     def _find_input_field(self) -> None:
#         """Find input field by parent element or driver.
#
#         :return: None
#         """
#         if self.parent_element:
#             self.input_field = self.parent_element.find_element(
#                 *self.input_field_locator
#             )
#         else:
#             self.input_field = self._driver.find_element(
#                 *self.input_field_locator
#             )
#
#     def clear_and_fill_input_field(self, data: str) -> None:
#         """Clear and fill input field with data.
#
#         :param data: str
#         :return: None
#         """
#         self._find_input_field()
#         self.input_field.clear()
#         self.input_field.send_keys(data)