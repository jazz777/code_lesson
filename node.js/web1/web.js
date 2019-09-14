// My First Program Node.js

// import http module
var http = require('http');


// run createServer Method
var server = http.createServer();

// definition on Request
server.on('request',function(req,res) {
    res.writeHead(200,{'Content-Type':'text/plain'});
    res.write(' Easy web server Node js http  module !! \n ');
/*
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
    res.write('Soracom Happy Max,It is running node.js http module !! \n ');
*/

    res.end();
});

// Assign IP Address ,and Port

server.listen(80,'10.146.0.4');
/*
you need "sudo  node web.js"
Because 80 is well known port.
*/

console.log("Server Lisning ");

/*

server.listen(1337,'34.84.111.149');

/* global IP
Listening NG ,GCP VM os do not have Global IP,
confirm ifconfig
*/


//server.listen(1337,'10.146.0.4');

/*
Listening OK ,You needs to permit firewall setting
*/


