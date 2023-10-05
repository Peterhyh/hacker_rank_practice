from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print('Start :', tag)
        for element in attr:
            print('->', element[0], '>', element[1])
    def handle_endtag(self, tag):
        print('End   :', tag)
    def handle_startendtag(self, tag, attr):
        print('Empty :', tag)
        for element in attr:
            print('->', element[0], '>', element[1])
        
lines = 2

parser = MyHTMLParser()

for _ in range(lines):
    parser.feed("<html><head><title>HTML Parser - I</title></head><body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>")