# washermon
Washer Monitor

This project involved setting up a Pi Zero W with an SPI A/D to read a photosensor attched in front of the 'Done' LED on our washing machine located in the basement of our home.

Originally this was a single Pi project running the Pushetta API to send a push message to Pushetta iPhone Client to notify 'Washer is Done', because this washing machine is so quiet when it runs/spins and takes FOREVER to spin down after a cycle.

Pushetta went away, and so I was faced with figuring out the next way forward.  There are very few other 'free' iPhone push clients available.  So, why use one Pi when you can use two :)  

I set up a second Pi with a UCTronics tiny touch screen, and using MQTT, push a message from the Pi connected to the washer to the Display Pi.  When the cycle is done, the message is sent, and the touchscreen display shows "DONE!" in full-screen with a green background.

I also added a Sunfounder labs auto-multi-color LED to drive when the cycle is complete, since the viewing angle of the display is pretty narrow.

The subfolders contain the details (as much as I can remember) of the setup for each of the two Pis.  
washer-pi is the Pi with the A/D at the washer.  
washer-dash is the Pi with the display somewhere else hopefully somewhere else in the house or what's the point? :)

The scripts are Python, and rely on a lot of existing libraries that are out there for makers to use.  

Probably the easiest part of the whole project was the actual scripting, relatively speaking.  There were some challenges with the MQTT callbacks and getting those to work right.  There were also a few head-banging moments trying to figure out Qt5 and driving a full screen GUI.  But what will be really tough for me to capture here are the 'admin' type activities on each Pi to get it configured for headless operation with remote access (VNC & SSH), getting the devices to start up and run the scripts automatically. All the little steps you take quickly as you run across an error, Google for a result, mash the keys on the command line and repeat until it's satisfactory.  It's that cliche: Move fast and break things.

bash 'history' command is your friend.  Give it a hug, and occasionally do a history > history.txt (followed by history1.txt, history2.txt, history_020121.txt)

Happy making!

