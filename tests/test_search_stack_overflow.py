from search.search_stack_overflow import get_relevant_stack_overflow_answers


def test_get_relevant_stack_overflow_answers_empty_query_gets_empty_snippets():
    expected_answers = tuple()
    query = ''
    actual_answers = get_relevant_stack_overflow_answers(query)
    assert actual_answers == expected_answers


def test_get_relevant_stack_overflow_answers_any_query_gets_dummy_snippets():
    expected_answers = 'answer 1', 'answer 2'
    query = 'any text'
    actual_answers = get_relevant_stack_overflow_answers(query)
    assert actual_answers == expected_answers
