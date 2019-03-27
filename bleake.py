import asyncio
from bleak import BleakClient

address = "D8:47:AB:04:8A:78"
MODEL_NBR_UUID = "0000aadc-0000-1000-8000-00805f9b34fb"




class GiikerMove():
    def __init__(self, value):
        face = value // 16
        amount = value % 16

        self.face = ["?", "B", "D", "L", "U", "R", "F"][face]
        


def change_handle(sender, data):
	print(data)



async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        value = await client.read_gatt_char(MODEL_NBR_UUID)



        print("len : ", len(value))
        print("Model Number: {0}".format("".join(map(chr, value))))
        recent_moves = list(map(GiikerMove, value[16:]))
        last_move = recent_moves[0]
        print(last_move.face)
        await client.start_notify(MODEL_NBR_UUID, change_handle)
        while True:
        	await asyncio.sleep(5)


loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))




        
        










