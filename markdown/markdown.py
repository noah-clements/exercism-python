import re


def parse(markdown):
    lines = markdown.split('\n')
    res = []
    in_list = False
    in_list_append = False
    # precompile the regex - it's faster. 
    # By using the {1,6} you can use the match count to stand in for the level
    heading = re.compile(r'(#{1,6}) (.*)')
    list_re = re.compile(r'\* (.*)')
    tag = re.compile(r'<h|<ul|<p|<li')
    bold = re.compile(r'__(.*?)__')
    ital = re.compile(r'_(.*?)_')
    for line in lines:
        heading_match = heading.match(line)
        if heading_match:           # Much simpler than testing is not None
            level = heading_match.group(1).count('#')
            # already captured the heading text - use it rather than hardcoding the start index
            line = f'<h{level}>' + heading_match.group(2) + f'</h{level}>'

        # Don't need to nest these tests to check for bold and italic
        # for both list items and paragraphs
        list_match = list_re.match(line)
        if list_match:
            curr = list_match.group(1)
            if not in_list:
                in_list = True
                line = '<ul><li>' + curr + '</li>'
            else:
                line = '<li>' + curr + '</li>'
        elif in_list:
            in_list_append = True
            in_list = False

        tag_match = tag.match(line)
        if not tag_match:
            line = '<p>' + line + '</p>'
        # Regex substitution is much simpler than the string manipulation
        line = bold.sub(r'<strong>\1</strong>', line)
        line = ital.sub(r'<em>\1</em>', line)
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res.append(line)
    if in_list:
        res.append('</ul>')
    return ''.join(res)
