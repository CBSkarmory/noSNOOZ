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
  });
}

function writeError(error) {
  if (error) throw error;
}
