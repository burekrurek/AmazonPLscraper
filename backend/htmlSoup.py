class htmlSoup:
    def __init__(self, raw_html):
        self.html = raw_html
        
    
    #returns an index of text of a selector we're looking for, for example <span
        
    def findString(self, html_class):
            x = self.html
            if html_class[0] == ".":
                html_class = html_class[1:]

            class_begin = x.find(f'{html_class}')
            text_start = x.find(f'>', class_begin)
            text_end = x.find(f'<', text_start + 1)
            
            return x[text_start+1:text_end]

