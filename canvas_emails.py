import csv
import sys

from canvas import get_data


def get_emails():
    data = get_data('users')
    result = []
    for user in data:
        if 'email' in user.keys() and user['email'] and ("@ccc.ufcg.edu.br" in user['email'] or "@computacao.ufcg.edu.br" in user['email'] or "@copin" in user['email']):
            result.append([user['id'], user['login_id'], user['name'],user['email'], "ok"])
        else:
            result.append([user['id'], user['login_id'], user['name'],user['email'], "error"])
    return result


if __name__ == "__main__":
    emails = get_emails()
    with sys.stdout as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(emails)