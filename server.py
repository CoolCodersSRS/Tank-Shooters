import PodSixNet.Channel
import PodSixNet.Server
from time import sleep
class ClientChannel(PodSixNet.Channel.Channel):
    def Network(self,data):
        print(data)

class MainServer(PodSixNet.Server.Server):
    channelClass = ClientChannel
    def Connected(self,channel,addr):
        print ("New Connection:",channel)
        

print ("Starting server")
mainServe = MainServer(localaddr=("0.0.0.0", 8080))
while True:
    mainServe.Pump()
    sleep(0.01)
