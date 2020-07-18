require("dotenv").config();
const WebSocket = require("ws");
const fs = require("fs");

const writeStream = fs.createWriteStream("./socket_output.txt");

const UDID = process.env.UDID;
const ws = new WebSocket(`wss://realtime.bluecitytechnology.com/ws/realtime/${UDID}/`, {
    "token": process.env.TOKEN,
    "UDID": UDID,
});

const duplex = WebSocket.createWebSocketStream(ws, { encoding: 'utf8' });

duplex.on("data", (chunk) => {
    console.log(chunk);
    writeStream.write(chunk + "\n");
});
// duplex.on("readable", () => console.log(duplex.read())); // This also works

// duplex.pipe(process.stdout);
// process.stdin.pipe(duplex);
