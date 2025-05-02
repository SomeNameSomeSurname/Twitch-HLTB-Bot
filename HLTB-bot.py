from howlongtobeatpy import HowLongToBeat
import twitchio
from pyexpat.errors import messages
from twitchio.ext import commands
import asyncio

class HLTBBot(commands.Bot):
    def __init__(self):
        super().__init__(
            token="YOUR_TOKEN",
            prefix="!",
            initial_channels=['CHOOSE_CHANNELS']
        )

    async def event_ready(self):
        pass

    @commands.command(name='pingHLTB')
    async def ping_command(self, ctx):
        await ctx.send("Ping ppHop Pong")

    @commands.command(name='hltb')
    async def hltv_command(self, ctx, *, game_name: str):
        try:
            results = await HowLongToBeat().async_search(game_name)

            if results is None or len(results) == 0:
                await ctx.send(f"Нет игры NuAHule")
                return

            best_match = max(results, key=lambda  x: x.similarity)

            message = (
                f"Игра: {best_match.game_name} ({best_match.release_world}) | "
                f"Main Story: {best_match.main_story} ч. | "
                f"Completionist: {best_match.completionist} ч. | "
                f"Link: {best_match.game_web_link}"
            )

            await  ctx.send(message)

        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("Я поломался oh ")

if __name__ == "__main__":
    bot = HLTBBot()
    bot.run()

