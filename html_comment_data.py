from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' not in data:
            print(f'>>> Single-line Comment\n{data}')
        else:
            print(f'>>> Multi-line Comment\n{data}')
        
    def handle_data(self, data):
        if data != '\n':
            print(f'>>> Data\n{data}')
        
  
lines = 4
html = ""

for _ in range(lines):
    html += input().rstrip() #insert HTML here
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()