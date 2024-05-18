'''
Convert bibtext to HTML elements.

Example input:
@article{pulendran2010systems,
  title={Systems vaccinology},
  author={Pulendran, Bali and Li, Shuzhao and Nakaya, Helder I},
  journal={Immunity},
  volume={33},
  number={4},
  pages={516--529},
  year={2010},
  publisher={Elsevier}
}

Example output:

'''

required = ['author', 'title', 'journal', 'volume', 'pages', 'year']

def format_dict_div(d):
    tempalte_left = '''<div class="panel panel-default"><div class="panel-body">
    '''
    tempalte_right = '''
    </div></div>
    '''
    r = '<p><b>' + d['year'] + '</b> ' + d['author'].replace('and', '|') + '</p>'
    r += '<p><i>' + d['title'] + '</i></p><p>'
    r += ', '.join([d[x] for x in [
        'journal', 'volume', 'pages', 'year'
    ]]) + '</p>'
    return tempalte_left + r + tempalte_right

def convert_entry(bibtext, required=required):
    '''returns HMTL
    '''
    d = {}
    LL = [line.strip() for line in bibtext.splitlines()[1:] if len(line)>3]
    for line in LL:
        try:
            a, b = line.split('={')
            b = b.replace('},', '').replace('}', '')
            d[a] = b
            if a == 'booktitle':
                d['journal'] = b
        except ValueError:
            print(LL[0], line)
    for x in required:
        if x not in d:
            d[x] = ''
    return format_dict_div(d)
    
def convert_bibtext_file(file):
    LL = open(file).read().split('@')
    r = ''
    for L in LL:
        r += convert_entry(L) + '\n'
    return r
