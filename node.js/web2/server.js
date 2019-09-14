var http = require('http');
var settings = require('./settings');
var server = http.createServer();
server.on('request',function(req,res) {
 res.writeHead(200,{'Content-Type':'text/plain'});
// res.write('Hello Nozomikawaii');
 res.write(settings.message);
 res.end();
});
server.listen(settings.port,settings.host);
console.log("server Listening...");
