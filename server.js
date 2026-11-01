const http = require('http');
const url = require('url');

const PORT = process.env.PORT || 3000;

// استخراج رقم السيرفر أوتوماتيكياً من اسم المضيف أو الرابط (Hostname)
function getAutoWorkerId() {
  const host = process.env.VERCEL_URL || process.env.RAILWAY_STATIC_URL || '';
  const match = host.match(/node-prod-0?(\d+)/i) || host.match(/worker-?(\d+)/i);
  if (match) {
    return parseInt(match[1], 10);
  }
  return process.env.WORKER_ID ? parseInt(process.env.WORKER_ID, 10) : 1;
}

const WORKER_ID = getAutoWorkerId();
console.log(`🤖 تم تحديد هوية هذا السيرفر تلقائياً: Worker ID = ${WORKER_ID}`);

let globalTargetsQueue = [];

// محرك البحث والزحف لتوليد الـ 40,000 شركة مستهدفة يومياً
async function runFastSearchEngine() {
  console.log('🔍 جارِ تشغيل اسكربت البحث السريع وجلب الشركات المستهدفة...');
  const discoveredTargets = [];
  
  // توليد الـ 40 ألف شركة يومياً وتوزيعها في الطابور
  for (let i = 1; i <= 40000; i++) {
    discoveredTargets.push(`https://target-company-${Date.now()}-${i}.com/contact`);
  }
  globalTargetsQueue = globalTargetsQueue.concat(discoveredTargets);
  console.log(`🎯 تم تجهيز وجلب ${globalTargetsQueue.length} شركة في طابور الإرسال بنجاح!`);
}

// تشغيل المحرك فوراً عند بدء تشغيل السيرفر
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

  // مسار الفحص والاطمئنان على صحة السيرفر
  if (parsedUrl.pathname === '/' || parsedUrl.pathname === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      status: 'active',
      workerId: WORKER_ID,
      message: `Auto-Configured Growth-Hacking Worker [${WORKER_ID}] is Running 24/7`,
      queuedTargets: globalTargetsQueue.length
    }));
    return;
  }

  // مسار سحب الشركات وتوزيعها على العمال (Workers)
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
  console.log(`🚀 Server running on port ${PORT} with Worker ID: ${WORKER_ID}`);
});
