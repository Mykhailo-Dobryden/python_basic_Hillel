"""2. Написати функцію яка частково приховуватиме e-mail, приклад:
 hide_email(somebody_email@gmail.com) -> em***@**il.com"""


def hide_user_name(string):
    char = '*'
    char_total = len(string)
    if len(string) < 5:
        char_total = char_total - 1
        return f"{string[:1]}{char * char_total}"
    if len(string) >= 5:
        char_total = char_total - 3
        return f"{string[:3]}{char * char_total}"


def hide_server_name(string):
    char = '*'
    char_total = len(string)
    if len(string) < 4:
        char_total = char_total - 1
        return f"{char * char_total}{string[-1:]}"
    if len(string) >= 4:
        char_total = char_total - 2
        return f"{char * char_total}{string[-2:]}"


def parse_email_address(email):
    user_name, _, mail_server_domain = email.rpartition('@')
    mail_server, _, domain = mail_server_domain.rpartition('.')
    return user_name, mail_server, domain


def hide_email(email):
    user_name, mail_server, domain = parse_email_address(email)
    return f"{hide_user_name(user_name)}@{hide_server_name(mail_server)}.{domain}"


print(hide_email("somebody_email@gmail.com"))
print(hide_email("dms@aol.com"))
print(hide_email("email@eyahoo.jp"))
print(hide_email("email@example.museum"))
