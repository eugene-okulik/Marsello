from test_UI_husnut_pw.utils.test_data import checked_text, language_ruby, text


def test_input_text(practice_input):
    practice_input.open_page()
    practice_input.input_text(text)
    practice_input.check_result_input_text(text)


def test_language_selection(practice_select):
    practice_select.open_page()
    practice_select.language_selection(language_ruby)
    practice_select.check_result_input_text()


def test_wait_text(load):
    load.open_page()
    load.click_and_wait()
    load.check_final_text(checked_text)


def test_filling_form(demo_qa):
    demo_qa.open_page()
    demo_qa.filling_form()
    demo_qa.check_result_form()
