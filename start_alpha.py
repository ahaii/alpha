from gevent import monkey
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from alpha.wsgi import application

monkey.patch_all()

print('Alpha is running ......')

ws_server = WSGIServer(
    ('0.0.0.0', 8000),
    application,
    log=None,
    handler_class=WebSocketHandler
)

try:
    ws_server.serve_forever()
except KeyboardInterrupt:
    print('服务器关闭......')
    pass

