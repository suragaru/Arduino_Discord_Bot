# Discord Bot Project

<!-- Badges -->
<p>
  <a href="https://github.com/suragaru/Arduino_Discord_Bot/network/members">
    <img src="https://img.shields.io/github/forks/suragaru/Arduino_Discord_Bot" alt="forks" />
  </a>
  <a href="https://github.com/suragaru/Arduino_Discord_Bot/stargazers">
    <img src="https://img.shields.io/github/stars/suragaru/Arduino_Discord_Bot" alt="stars" />
  </a>
  <a href="https://github.com/suragaru/Arduino_Discord_Bot/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/suragaru/Arduino_Discord_Bot" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/suragaru/Arduino_Discord_Bot" alt="last update" />
  </a>
  <a href="https://github.com/suragaru/Arduino_Discord_Bot/issues/">
    <img src="https://img.shields.io/github/issues/suragaru/Arduino_Discord_Bot" alt="open issues" />
  </a>  
  <a href="https://github.com/suragaru/Arduino_Discord_Bot/blob/main/LICENSE.md">
    <img src="https://img.shields.io/github/license/suragaru/Arduino_Discord_Bot.svg" alt="open issues" />
  </a>  
</p>

This Discord bot allows users to control relays via serial communication with a microcontroller. The bot is built using the [discord.py](https://github.com/Rapptz/discord.py) library and communicates with the microcontroller using the `pyserial` library.

---

## Buy me a coffee

Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this :)

<!---<a href="https://www.buymeacoffee.com/igorantun" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>--->

<a href="https://ko-fi.com/suragarucoffee"> <img src="https://cdn.ko-fi.com/cdn/kofi3.png?v=3" alt="Buy Me A Coffee" height="40" width="auto"/></a>

---

## Features
- **Relay Control**: Turn on/off relays via Discord commands.
- **Help Command**: Provides a list of available commands and their functions.

![image](https://github.com/user-attachments/assets/00673070-8c9a-4131-8938-64826f00552f)


## :toolbox: Setup

## Requirements

- Python 3.8+
- [discord.py](https://pypi.org/project/discord.py/) library
- [pyserial](https://pypi.org/project/pyserial/) library
- Microcontroller with relays connected to the serial port
  
### Wiring

### Installation

1. Clone the Repository
   ```bash
   git clone https://github.com/suragaru/Arduino_Discord_Bot.git
   cd discord-relay-bot
   ```

2. Install dependencies:
   ```bash
   pip install discord.py pyserial`
   ```

4. Set Up the Bot
Replace `"DISCORD_TOKEN_HERE"` with your bot's token in the `client.run("DISCORD_TOKEN_HERE")` line.

5. Run the bot
`python bot.py`
- After the bot works, modify the script if you want to add more functions to the bot.

### Serial Communication
The bot sends commands to the microcontroller via the serial port specified in the code (COM3 in this case). Make sure to update the serial port according to your system's configuration.

### Contributing
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

## License
>You can check out the full license [here](https://github.com/suragaru/Arduino_Discord_Bot/blob/main/LICENSE.md)

This project is licensed under the terms of the **MIT** license.



