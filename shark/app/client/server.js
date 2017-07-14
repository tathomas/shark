var express = require('express');
var server = express();
server.use(express.static(__dirname));

server.get('/hello', (req, res) => {
  res.status(200).send('Hello, world!').end();
});

var port = process.env.PORT || 8081;
server.listen(port);
console.log('Use port ' + port + ' to connect to this server');

exports = module.exports = server;
