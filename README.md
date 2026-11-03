# artemis_http_repl
A basic Python REPL for executing arbitrary Lua code using https://github.com/alula/switch-artemis-launcher.

## Requirements
- A device running the Artemis launcher listening on an HTTP server
- requests
- Python that supports f-strings

## How to use
Install Python and requests then run. Enter in your devices IP address and it will probe it for some useful data before dropping to the REPL loop.

Be warned, while you can peek and poke, I have found that they will cause the game to segfault most of the time. Most likely due to increased security on the platforms that this is running on.

Enter in code then hit EOF to execute (Ctrl+D typically). The REPL will give you the result or a NetworkError if the game crashes.

Instructions on how to install the Artemis launcher or anything relating to the end device is strictly out of scope of this repository.