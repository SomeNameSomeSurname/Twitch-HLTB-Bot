# Twitch HLTB Bot
Python bot to text HLTB game completion info in chat

It uses [ScrappyCocoo HowLongToBeat-PythonAPI](https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI) 
and [PythonistaGuild TiwtichIO](https://github.com/PythonistaGuild/TwitchIO) v3.

## Usage
### Initial setup
1.) To launch bot download HLTB-bot.py, requirements.txt and Get_IDs.py files. Fill your ClientID and Client Secret in CREDENTAILS.py
You can get them by registering your app on twitch [here](dev.twitch.com).
2.) In Get_IDs.py enter your channel name and channel name of your bot. Example:
```python
async def main() -> None:
    async with twitchio.Client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET) as client:
        await client.login()
        user = await client.fetch_users(logins=["YOUR_CHANNEL_NAME", "BOTS_CHANNEL_NAME"])
        for u in user:
            print(f"User: {u.name} - ID: {u.id}")
```
After runnning your ids will be output in console, write them in credentials.
3.) Comment setup_hook section and run. Visit http://localhost:4343/oauth?scopes=user:read:chat%20user:write:chat%20user:bot , while being logged on twitch with your BOT ACCOUNT. Then visit http://localhost:4343/oauth?scopes=channel:bot while while being logged on twitch with your MAIN ACCOUNT.
4.) Rerun programm
### Chat usage
To get game info type in chat
```
!hltb GAME_NAME
```
Bot will answer in format
```
Game: GAME_NAME (YEAR) | Main Story HH (in decimal format) h. | Completionist HH (in decimal format) h. | Link: GAME_LINK
```
## Requirements
For bot work you will need at least python 3.10 and to install [ScrappyCocoo HowLongToBeat-PythonAPI](https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI) and [PythonistaGuild TiwtichIO](https://github.com/PythonistaGuild/TwitchIO).
```python
pip install -r requirements.txt
```
or download them directly
```python
pip install twitchio howlongtobeatpy
```
## About Issues, Discussions and PR
TwitchIOv3 IMHO is still raw, so with updates something can be changed which can result in breaking bot.

If you found a bug please report it by creating an [issue](https://github.com/SomeNameSomeSurname/Twitch-HLTB-Bot/issues).

If you whilling to add feature, or have an idea for feature you can open discussion or [PR](https://github.com/SomeNameSomeSurname/Twitch-HLTB-Bot/pulls)
## Special thanks
To ScrappyCocco for great HLTB API

To PythonistaGuild for library for the twitch API

To Refferency for the idea of the bot

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
