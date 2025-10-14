'''
Extract posts

To-do: Create blog style posts from plain text files. 
Generate list of contents from directory of text files.

'''

import os

def parse_article(text_file):
    '''
    return title and content
    '''
    t = open(text_file).readlines()
    title = t[0].rstrip()
    content = '<p>' + '</p><p>'.join(t[2:]) + '</p>'
    return (title, content)

# will make more generic later
def get_posts_from_dir(dir='text/', prefix_filter='.txt'):
    files = os.listdir(dir)
    list_articles = []
    for f in files:
        if not f.endswith(prefix_filter):
            continue
        title, content = parse_article(dir + f)
        list_articles.append(
            {'title': title,
             'content': content}
        )
        
    return list_articles