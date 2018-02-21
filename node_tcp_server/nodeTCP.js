var net = require('net');
var server = net.createServer(function(socket) {
	socket.write('Echo server\r\n');
	socket.pipe(socket);
});
server.listen(1337, '127.0.0.1');
/*
connect with a tcp client from the command line using netcat, the *nix 
utility for reading and writing across tcp/udp network connections.
$ netcat 127.0.0.1 1337
should see:
> Echo server
*/
var net = require('net');
var client = new net.Socket();
client.connect(1337, '127.0.0.1', function() {
	console.log('Connected');
	client.write('Hello, server! From Client.');
});
client.on('data', function(data) {
	console.log('Received: ' + data);
	client.destroy(); // kill client after server's response
});
client.on('close', function() {
	console.log('Connection closed');
});