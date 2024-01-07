<b>Moderator (Discord Bot):</b>
<p>Made in Python using the pyserial and discord modules, this is a simple functional bot that allows you to work/control an Arduino board through a locally run Discord bot on your PC. The Arduino board is connected to a lamp or another device, and you can control it using commands through the bot. It's a smart project that can be crafted simply.</p><br/>


<p><b>Procedure </b><strong>Step 1:</strong></p>
<p>Firstly, install the necessary Python packages by running the following command:</p>
<pre><code>pip install discord pyserial</code></pre>
<p>Note: The latest Python version may not work; I recommend using version 3.9.0+ for this project.</p>
<p>Next, program your Arduino board after wiring your circuit. Utilize the <code>program.ino</code> file and make script modifications according to your preferences.</p>

<p><strong>Step 2:</strong></p>
<p>Test it with the <code>pyserial.py</code> script to diagnose any errors in your program.</p>

<p><strong>Step 3:</strong></p>
<p>Create your Discord bot on <a href="https://discord.com/developers/applications" target="_blank">https://discord.com/developers/applications</a>. Add your bot token in the <code>app.py</code> script and test it.</p>

<p><strong>Step 4:</strong></p>
<p>After the bot works, modify the script. You can also upgrade the bot if you want to go crazy with it.</p>


