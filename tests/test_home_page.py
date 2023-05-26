from src.page_objects.home_page import HomePage


def test_search(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.search("Iphone")
