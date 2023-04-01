import re
BOLD = r'__(.*?)__', r'<strong>\1</strong>'
ITALIC = r'_(.*?)_', r'<em>\1</em>'
LIST = re.compile(r'^\* (.*)', re.M), r'<li>\1</li>'
END_LIST = re.compile(r"(<li>.*</li>)", re.S), r"<ul>\1</ul>"
HEADER = ((re.compile(r'^%s (.+)' % ('#' * i)), r'<h{0}>\1</h{0}>'.format(i))
          for i in range(6, 0, -1))
PARAGRAPH = re.compile(r'^(?!<h|<li|<ul)(.*)', re.M), r'<p>\1</p>'
FLAT_TEXT = r'\n', r''
OP = BOLD, ITALIC, LIST, END_LIST, *HEADER, PARAGRAPH, FLAT_TEXT
def parse(md: str) -> str: return [md := re.sub(*op, md) for op in OP][-1]