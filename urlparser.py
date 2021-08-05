from urllib.parse import urlparse, parse_qs

#parses video id from given youtube link adopted from https://gist.github.com/kmonsoor/2a1afba4ee127cce50a0
def parse_vid_id(link):
        if link.startswith(('youtu', 'www')):
                link = 'http://' + link
        
        query = urlparse(link)
        if 'youtube' in query.hostname:
                if query.path == '/watch':
                        return parse_qs(query.query)['v'][0]
                elif query.path.startswith(('/embed/', '/v/')):
                        return query.path.split('/')[2]
                elif 'youtu.be' in query.hostname:
                        return query.path[1:]
                else:
                        raise ValueError