// needed for exec
const { exec } = require('child_process');

// Setup basic express server
var express = require("express");
var socket = require("socket.io");
var socketClient = require("socket.io-client");
var fs = require("fs");

FILE_NAME = "js_to_py.txt";
SUBREDDITS = "news,worldnews,politics";

var app = express();
app.use(express.static("."));
var server = app.listen(8080, onServerStart);
var connection; //connection with load balancer server

function onServerStart () {
    console.log("Started server");
}

var io = socket(server);
io.on("connection", onSocketConnection); //when connected

function onSocketConnection(connection) {
    console.log("Connected");
    connection.on("data", function(data){
	var message = data.phone_number + ":" + data.carrier + ":" + SUBREDDITS + "\n";
	fs.appendFile(FILE_NAME, message, writeError);

	// notification on stdout
	console.log("[DEBUG] got data, execing handle_subs")
	// invoke handle_subscribers.py
	exec('./handle_subscribers.py', (err, stdout, stderr) => {
	    if (err) {
		// node couldn't execute the command
		return;
	    }
	    
	    // the *entire* stdout and stderr (buffered)
	    console.log(`${stdout}`);
	    console.log(`${stderr}`);
	});
	
    });
}

function writeError(error) {
  if (error) throw error;
}
