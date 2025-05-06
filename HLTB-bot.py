import asyncio
import logging
import sqlite3

from howlongtobeatpy import HowLongToBeat

import asqlite
import twitchio
from twitchio import eventsub
from twitchio.authentication import ValidateTokenPayload
from twitchio.ext import commands
from pyexpat.errors import messages

import CREDENTIALS

LOGGER: logging.Logger = logging.getLogger("Unofficial_HLTB_Bot")

#Bot credentials, you can replace them with your strings, or create CREDENTIALS.py
#with following lines:
'''
CLIENT_ID:str="Your client id acquired from dev.twitch console"
CLIENT_SECRET:str="Your client secret acquired from dev.twitch console"
BOT_ID="Your bot name"
OWNER_ID="Channel to join"
'''
CLIENT_ID=CREDENTIALS.CLIENT_ID
CLIENT_SECRET=CREDENTIALS.CLIENT_SECRET
BOT_ID=CREDENTIALS.BOT_ID
OWNER_ID=CREDENTIALS.OWNER_ID


class HLTBBot(commands.Bot):
    def __init__(self,*,token_database: asqlite.Pool)-> None:
        self.token_database = token_database
        super().__init__(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            bot_id=BOT_ID,
            owner_id=OWNER_ID,
            prefix="!",
        )

    # async def setup_hook(self) -> None:
    #     await self.add_component(MyComponent(self))
    #
    #     subscription = eventsub.ChatMessageSubscription(broadcaster_user_id=OWNER_ID, user_id=BOT_ID)
    #     await self.subscribe_websocket(payload=subscription)

    async def add_token(self, token: str, refresh: str) -> twitchio.authentication.ValidateTokenPayload:
        resp: twitchio.authentication.ValidateTokenPayload = await super().add_token(token, refresh)

        query ="""
        INSERT INTO tokens (user_id, token, refresh)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id)
        DO UPDATE SET
            token = exclude.token,
            refresh = exclude.refresh;
        """
        async with self.token_database.acquire() as connection:
            await connection.execute(query, (resp.user_id, token, refresh))

        LOGGER.info("Added token to the database for user: %s",resp.user_id)
        return resp

    async def load_tokens(self, path: str | None = None, /) -> None:

        async  with self.token_database.acquire() as connection:
            rows: list[sqlite3.Row] = await connection.fetchall("""Select * from tokens""")

        for row in rows:
            await  self.add_token(row["token"], row["refresh"])

    async def setup_database(self)->None:
        query = """CREATE TABLE IF NOT EXISTS tokens(user_id TEXT PRIMARY KEY, token TEXT NOT NULL, refresh TEXT NOT NULL)"""
        async  with self.token_database.acquire() as connection:
            await connection.execute(query)

    async  def event_ready(self)-> None:
        LOGGER.info("Successfully logged in as: %s", self.bot_id )

class MyComponent(commands.Component):
    def __init__(self, bot: HLTBBot):
        self.bot = bot
    #Ping command check
    @commands.command(aliases=['pingHLTB','pinghltb','PingHLTB','Pinghltb',''])
    async def HLTB_ping(self, ctx):
        await ctx.send("Пинг ppHop Понг")

    #HLTB search command
    @commands.command(aliases=['HLTB'])
    async def hltb(self, ctx: commands.Context, *, game_name: str):
        results = await HowLongToBeat().async_search(game_name)

        if results is None or len(results) == 0:
            await ctx.send(f"Игра не найдена")
            return

        best_match = max(results, key=lambda  x: x.similarity)

        message = (
            f"Игра: {best_match.game_name} ({best_match.release_world}) | "
            f"Main Story: {best_match.main_story} ч. | "
            f"Completionist: {best_match.completionist} ч. | "
            f"Ссылка: {best_match.game_web_link}"
            )

        await  ctx.send(message)

def main() -> None:
    twitchio.utils.setup_logging(level=logging.INFO)

    async def runner() -> None:
        async  with asqlite.create_pool("tokens.db") as tdb, HLTBBot(token_database=tdb) as bot:
            await  bot.setup_database()
            await  bot.start()

    try:
        asyncio.run(runner())
    except KeyboardInterrupt:
        LOGGER.warning("Key interrupt")

if __name__ == "__main__":
    main()

