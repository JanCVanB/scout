from search.search_stack_overflow import get_relevant_stack_overflow_answers


def test_get_relevant_stack_overflow_answers_empty_query_gets_empty_snippets():
    expected_answers = tuple()
    query = ''
    actual_answers = get_relevant_stack_overflow_answers(query)
    assert actual_answers == expected_answers


def test_get_relevant_stack_overflow_answers_returns_best_answer_first():
    queries = 'python yield', 'java static', 'c++'
    best_answer_keywords = 'mygenerator', 'enclosing', 'prediction'
    for query, best_answer_keyword in zip(queries, best_answer_keywords):
        answers = get_relevant_stack_overflow_answers(query)
        best_answer = answers[0]
        assert best_answer_keyword in best_answer
