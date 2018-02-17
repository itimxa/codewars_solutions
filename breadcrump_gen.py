""" You can find below solution for Kata 'Breadcrump Generator'
task for this Kata you can find on link below
https://www.codewars.com/kata/breadcrumb-generator """

import re
def generate_bc(url, separator):
    url = re.sub('\?[\w?=&.]+|/index\.[\w?=&.]+|\#\w+', '', url)  #search and replace anchors, parameters and index.
    url = url.replace('//', '').split('/')[1:]   #replace // so we can ignore protocols (http, https)
    ignore_words = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]
    if url and '' not in url:
        result = '<a href="/">HOME</a>'
    else:
        return '<span class="active">HOME</span>'
    for i in range(len(url)):
        if len(url[i]) > 30:
            dir_name = ''.join(j[0] for j in url[i].split('-') if j not in ignore_words)  #acronomizing words
        elif '-' in url[i]:
            dir_name = url[i].replace('-', ' ')
        else:
            dir_name = url[i]
        if i != len(url)-1:   #detect which element we need to use (<a>/<span>)
            result += '{0}<a href="/{1}/">{2}</a>'.format(separator,'/'.join(url[:i + 1]), dir_name.upper())
        else:
            result += '{0}<span class="active">{1}</span>'.format(separator, dir_name.split('.')[0].upper())
    return result

