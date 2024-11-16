import board
import digitalio
from DFPlayer import DFPlayer
import asyncio
import busio
import pwmio
import json
import random
import time

class grad9000():
    def __init__(self):
        self.busy = digitalio.DigitalInOut(board.D1)
        self.uart = busio.UART(tx=board.D6, rx=board.D7, baudrate=9600)
        self.dfp = DFPlayer(self.uart, volume=70)
        self.redled = pwmio.PWMOut(board.D3, frequency=25000, duty_cycle=0)
        self.greenled = pwmio.PWMOut(board.D2, frequency=25000, duty_cycle=0)
        with open('audios.json') as json_file:
            self.audios = json.load(json_file)
            
    async def start(self, wait_time):
        max = 100
        max_2 = max*max
        for i in range(max):
            self.redled.duty_cycle = int(32000*(i*i/max_2))
            await asyncio.sleep_ms(int(wait_time/max))    

    async def blink(self, led, wait_time, duty = 65535):
        led.duty_cycle = duty
        await asyncio.sleep_ms(int(wait_time/2))   
        led.duty_cycle = 0
        await asyncio.sleep_ms(int(wait_time/2))

    async def perma_blink(self, led, wait_time, duty):
        while True:
            await self.blink(led, wait_time, duty)

    async def random_blink(self, led, wait_time, segments = 5):
        for i in range(segments):
            duty = random.randint(10000,40000)
            led.duty_cycle = duty
            await asyncio.sleep_ms(int(wait_time/segments))

    def get_folder_name_from_id(self, id):
        return next((item for item in self.audios if self.audios[item].get('id') == id))
    
    def get_song_dict_from_id(self, folder, id):
        return next((item for item in self.audios[folder]['canciones'] if item.get('id') == id))
    
    def play(self, folder, song):
        if isinstance(folder, int) and isinstance(song, int):
            self.dfp.play(folder,song)
            folder_name = self.get_folder_name_from_id(folder)
            song_item = self.get_song_dict_from_id(folder_name, song)
            return song_item['duracion']
        if isinstance(folder, str) and isinstance(song, str):
            song_item = next((item for item in self.audios[folder]['canciones'] if item["nombre"] == song), None)
            self.dfp.play(self.audios[folder]['id'], song_item['id'])
            return song_item['duracion']
        
    def play_random(self, folder):
        folder_name = self.get_folder_name_from_id(folder)
        dur = self.play(folder, random.randint(1,len(self.audios[folder_name]['canciones'])-1))
        return dur

    def pause(self):
        self.dfp.pause()
        
async def main():
    hal = grad9000()
    await hal.start(1000)
    dur = hal.play_random(1)
    print(dur)
    await hal.random_blink(hal.greenled, int(dur*1000), 10)
if __name__ == "__main__":
    asyncio.run(main())