const http = require('http');
const url = require('url');

const PORT = process.env.PORT || 3000;

// استخراج رقم السيرفر أوتوماتيكياً من اسم المضيف أو الرابط (Hostname)
function getAutoWorkerId() {
  const host = process.env.VERCEL_URL || '';
  const match = host.match(/node-prod-0?(\d+)/i) || host.match(/worker-?(\d+)/i);
  if (match) {
    return parseInt(match[1], 10);
  }
  // لو مش ظاهر في الرابط، بياخد الرقم من البيئة أو الافتراضي 1
  return process.env.WORKER_ID ? parseInt(process.env.WORKER_ID, 10) : 1;
}

const WORKER_ID = getAutoWorkerId();
console.log(`🤖 تم تحديد هوية هذا السيرفر تلقائياً: Worker ID = ${WORKER_ID}`);

let globalTargetsQueue = [];

async function runFastSearchEngine() {
  console.log('🔍 جارِ تشغيل اسكربت البحث السريع...');
  const discoveredTargets = [];
  for (let i = 1; i <= 1000; i++) {
    discoveredTargets.push(`https://example-company-${Date.now()}-${i}.com/contact`);
  }
  globalTargetsQueue = globalTargetsQueue.concat(discoveredTargets);
}

runFastSearchEngine();

const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = url.parse(req.url, true);

  if (parsedUrl.pathname === '/' || parsedUrl.pathname === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      status: 'active',
      workerId: WORKER_ID,
      message: `Auto-Configured Worker [${WORKER_ID}] is Running`,
      queuedTargets: globalTargetsQueue.length
    }));
    return;
  }

  if (parsedUrl.pathname === '/api/get-targets' && req.method === 'GET') {
    const batchSize = 50;
    const workerBatch = globalTargetsQueue.splice(0, batchSize);

    console.log(`📦 السيرفر رقم [${WORKER_ID}] سحب دفعة بنجاح (${workerBatch.length} رابط).`);

    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      success: true,
      workerId: WORKER_ID,
      targets: workerBatch
    }));
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT} with Worker ID: ${WORKER_ID}`);
});
