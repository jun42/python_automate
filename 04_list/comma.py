


def comma_code(spam):
    
    
    if len(spam) == 0:
        
        return print('blank')
    
    elif len(spam) == 1:
        
        return print(str(spam[0])) 
    
    elif len(spam) > 1:
        text = spam[0]
        for i, elem in enumerate(spam[1:]):
            
            if i == len(spam) - 2:
                text = text + ' and ' + elem
            else:
                text = text + ', ' + elem
            
        return print(text)
    
spam = ['apples', 'bananas', 'tofu', 'cats']
comma_code(spam)