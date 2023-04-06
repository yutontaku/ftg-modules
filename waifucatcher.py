from .. import loader, utils


def register(cb):
    cb(WaifuCatcherMod())


class WaifuCatcherMod(loader.Module):
    """Module for WaifuCatcher autoplay"""
    def __init__(self):
        self.enabled = True
    strings = {"name": "WaifuCatcher"}
    async def enablecmd(self, message):
        '''enable autoplay'''
        self.enabled = True
        await message.edit('Enabled autoplay')
    async def disablecmd(self, message):
        '''disale autoplay'''
        self.enabled = False
        await message.edit('Disabled autoplay')
    @loader.watcher('in', from_id=1976201765)
    async def play(self, message):
        if self.enabled:
            if "Hey! You reached the maximum amount of 🎟" in message.text:
                await message.reply('/start')
                await message.reply('PLAY NOW! 💠')
                await message.reply('Play 1000🎟')
            elif "Click below to activate autoplay👇" in message.text:
                await message.click(0)
