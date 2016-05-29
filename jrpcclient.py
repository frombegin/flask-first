from flask_jsonrpc.proxy import ServiceProxy

server = ServiceProxy('http://localhost:5000/api')
s = server.time.now()
print(s)
print(s.get('result', ''))
print(s.get('error', ''))
