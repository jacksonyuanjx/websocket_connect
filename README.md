# websocket_connect_python

## How to Run
* Navigate to the `/python` directory in your terminal
* Make sure Python 3 is installed on your machine
* Create a `.env` file in the root of the `/python` directory and include the `UDID` and `TOKEN` values (WARNING: this has not been tested but if it doesn't work, you can just hardcode the values into `connect.py`)
* Run `python3 connect.py` in your terminal

# websocket_connect_node

## How to Run
* Navigate to the `/node_js` directory in your terminal
* Make sure you have Node.js installed on your machine
* Type `yarn` or `npm i` in your terminal
* Create a `.env` file in the root of the `/node_js` directory and include the `UDID` and `TOKEN` values
* Run `node index.js` in the terminal. This will output the realtime socket data in the terminal and also store all the data in a file called `socket_output.txt`
* Press Ctrl + C (on Windows) or Cmd + C (on Mac) in order to stop the process
