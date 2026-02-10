from test_UI_husnut_pw.pages.load_page import Load
from test_UI_husnut_pw.pages.demo_qa_page import DemoQa
from test_UI_husnut_pw.pages.qa_practice_input_page import QaPracticeInputText
from test_UI_husnut_pw.pages.qa_practice_single_select import QaPracticeLanguageSelection
import pytest


@pytest.fixture()
def load(page):
    return Load(page)


@pytest.fixture()
def demo_qa(page):
    return DemoQa(page)


@pytest.fixture()
def practice_input(page):
    return QaPracticeInputText(page)


@pytest.fixture()
def practice_select(page):
    return QaPracticeLanguageSelection(page)
