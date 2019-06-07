import socket, traceback

import matplotlib.pyplot as plt
import numpy as np

host = ''
port = 5555
pointLimit = 10
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

#plt.ion() ## Note this correction
fig=plt.figure()
plt.axis([-10,20,-10,20])

i=0
x=list()
y=list()

def addData(pointArray, newData):
  pointArray.append(newData)
  print(pointArray.__len__())
  if pointArray.__len__() > pointLimit:
    pointArray.pop(0)
  return pointArray

while 1:
  try:
    message, address = s.recvfrom(8192)
    print (message)
    message = message.decode('UTF-8')
    points = message.split(',')
    print(points[2]+' , '+points[3])
    addData(x, points[2]);
    addData(y, points[3]);
    plt.scatter(x, y);
    plt.show()
    plt.pause(0.0001)
  except (KeyboardInterrupt, SystemExit):
    break
  except:
    traceback.print_exc()
