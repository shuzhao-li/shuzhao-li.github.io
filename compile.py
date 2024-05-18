import jinja2
from bibtex import convert_bibtext_file


def prepare_html(html_content, jinja_dict={}):
    '''
    Open and read html_content, then update by jinja_dict.
    Returns updated HTML text
    '''
    return html_content


# make index.html
def make_index_html(header, footer, body, target="docs/index.html"):
    new = prepare_html(open(header).read()
                ) + prepare_html(open(body).read()
                ) + prepare_html(open(footer).read()
                )
    with open(target, 'w') as F:
        F.write(new)
    
# make publications.html
def make_publications_html(header, footer, body, target="docs/publications.html"):
    
    new = prepare_html(open(header).read()
                ) + prepare_html(open(body).read()
                ) + prepare_html(open(footer).read()
                )
    with open(target, 'w') as F:
        F.write(new)

# make cv.html
def make_cv_html(header, footer, body, target="docs/cv.html"):
    
    new = prepare_html(open(header).read()
                ) + prepare_html(open(body).read()
                ) + prepare_html(open(footer).read()
                )
    with open(target, 'w') as F:
        F.write(new)

# make chinese.html
def make_chinese_html(header, footer, body, target="docs/chinese.html"):
    
    new = prepare_html(open(header).read()
                ) + prepare_html(open(body).read()
                ) + prepare_html(open(footer).read()
                )
    with open(target, 'w') as F:
        F.write(new)

# make posts.html
def make_posts_html(header, footer, body, target="docs/posts.html"):
    
    new = prepare_html(open(header).read()
                ) + prepare_html(open(body).read()
                ) + prepare_html(open(footer).read()
                )
    with open(target, 'w') as F:
        F.write(new)

# make _publications.htm


def main():
    
    # Convert Google Scholar exported bibtex to HTML
    with open("src/bibtex_publications.htm", 'w') as F:
        F.write(
            '''<div class="container-fluid text-left">\n''' +
            convert_bibtext_file("src/citations.txt") + '''\n</div>'''
        )
        
    make_index_html(
        header="src/_header.htm", footer="src/_footer.htm", body="src/_front.htm", 
        target="docs/index.html"
        )
    
    # May change how to generate publications
    make_publications_html(
        header="src/_header.htm", footer="src/_footer.htm", body="src/bibtex_publications.htm", 
        target="docs/publications.html"
        )
    make_posts_html(
        header="src/_header.htm", footer="src/_footer.htm", body="src/_underconstruction.htm", 
        target="docs/teaching.html"
        )
    
    make_cv_html(
        header="src/_header.htm", footer="src/_footer.htm", body="src/_underconstruction.htm", 
        target="docs/cv.html"
        )
    make_chinese_html(
        header="src/_header.htm", footer="src/_footer.htm", body="src/_underconstruction.htm",  
        target="docs/chinese.html"
        )
    make_posts_html(
        header="src/_header.htm", footer="src/_footer.htm", body="src/_underconstruction.htm", 
        target="docs/posts.html"
        )
    

if __name__ == '__main__':
    main()
