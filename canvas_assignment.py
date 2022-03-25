import sys

from canvas import get_data, get_submissions

assignments_data = get_data('assignments/')
assignment_id = sys.argv[1]
get_submissions(assignment_id, 'sub_a_')