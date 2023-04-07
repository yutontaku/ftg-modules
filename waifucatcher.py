from .. import loader, utils
from asyncio import sleep

def register(cb):
    cb(WaifuCatcherMod())


class WaifuCatcherMod(loader.Module):
    """Module for WaifuCatcher autoplay"""
    def __init__(self):
        self.enabled = True
        self.day = False
    strings = {"name": "WaifuCatcher"}
    async def catchcmd(self, message):
        '''disable/enable autoplay'''
        self.enabled = not self.enabled
        await message.edit('Autoplay mode is turned on' if self.enabled else 'Autoplay mode is turned off')
    @loader.watcher('in', from_id=1976201765)
    async def play(self, message):
        if self.enabled:
            if "Hey! You reached the maximum amount of 🎟" in message.text:
                await message.client.send_message(1976201765, '/start')
                await message.client.send_message(1976201765, 'PLAY NOW! 🎟')
                await message.client.send_message(1976201765, 'Play 1000🎟')
            elif "Click below to activate autoplay👇" in message.text:
                await message.click(0)
    async def daycmd(self, message):
        '''enable/disable day reward'''
        self.day = not self.day
        await message.edit('day reward mode is turned on' if self.day else 'day reward mode is turned off')
        while self.day:
        	await message.client.send_message(1976201765, "/start")
        	await sleep(20)
        	await message.client.send_message(1976201765, "Rewards 🎁")
        	await sleep(20)
        	await message.client.send_message(1976201765, "Daily Login 🌟")
        	await sleep(5)
        	await message.client.send_message(1976201765, "Back 🔙")
        	await sleep(86400)