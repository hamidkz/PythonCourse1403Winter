usernames = ['hamidkz', 'alia', 'minah', 'zahraz', '']

emails = []
for username in usernames:
    email = f'{username}@systemgroup.net'
    emails.append(email)
print(emails)

emails_alt = [f'{username}@systemgroup.net' for username in usernames if len(username) > 0]
print(emails_alt)

