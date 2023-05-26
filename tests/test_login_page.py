from src.page_objects.account_page import AccountPage
from src.page_objects.login_page import LoginPage


def test_invalid_login(web_drivers):
    expected_msg = "Warning: No match for E-Mail Address and/or Password."
    login_page = LoginPage(*web_drivers)
    login_page.open()
    login_page.login("user@qaminds.com", "invalid_password")
    actual_msg = login_page.get_warning_message()
    assert expected_msg == actual_msg, f"Warning message should {expected_msg}"


def test_valid_login(web_drivers):
    expected_title = "My Account"
    expected_right_menus = ["My Account", "Edit Account", "Password", "Address Book"]
    login_page = LoginPage(*web_drivers)
    login_page.open()
    login_page.login("tester@qaminds.com", "testtest")
    account_page = AccountPage(*web_drivers)
    actual_title = account_page.get_title()
    assert expected_title == actual_title, f"Page title after login should be {expected_title}"
    actual_right_menus = account_page.get_right_menu_names()
    for menu_name in expected_right_menus:
        assert menu_name in actual_right_menus, f"Right menu should include {menu_name}"
    account_page.click_right_menu("Edit Account")
    assert True
