def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])
    url_path = environ['url_path']
    if url_path == '/index.py':
        body = 'Index Page ...'
    elif url_path == '/center.py':
        body = 'Center Page ...'
    else:
        body = 'Other Page ...'
    return body + '<br>人生苦短<br>我用Python'


