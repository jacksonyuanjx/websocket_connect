import time
import asyncio
import websockets
import time
import multiprocessing
from my_queue import MyQueue


class BCTWSConnection(multiprocessing.Process):
    def __init__(self, UDID, token, url="realtime.bluecitytechnology.com", cacheSize=10):

        self.UDID = UDID
        self.token = token
        self.url = url
        self.frames = MyQueue()
        self.cacheSize = cacheSize

        super().__init__(None)

        self.start()

    def run(self):
        asyncio.get_event_loop().run_until_complete(
            self.connectToServer('wss://{}'.format(self.url), self.UDID, self.token))

    async def connectToServer(self, uri, UDID, token):
        # print(UDID)
        # print(uri+"/ws/realtime/{}/".format(UDID))
        while True:
            try:
                async with websockets.connect(uri+"/ws/realtime/{}/".format(UDID), extra_headers={"token": token, "UDID": UDID}) as websocket:
                    print('----BCT realtime service---- Connected.')
                    while True:
                        # print('---- first line')
                        res = await websocket.recv()
                        # print('---- after webcoekt.recv()')
                        # print("----", self.frames.qsize())
                        if self.frames.qsize() > self.cacheSize:
                            # print('---- inside if stmt')
                            self.get()
                        # print('--- after if stmt')
                        self.frames.put(res)
            except:
                print(
                    '----BCT realtime service---- Connection failed. Retry to connect in 2 seconds.')
                time.sleep(2)

    def get(self):
        return self.frames.get()


if __name__ == "__main__":
    c_ = BCTWSConnection("YOUR UDID", "YOUR TOKEN")
    while True:
        f_ = c_.get()
        print(f_)