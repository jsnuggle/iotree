# IOTree
A simple way to control your christmas tree lights remotely.

## Why?
Last Christmas we got a new set of LED christmas lights with a 3-way switch
to control the color mode. The kids love color. My wife likes white. I'm
lazy, and our tree is right next to our Google Home so I wanted to see if
I could wire them together.

## Parts Needed
- Google Home (or Alexa)
- Lights (I used [Sylvania 3-Function Color Change - SNKS-1-2](https://www.amazon.com/Sylvania-3-Function-Color-Changing-Lights/dp/B01LZE6N23))
- Raspberry Pi with power supply + network connection
- GPIO Breakout
- 3 x Optocoupler (I used [6N138](https://www.amazon.com/Optocoupler-Single-Channel-Darlington-Output/dp/B07DLTSXC1))
- Breadboard
- Jumper wires 

## Hardware Prep
The first thing you'll need to do is break connections from the three color 
channels in the switch box. Honestly the most difficulat part of the project
was figuring out how to get into the box. I had to use a saw. Once I was in,
was very clear there were three posts (one for each color mode) and a negative
post. I soldered long wires to all of these and taped the box back together.

On the circuit board, the basic setup is to use the three optocouplers to 
control the three light channels -- and to heave each optocoupler controlled
by an independent GPIO pin. I'll attach a photo and wiring schematic when I can.

## IOT Connectins Setup
There are a numbrer of components you need to wire together to get your Google
Home talking to your Christmas tree. Luckily all of them are very simple to work
with. End to end the system looks like this:

Google Assistant -> IFTTT -> Adafruit IO -> Raspberry Pi

I'll show you how to set up each of these components separtely.

### Adafruit IO
Visit [adafruit.io](http://adafruit.io). If you don't already have an account, 
set one up. This system doesn't send a ton of data, so a free account is totally
fine. After you've logged in, set up a new feed. The feed I set up for this
project is called IOTree Commands (iotree-commands), but you can name it
what you like and update the value in config.py.

Be sure to copy your Adafruit IO **username** and **API key** - youll need 
those in a minute.

### IFTTT
Visit If This Then That ([ifttt.com](http://ifttt.com)) and set up an account if
you haven't aready. Navitate to make your own applet from scratch. I set up two, 
but they both follow the same formula. 

Start with the **Google Assistant** service. If you haven't used IFTTT with Google
before you'll need to connect your account. Once you have, select the trigger **'Say a 
phrase with a text ingredient'**. I entered the phrase 'Set Christmas lights
to $' where $ is a text ingredient.

Next, add **Adafruit** as an action service. Again you'll need to connect IFTTT
to Adafruit if you haven't already. Once you have, you'll select the action 
**'Send data to Adafruit IO'**. You should see the feed you created in the dropdown
(for me 'IOTree Commands') -- select that feed and add the following to the 
Data to save field: 
```
{"execute":"color_change", "arg":"{{TextField}}"}
```
where 'TextField' is an ingredient macro (reachable via 'add ingredient').

Once you've saved that, add one more applet to turn on and off the lights. Use 
the same base components as above (Google Assistant + Adafruit) using this text:
```
Turn $ the Christmas tree
```
and this json payload in the Adafruit 'Data to save' field:
```
{"execute":"power", "arg":" {{TextField}}"}
```

and that's it for connections.

## System Setup
Clone this project to the directory of your choice on your raspberry pi:
```
git clone git@github.com:jsnuggle/iotree.git 
```

Make sure your system has an up to date copy of python3 and pip3. Run the
following command to download the required packages
```
pip3 -r requirements.txt
```

Open the file secrets_MODIFY_ME.py and add your Adafruit IO username and API
key. Once you're set, rename the file to secrets.py.

If you've used a different name for the Adafruit IO feed, change the value in
config.py.

### Starting the system
To start the application, run the following command from the project directory:
```
./bin/run.sh
```

This will give you an idea if everything is working correctly, but since this
will start a system-blocking process, it's not the most convenient thing in 
the world. What I've taken to doing is running the process inside tmux. The
added value here is it's easy to reattach to the running process if you 
log out and back in to your Raspberry Pi (I connect to mine exclusively over
Mosh). To start the app inside tmux, run this command:
```
./bin/runTmux.sh
```

This will start a tmux session in the background called 'iotree' with the 
application running inside. To attach to that session, run:
```
tmux attach -tiotree
```

### Auto-Start
To go a step further, you can setup the application as an init.d process 
that will run on system start. This is helpful in the case of power outages
or if you accidentally unplug your Pi -- you won't have to log in and restart
the app. To set that up, run the command:
```
./bin/initd_install.sh
```

## Extra Credit
For fun, I also set up a few more commands inside of IFTTT. I connected the
timer trigger to Adafruit IO to allow me to turn the tree on and off on a
fixed schedule. But you can also get more exotic and connect to other triggers (
like location services). It's also easy enough to connect to Alexa following the 
same patterns -- but at the time I wrote this I didn't see a way to allow
for text ingredient parsing. That just means you'll need to set up seprate applets
for any workflow you want to suppport (e.g. each color mode the lights support). 

Special thanks to imightbeamy - I still find myself stealing liberally from 
ideas in her [Buzzerbot9000](https://github.com/imightbeamy/buzzerbot9000). 
