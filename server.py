import os
import pickle
import socket


def server(so):
  data = so.recv(1024)

  obj = pickle.loads(data)

  c.send("Ob try again ;) \n")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 4444))
sock.listen(2)

while True:
  c, a = sock.accept()

  if(os.fork() == 0):
      c.send("accepted connection from %s:%d" % (a[0], a[1]))
      server(c)
      exit(1)
