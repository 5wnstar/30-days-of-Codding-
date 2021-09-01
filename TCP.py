# 30-days-of-Codding
#DAY 1 TCP CONNECTION
import socket 
target_host= "www.facebook.com"
target_port= 80, 443
#creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# connecting the client
client.connect((target_host,target_port))
# sending some data
cient.send("GET / HTTP/1.1\r\nHost: facebook.com\r\n\r\n")
# receiving  some data
reply = client.recv(4096) 
print reply 
