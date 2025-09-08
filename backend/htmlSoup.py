class htmlSoup:
    def __init__(self, raw_html):
        self.html = raw_html
        
    
    #returns an index of text of a selector we're looking for, for example <span
    def lookFor(self, selector):
        x = self.html
        try:
            beginning = x.find(f'<{selector}')
            if beginning[-1] != '>': 
                end = x.find('>', beginning)
            else:
            
            #this shit doesnt work if its a nested one, instead lets just look for the one sign, and not the selector exactly
            #beginning_2 = x.find(f'</{selector}>', end)
                beginning_2 = x.find('<', end)
            
            
            return x[end+1:beginning_2]
            
        
        except Exception as e:
            return e
        
    def findByClassOrId(self, html_class):
        x = self.html
        if html_class[0] == ".":
            html_class = html_class[1:]

        class_begin = x.find(f'{html_class}')
        text_start = x.find(f'>', class_begin)
        text_end = x.find(f'<', text_start + 1)
        
        return x[text_start+1:text_end]
        
