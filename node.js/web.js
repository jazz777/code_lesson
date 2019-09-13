var http = require('http');
var server = http.createServer();
server.on('request',function(req,res) {
    res.writeHead(200,{'Content-Type':'text/plain'});
    res.write('Hello World');
    res.end();
});
// server.listen(1337,'34.84.111.149');
server.listen(1337,'10.146.0.4');
console.log("Server Lisning ");
