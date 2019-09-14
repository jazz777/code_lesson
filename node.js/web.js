var http = require('http');
var server = http.createServer();
server.on('request',function(req,res) {
    res.writeHead(200,{'Content-Type':'text/plain'});
    res.write('Soracom Happy Max');
    res.end();
});
// server.listen(1337,'34.84.111.149');
//  not working ,global IP


//server.listen(1337,'10.146.0.4');
server.listen(1348,'10.146.0.4');



//server.listen(81,'10.146.0.4');
// not working ,why?


console.log("Server Lisning ");
