# Gerrit van Rensburg A.K.A Hadreezy



import bottle
import os


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00ff02',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'This year it\'s real'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'move': 'west',
        'taunt': 'battlesnake-python!'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }






# Inserting An Assortment of Wall Detection and Avoidance Code

# Checks if desired coordinate is a wall -- https://github.com/jennifertigner/battlesnake-2016/blob/master/app/main.py
def isWall(data, coord):
    #check if coord is out of bounds
    if coord[0] < 0 or coord[1] < 0:
        return True
    elif coord[0] >= data['width'] or coord[1] >= data['height']:
        return True
    else:
return False





# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
