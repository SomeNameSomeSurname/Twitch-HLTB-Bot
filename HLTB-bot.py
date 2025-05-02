from howlongtobeatpy import HowLongToBeat
import twitchio
from pyexpat.errors import messages
from twitchio.ext import commands
import asyncio

class HLTBBot(commands.Bot):
    def __init__(self):
        super().__init__(
            token="YOUR_TOKEN", #paste here you token
            prefix="!", #You can keep it, or change for any other
            initial_channels=['CHOOSE_CHANNELS'] #channels that you want to work with
        )

    async def event_ready(self):
        pass

    #Ping command check
    @commands.command(name='pingHLTB')
    async def ping_command(self, ctx):
        await ctx.send("Ping ppHop Pong")

    #HLTB search command
    @commands.command(name='hltb')
    async def hltv_command(self, ctx, *, game_name: str):
        try:
            results = await HowLongToBeat().async_search(game_name)

            if results is None or len(results) == 0:
                await ctx.send(f"No game found")
                return

            best_match = max(results, key=lambda  x: x.similarity)

            #Comment section of the match if needed
            message = (
                f"Game: {best_match.game_name} ({best_match.release_world}) | "
                f"Main Story: {best_match.main_story} H. | "
                f"Completionist: {best_match.completionist} H. | "
                f"Link: {best_match.game_web_link}"
            )

            await  ctx.send(message)

        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("I'm broken oh ")

if __name__ == "__main__":
    bot = HLTBBot()
    bot.run()

