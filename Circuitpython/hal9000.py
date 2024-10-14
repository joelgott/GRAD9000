import board
import digitalio
from DFPlayer import DFPlayer
import asyncio
import busio
import pwmio
import json
import random

class HAL9000():
    def __init__(self):
        self.busy = digitalio.DigitalInOut(board.D1)
        self.uart = busio.UART(tx=board.D6, rx=board.D7, baudrate=9600)
        self.dfp = DFPlayer(self.uart)
        self.redled = digitalio.DigitalInOut(board.D2)
        self.greenled = pwmio.PWMOut(board.D3, frequency=25000, duty_cycle=0)
        with open('audios.json') as json_file:
            self.audios = json.load(json_file)       
    
    def play(self, folder, song):
        if isinstance(folder, int) and isinstance(song, int):
            self.dfp.play(folder,song)
            folder_name = next((item for item in self.audios if self.audios[item].get('id') == folder))
            song_item = next((item for item in self.audios[folder_name]['canciones'] if item.get('id') == song))
            return song_item['duracion']
        if isinstance(folder, str) and isinstance(song, str):
            song_item = next((item for item in self.audios[folder]['canciones'] if item["nombre"] == song), None)
            self.dfp.play(self.audios[folder]['id'], song_item['id'])
            return song_item['duracion']
        
    async def blink(self, wait_time):
        self.greenled.duty_cycle = 32768
        await asyncio.sleep_ms(wait_time)   
        self.greenled.duty_cycle = 0
            
    def play_random(self, folder):
        pass

    def pause(self):
        self.dfp.pause()

    async def play_light(self):
        while True:
            if self.busy.value:
                await self.blink(random.randint(200,1000))
                await asyncio.sleep_ms(random.randint(200,1000))
        
async def main():
    hal = HAL9000()
    asyncio.create_task(hal.play_light())
    folder = 'memes'
    for i in hal.audios[folder]['canciones']:
        folder_id = hal.audios[folder]['id']
        song_id = i['id']
        print('folder id = {}, song id = {}'.format(folder_id, song_id))
        dur = hal.play(int(folder_id),int(song_id))
        print(dur)
        await asyncio.sleep_ms(int(dur*1000))    

if __name__ == "__main__":
    asyncio.run(main())