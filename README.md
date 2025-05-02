# Twitch HLTB Bot
Ready to use simple Python bot to text HLTB game completion info in chat

It uses [ScrappyCocoo HowLongToBeat-PythonAPI](https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI) 
and [PythonistaGuild TiwtichIO](https://github.com/PythonistaGuild/TwitchIO).

## Usage
### Launching
To launch bot download HLTB-bot.py and requirements.txt files. Fill your account or bot account token and channel name on which you would like to use bot
```python
    def __init__(self):
        super().__init__(
            token="YOUR_TOKEN",
            prefix="!",
            initial_channels=['CHOOSE_CHANNELS']
        )
```
You can get token from [twitchtokengenerator](https://twitchtokengenerator.com/) made by [swiftyspiffy](https://github.com/swiftyspiffy/)
### Chat usage
To get game info type in chat
```
!hltb GAME_NAME
```
Bot will answer in format
```
Game: GAME_NAME (YEAR) | Main Story HH (in decimal format) | Completionist HH (in decimal format) | Link: GAME_LINK
```
## Requirements
For bot work you will need at least python 3.10 and to install [ScrappyCocoo HowLongToBeat-PythonAPI](https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI) and [PythonistaGuild TiwtichIO](https://github.com/PythonistaGuild/TwitchIO).
```python
pip install -r requirements.txt
```
or download them directly
```python
pip install twitchio==2.10 howlongtobeatpy
```
Notice that TwitchIO 3.0.0 and further versions stoped supporting IRC, so updating it from 2.10 will break bot.
## About Issues, Discussions and PR
If you found a bug please report it by creating an [issue](https://github.com/SomeNameSomeSurname/Twitch-HLTB-Bot/issues).

If you whilling to add feature, or have an idea for feature you can open discussion or [PR](https://github.com/SomeNameSomeSurname/Twitch-HLTB-Bot/pulls)
## Special thanks
To ScrappyCocco for great HLTB API

To PythonistaGuild for library for the twitch API

To Refferency for the idea of the bot

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
