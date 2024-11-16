import pwmio
import asyncio
import board
import random

async def blink(led, wait_time, duty = 65535):
    led.duty_cycle = duty
    await asyncio.sleep_ms(int(wait_time/2))   
    led.duty_cycle = 0
    await asyncio.sleep_ms(int(wait_time/2))

async def perma_blink(led, wait_time, duty):
    while True:
        await blink(led, wait_time, duty)

async def random_blink(led, wait_time, segments = 5):
    for i in range(segments):
        duty = random.randint(10000,40000)
        led.duty_cycle = duty
        await asyncio.sleep_ms(int(wait_time/segments))

async def start(led, wait_time):
    maxcicles = 100
    max_2 = maxcicles*maxcicles
    for i in range(maxcicles):
        led.duty_cycle = int(32000*(i*i/max_2))
        await asyncio.sleep_ms(int(wait_time/maxcicles))

async def main():
    redled = pwmio.PWMOut(board.D3, frequency=25000, duty_cycle=0, variable_frequency=True)
    greenled = pwmio.PWMOut(board.D2, frequency=25000, duty_cycle=0, variable_frequency=True)  
    #await blink(greenled,500)
    await start(redled,1000)
    
    #asyncio.create_task(perma_blink(greenled,200, 20000))
    #await asyncio.sleep_ms(5000) 
    await random_blink(greenled, 2000, 20)

if __name__ == "__main__":
    asyncio.run(main())