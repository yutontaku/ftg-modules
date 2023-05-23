from .. import loader, utils
from asyncio import sleep

def register(cb):
    cb(WaifuCatcherMod())


class WaifuCatcherMod(loader.Module):
    """Module for WaifuCatcher autoplay"""
    def __init__(self):
        self.catch = True
        self.day = False
    strings = {"name": "WaifuCatcher"}
    async def catchcmd(self, message):
        '''disable/enable autoplay'''
        self.catch = not self.catch
        await message.edit('Autoplay mode is turned on' if self.catch else 'Autoplay mode is turned off')
    @loader.watcher('in', from_id=1976201765)
    async def play(self, message):
        if self.catch:
            if "Hey! You reached the maximum amount of 🎟" in message.text:
                await message.client.send_message(1976201765, '/start')
            elif "Main Menu" in message.text:
                await message.client.send_message(1976201765, 'PLAY NOW! 💠')
            elif "✨💠 SPECIAL BANNER 💠✨" in message.text:
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
    async def achievementscmd(self, message):
        '''Auto-claim your achievements'''
        await message.edit('Claiming achivements')
        await message.client.send_message(1976201765, "/start")
        await sleep(5)
        await message.client.send_message(1976201765, "Rewards 🎁")
        await sleep(7)
        await message.client.send_message(1976201765, "Achievements 🏆")
    @loader.watcher('in', from_id=1976201765)
    async def achives(self, message):
    	if 'Achievements' in message.text:
            try:
                id = message.id
                msg = await message.client.get_messages(entity=1976201765, max_id=id + 1, min_id=id - 1)
                msg[0].click(1)
            except Exception:
                pass
