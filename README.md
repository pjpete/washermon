# washermon
Washer Monitor

This project involved setting up a Pi Zero W with an SPI A/D to read a photosensor attched in front of the 'Done' LED on our washing machine located in the basement of our home.

Originally this was a single Pi project running the Pushetta API to send a push message to Pushetta iPhone Client to notify 'Washer is Done', because this washing machine is so quiet when it runs/spins and takes FOREVER to spin down after a cycle.

Pushetta went away, and so I was faced with figuring out the next way forward.  There are very few other 'free' iPhone push clients available.  So, why use one Pi when you can use two :)  

I set up a second Pi with a UCTronics tiny touch screen, and using MQTT, push a message from the Pi connected to the washer to the Display Pi.  When the cycle is done, the message is sent, and the touchscreen display shows "DONE!" in full-screen with a green background.

I also added a Sunfounder labs auto-multi-color LED to drive when the cycle is complete, since the viewing angle of the display is pretty narrow.

