Create a .env file with:

TOKEN, COURSE_ID, URL and SLEEP_TIME

URL is 'https://canvas.instructure.com/api/v1/courses/' for the instructure Canvas. Also, SLEEP_TIME = 0 is a good default.

Scripts:
- canvas_emails: get a CSV with emails
- canvas_quiz: get quiz submissions as txt files
- canvas_to_codepost: convert a directory with zipped files with students java exercises to codepost.
