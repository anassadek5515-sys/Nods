const http = require('http');
const url = require('url');

const PORT = process.env.PORT || 3000;

// ذاكرة مؤقتة لتخزين الروابط المستهدفة
let globalTargetsQueue = [];

// 1. دالة اسكربت البحث السريع (المدمجة داخلياً)
async function runFastSearchEngine() {
  console.log('🔍 جارِ تشغيل اسكربت البحث السريع لجلب مواقع الشركات...');
  
  const discoveredTargets = [];
  for (let i = 1; i <= 1000; i++) {
    discoveredTargets.push(`https://example-company-${Date.now()}-${i}.com/contact`);
  }

  globalTargetsQueue = globalTargetsQueue.concat(discoveredTargets);
  console.log(`✅ تم جلب وإضافة ${discoveredTargets.length} موقع جديد. الإجمالي في الطابور: ${globalTargetsQueue.length}`);
}

// تشغيل البحث تلقائياً عند بدء التشغيل
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

  // نقطة فحص الحالة
  if (parsedUrl.pathname === '/' || parsedUrl.pathname === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      status: 'active',
      message: 'Unified Multi-Worker Outreach Server is Running',
      queuedTargets: globalTargetsQueue.length
    }));
    return;
  }

  // نقطة سحب الروابط المخصصة للـ 6 سيرفرات
  if (parsedUrl.pathname === '/api/get-targets' && req.method === 'GET') {
    const workerId = parsedUrl.query.workerId || 'unknown';
    
    // سحب دفعة لكل سيرفر (مثلاً 50 رابط في كل طلب)
    const batchSize = 50;
    const workerBatch = globalTargetsQueue.splice(0, batchSize);

    console.log(`📦 السيرفر رقم [${workerId}] طلب روابط، وتم إرسال ${workerBatch.length} رابط له.`);

    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      success: true,
      workerId: workerId,
      targets: workerBatch
    }));
    return;
  }

  res.writeHead404 ? null : (res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' }), res.end(JSON.stringify({ error: 'Endpoint not found' })));
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
