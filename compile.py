import time
import jinja2
from bibtex import convert_bibtext_file
from get_posts import get_posts_from_dir

def prepare_html(html_content, d={}):
    '''
    Open and read html_content, then update by jinja_dict.
    Returns updated HTML text
    '''
    env = jinja2.Environment()
    template = env.from_string(html_content)
    return template.render(d)

# make html
def concatenate_html(header, footer, body, body_dict={}, target="docs/index.html"):
    '''
    header, footer are prepared separately.
    body and body_dict are used to template new content.
    '''
    new = header + prepare_html(
                        open(body).read(), body_dict
                            ) + footer
    with open(target, 'w') as F:
        F.write(new)
    

def main():
    
    header = prepare_html(open("src/_header.htm").read(), {})
    footer = prepare_html(open("src/_footer.htm").read(), {'time_record': time.ctime()})
    # will make more generic later
    list_articles = get_posts_from_dir()
    
    # Convert Google Scholar exported bibtex to HTML
    with open("src/bibtex_publications.htm", 'w') as F:
        F.write(
            '''<div class="container-fluid text-left"><p>
            <h4>Publications</h4>
            <ul> 
            <li><a href="https://scholar.google.com/citations?user=lNBq0asAAAAJ&hl=en">Google Scholar</a></li>
            <li><a href="https://pubmed.ncbi.nlm.nih.gov/?term=shuzhao+li&sort=date">PubMed</a></li>
            </ul>
            </p></div>''' + 
            '''<div class="container-fluid text-left">\n''' +
            convert_bibtext_file("src/citations.txt") + '''\n</div>'''
        )
        
    # with open("src/xx.htm", 'w') as F:
    #    F.write()
        
    concatenate_html(
        header, footer, 
        body="src/_front.htm", body_dict={},
        target="docs/index.html"
        )
    
    # May change how to generate publications
    concatenate_html(
        header, footer, body="src/bibtex_publications.htm", body_dict={},
        target="docs/publications.html"
        )
    
    # make teaching.html
    concatenate_html(
        header, footer, body="src/_underconstruction.htm", body_dict={},
        target="docs/teaching.html"
        )
    
    # make cv.html
    concatenate_html(
        header, footer, body="src/_underconstruction.htm", body_dict={},
        target="docs/cv.html"
        )
    
    # make chinese.html
    concatenate_html(
        header, footer, body="src/_chinese.htm",  body_dict={'articles': list_articles},
        target="docs/chinese.html"
        )
    
    # make posts.html
    concatenate_html(
        header, footer, body="src/_posts.htm", body_dict={},
        target="docs/posts.html"
        )
    

if __name__ == '__main__':
    main()
