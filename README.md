# vector-snippets
Little snippets in python to be used with Anki Vector SDK

The idea is to create a bunch of little python script that should accomplish only one specific action. This would allow anyone to decide how to call each one.

Just as an example I will share a simple vector-service.py file that will listen to an Adafruit IO feed for certain "keyword" and then give commands to Vector. Just for fun, these keywords are in Italian, I'am actually try to make it easier to use Vector for non-english owner (more on this later...)

You should already have installed the Anki Vector SDK (read here for info: https://developer.anki.com/vector/docs/initial.html) and the Adafruit IO (create an account here:https://io.adafruit.com and then install the Adafruit Client, for instance on a Raspberry PI give the command: sudo pip3 install adafruit-io )

Remember to set your Adafruit IO username and api key.
