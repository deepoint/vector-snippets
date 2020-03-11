#!/usr/bin/python3

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

# Import requests library used for making HTTP calls to the dashboard server.
import requests

# Import subprocess
import subprocess

# Import Anki Vector SDK
import anki_vector

# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = 'your-adafruit-io-key'       # Set to your Adafruit IO key.
ADAFRUIT_IO_USERNAME = 'your-adafruit-username'  # See https://accounts.adafruit.com
                                                    # to find your username.
# Set the URL of the physical dashboard to use.  If running on the same Pi as
# the dashboard server then keep this the default localhost:5000 value.  If
# modified make sure not to end in a slash!
DASHBOARD_URL = 'http://localhost:5000'  # URL of the physical dashboard.
                                         # Don't end with a slash!


# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print ('Connected to Adafruit IO!  Listening for feed changes...')
    # Subscribe to the three pi-dashboard feeds that will be displayed on the
    # dashboard.  Modify this to subscribe to all the feeds you want to display.
    client.subscribe('vector')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print ('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):

    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    text ="{1}".format(feed_id, payload)
    print (text)
    #If you have more than one feed...
    if feed_id == 'vector':

        if text == "esci di casa":
            with anki_vector.Robot() as robot:
                robot.behavior.drive_off_charger()
        elif text == "vai a casa":
            with anki_vector.Robot() as robot:
                robot.behavior.drive_on_charger()
        elif text == "livello batteria":
            #Let's call a snippet. Check the path of the file.
            subprocess.call(['/home/pi/battery_level.py'])
        else :
            args = anki_vector.util.parse_command_args()
            with anki_vector.Robot(args.serial) as robot:
                robot.behavior.say_text(text)

# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Use the loop_blocking function to run the message loop for processing Adafruit
# IO events.  Since this script doesn't do any other processing this blocking
# version of the message loop is fine.  All the program logic will occur in the
# callback functions above when Adafruit IO feeds are changed.
client.loop_blocking()
