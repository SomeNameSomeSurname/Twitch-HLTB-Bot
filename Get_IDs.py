import asyncio
import twitchio
import CREDENTIALS

CLIENT_ID=CREDENTIALS.CLIENT_ID
CLIENT_SECRET=CREDENTIALS.CLIENT_SECRET

async def main() -> None:
    async with twitchio.Client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET) as client:
        await client.login()
        user = await client.fetch_users(logins=["refferency", "unofficial_hltb_bot"])
        for u in user:
            print(f"User: {u.name} - ID: {u.id}")

if __name__ == "__main__":
    asyncio.run(main())