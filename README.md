MCtoPi
======
This is an API for interfacing between Minecraft running on a computer and a Raspberry Pi. You must first download and install the [ComputerCraft](http://www.computercraft.info/) mod for Minecraft. Once it is installed, you need to move the CC API onto the computer in MC. There are multiple ways to do this, and it is left as an exersise to the reader to find out how. Once the API is on the computer, it can be loaded with `os.loadAPI("MCtoPi")`. The commands are as follows:

| Function     | Arguments    | Returns                | Action                |
| -------------|--------------|------------------------|---------------------- |
| MCtoPi.setup | _host, _port | Nothing                | Setup the API         |
| MCtoPi.send  | data         | Data sent back from Pi | Send and recieve data |