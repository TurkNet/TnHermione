import re

sensitive_keywords = [
    "password", "passwd", "pass", "secret", "key", "apikey", "token",
    "ssh-key", "private-key", "credential", "credentials"
]

def contains_sensitive_info(message):
    pattern = re.compile("|".join(sensitive_keywords), re.IGNORECASE)
    lines = message.split('\n')
    for line_number, line in enumerate(lines, 1):
        match = pattern.search(line)
        if match:
            return True, line_number, match.group()
    return False, None, None
