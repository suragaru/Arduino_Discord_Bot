# Discord Bot Project

<!-- Badges -->
<p>
  <a href="https://github.com/suragaru/shizuka_app/network/members">
    <img src="https://img.shields.io/github/forks/suragaru/shizuka_app" alt="forks" />
  </a>
  <a href="https://github.com/suragaru/shizuka_app/stargazers">
    <img src="https://img.shields.io/github/stars/suragaru/shizuka_app" alt="stars" />
  </a>
  <a href="https://github.com/suragaru/shizuka_app/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/suragaru/shizuka_app" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/suragaru/shizuka_app" alt="last update" />
  </a>
  <a href="https://github.com/suragaru/shizuka_app/issues/">
    <img src="https://img.shields.io/github/issues/suragaru/shizuka_app" alt="open issues" />
  </a>  
  <a href="https://github.com/suragaru/shizuka_app/blob/main/LICENSE.md">
    <img src="https://img.shields.io/github/license/suragaru/shizuka_app.svg" alt="open issues" />
  </a>  
</p>

This is a Discord bot built using `discord.py` with various functionalities including astronomy announcements, news updates, Bible verses, anime information, and more.

---

## Buy me a coffee

Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this :)

<!---<a href="https://www.buymeacoffee.com/igorantun" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>--->

<a href="https://ko-fi.com/suragarucoffee"> <img src="https://cdn.ko-fi.com/cdn/kofi3.png?v=3" alt="Buy Me A Coffee" height="40" width="auto"/></a>

---

## :dart: Features

- Astronomy Announcements: Sends daily updates about upcoming astronomy events.
- News Updates: Provides the latest news from specified sources.
- Daily Bible Verse: Shares a daily Bible verse in specified channels.
- Anime Information: Searches and displays details about anime.
- Music Playback: Plays music in voice channels.
- Moderator Tools: Provides tools for server moderation.
  <br><br>


![User Features](http://i.imgur.com/WbF1fi2.png)

## :toolbox: Setup

### Prerequisites

- Python 3.8+
- `pyserial`
- `discord`
- 
### Wiring

### Installation

1. Download the repository

2. Install required packages:
   ```bash
   pip install pyserial, discord.py
   ```
3. Once the dependencies are installed and wiring is done, you can run `bot.py` to start the application.You will then invite the bot to your server and test it.

---

## License
>You can check out the full license [here](https://github.com/suragaru/shizuka_app/blob/main/LICENSE.md)

This project is licensed under the terms of the **MIT** license.







# Arduino Discord Bot
A python bot using the pyserial and discord modules; this is a simple functional bot that allows you to work/control an arduino board through a locally run discord bot on your PC. The arduino board is connected to a lamp or another device, and you can control it using commands through the bot.<br/>

Procedure : <br/>
• Step 1: Firstly, install the necessary python packages by running the following command: <code>pip install discord pyserial</code>.
Next, program your arduino board after wiring your circuit. Use the <code>program.ino</code> file and make script modifications according to your preferences.</p>
Note: the latest python version may not work; am using 3.9.0 version for this project

• Step 2: Test it with the <code>pyserial.py</code> script to diagnose any errors in your program

• Step 3: Create your discord bot on <a href="https://discord.com/developers/applications" target="_blank">https://discord.com/developers/applications</a>. Add your bot token in the <code>app.py</code> script and test it.

• Step 4: After the bot works, modify the script if you want to add more functions to the bot.

