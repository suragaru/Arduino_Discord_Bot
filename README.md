# ARDUINO DISCORD BOT
A python bot using the pyserial and discord modules; this is a simple functional bot that allows you to work/control an arduino board through a locally run discord bot on your PC. The arduino board is connected to a lamp or another device, and you can control it using commands through the bot.<br/>

Procedure : <br/>
• Step 1: Firstly, install the necessary python packages by running the following command: <code>pip install discord pyserial</code>.
Next, program your arduino board after wiring your circuit. Use the <code>program.ino</code> file and make script modifications according to your preferences.</p>
Note: the latest python version may not work; am using 3.9.0 version for this project

• Step 2: Test it with the <code>pyserial.py</code> script to diagnose any errors in your program

• Step 3: Create your discord bot on <a href="https://discord.com/developers/applications" target="_blank">https://discord.com/developers/applications</a>. Add your bot token in the <code>app.py</code> script and test it.

• Step 4: After the bot works, modify the script if you want to add more functions to the bot.

