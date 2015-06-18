import stackexchange


stack_overflow = stackexchange.Site(stackexchange.StackOverflow,
                                    impose_throttling=True)
stack_overflow.be_inclusive()


def get_relevant_stack_overflow_answers(query, num_answers=3):
    if not query:
        return tuple()
    questions = stack_overflow.search(intitle=query)
    questions = [stack_overflow.question(question.id)
                 for question in questions]
    questions.sort(key=lambda question: question.score, reverse=True)
    questions = questions
    answers = [answer
               for question in questions
               for answer in question.answers]
    answers.sort(key=lambda answer: answer.score, reverse=True)
    answer_bodies = [answer.body for answer in answers]
    answer_bodies = answer_bodies[:num_answers]
    return tuple(answer_bodies)
