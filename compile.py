import time
import jinja2
from bibtex import convert_bibtext_file

def prepare_html(html_content, d={}):
    '''
    Open and read html_content, then update by jinja_dict.
    Returns updated HTML text
    '''
    env = jinja2.Environment()
    template = env.from_string(html_content)
    return template.render(d)

# make html
def concatenate_html(header, footer, body, target="docs/index.html"):
    new = header + prepare_html(open(body).read()) + footer
    with open(target, 'w') as F:
        F.write(new)
    

def main():
    
    header = prepare_html(open("src/_header.htm").read(), {})
    footer = prepare_html(open("src/_footer.htm").read(), {'time_record': time.ctime()})
    
    # Convert Google Scholar exported bibtex to HTML
    with open("src/bibtex_publications.htm", 'w') as F:
        F.write(
            '''<div class="container-fluid text-left">\n''' +
            convert_bibtext_file("src/citations.txt") + '''\n</div>'''
        )
        
    concatenate_html(
        header, footer, 
        body="src/_front.htm", 
        target="docs/index.html"
        )
    
    # May change how to generate publications
    concatenate_html(
        header, footer, body="src/bibtex_publications.htm", 
        target="docs/publications.html"
        )
    
    # make teaching.html
    concatenate_html(
        header, footer, body="src/_underconstruction.htm", 
        target="docs/teaching.html"
        )
    
    # make cv.html
    concatenate_html(
        header, footer, body="src/_underconstruction.htm", 
        target="docs/cv.html"
        )
    # make chinese.html
    concatenate_html(
        header, footer, body="src/_underconstruction.htm",  
        target="docs/chinese.html"
        )
    # make posts.html
    concatenate_html(
        header, footer, body="src/_posts.htm", 
        target="docs/posts.html"
        )
    

if __name__ == '__main__':
    main()
