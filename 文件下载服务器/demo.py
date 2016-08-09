在当前目录下，把文件打包成.tar.gz文件

启动：
python -m SimpleHTTPServer

打开浏览器即可下载文件列表。



###源码#####


import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
