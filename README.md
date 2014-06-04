MCtoPi
======
This is an API for interfacing between Minecraft running on a computer and a Raspberry Pi. You must first download and install the [ComputerCraft](http://www.computercraft.info/) mod for Minecraft. Once it is installed, you need to move the CC API onto the computer in MC. It is just called `MCtoPI` with no extention. There are multiple ways to do this, and it is left as an exersise to the reader to find out how. Once the API is on the computer, it can be loaded with `os.loadAPI("MCtoPi")`. The commands are as follows:

| Function     | Arguments    | Returns                | Action                |
| -------------|--------------|------------------------|---------------------- |
| MCtoPi.setup | _host, _port | Nothing                | Setup the API         |
| MCtoPi.send  | data         | Data sent back from Pi | Send and recieve data |

The MCtoPI.py file is the API for the Raspberry Pi. It can go wherever you want on the Pi. In order to use this, you must import it using the python `import` command. Then you must make a class that inherits from `MCtoPi.MCtoPi`. This class must have one function called `get` that takes three arguments: `self, output, input`. The output arg is a file-like object. Any data written to this will be returned to Minecraft. The input arg is whatever data was passed to the `send` function in Minecraft. To start the server, call `MCtoPi.start()`. the start function takes two arguments: the first is the class that inherits from `MCtoPi.MCtoPi`, and the second is the optional port number, which defaults to `3141`.
