const http = require('http');
const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
        status: 'online',
        message: 'Node is active and running successfully on Vercel!',
        timestamp: new Date()
    }));
});

server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
