# Twitch HLTB Bot
Ready to use simple Python bot to text HLTB game completion info in chat

It uses [ScrappyCocoo HowLongToBeat-PythonAPI](https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI) 
and [PythonistaGuild TiwtichIO](https://github.com/PythonistaGuild/TwitchIO).

## Usage
To launch bot download HLTB-bot.py and requirements.txt files. Fill your account or bot account token and channel name on which you would like to use bot
```python
    def __init__(self):
        super().__init__(
            token="YOUR_TOKEN",
            prefix="!",
            initial_channels=['CHOOSE_CHANNELS']
        )
```
Also you will need to instal [ScrappyCocoo HowLongToBeat-PythonAPI](https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI) and [PythonistaGuild TiwtichIO](https://github.com/PythonistaGuild/TwitchIO).
```python
pip install -r requirements.txt
```
or download them directly
```python
pip install twitchio==2.10.0 howlongtobeatpy
```
Notice that TwitchIO 3.0.0 and further versions stop supporting IRC, so updating it from 2.10 will break bot.
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
