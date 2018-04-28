# voice_recog_control
Using google's Speech API in python3 to control arduino uno board to light up a LED
It uses following modules
  pyserial,
  time,
  speechrecognition,
  gtts,
  urllib3,
  pygame

1. import all the required modules
2. then intialize the mixer from pygame for audio threshold adjustments
3. declare a variable for arduino board and declare its port and baud rate in it.
4. *after 2 seconds delay the arduino board will setup for serial communication with python*
5. declare a list with strings with which your command will match
6.while true intialize the recognizer and choosing the microphone as source fetch your voice command
7.try to check your voice command with the declared list
8. if your command matches with the list declare a function and statements

*before using this command you need to ensure that arduino serial program has to be burned into in arduino board

