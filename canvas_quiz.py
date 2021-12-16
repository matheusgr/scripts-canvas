import json
import sys

from canvas import get_data


quiz_data = get_data('quizzes/')

quiz_id_download = sys.argv[1]

for quiz in quiz_data:
    quiz_id = str(quiz['id'])
    if quiz_id not in [quiz_id_download]:
        continue
    title = quiz['title']
    due_at = quiz['due_at']
    assignment_id = str(quiz['assignment_id'])
    question_data = get_data('quizzes/' + quiz_id + '/questions') 
    questions = {}
    for question in question_data:
        question_id = question['id']
        question_text = question['question_text']
        questions[question_id] = question_text
    questions_fname = 'questions_' + quiz_id + '.txt'
    open(questions_fname, 'w').write(json.dumps(question_data))
    sub_data = get_data('assignments/' + assignment_id + '/submissions?include[]=submission_history')
    open('sub_' + quiz_id + '.txt', 'w').write(json.dumps(sub_data))