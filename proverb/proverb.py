def proverb(*wants, qualifier=None):
    proverb_lines = []
    if not wants:
        return proverb_lines
    first_cause, *consequences = wants
    # print(f"first_cause: {first_cause}; consequences: {consequences}")
    cause = first_cause
    for consequence in consequences:
        proverb_lines.append(f"For want of a {cause} the {consequence} was lost.")
        cause = consequence
    first_cause = f"{qualifier} {first_cause}" if qualifier else first_cause
    proverb_lines.append(f"And all for the want of a {first_cause}.")
    return proverb_lines
