const http = require('http');
const url = require('url');

const PORT = process.env.PORT || 3000;

// ذاكرة مؤقتة لتخزين الروابط المستهدفة
let globalTargetsQueue = [];

// 1. دالة اسكربت البحث السريع (المدمجة داخلياً)
async function runFastSearchEngine() {
  console.log('🔍 جارِ تشغيل اسكربت البحث السريع لجلب مواقع الشركات...');
  
  // هنا محاكاة لاسكربت البحث اللي بيجيب الـ 40 ألف موقع في ثواني
  // (تقدر تحط هنا منطق البحث الفعلي أو الـ Scraper الخاص بك)
  const discoveredTargets = [];
  for (let i = 1; i <= 100; i++) {
    discoveredTargets.(`https://example-company-${Date.now()}-${i}.com/contact`);
  }

  // إضافة الروابط الجديدة للطابور العام
  globalTargetsQueue = globalTargetsQueue.concat(discoveredTargets);
  console.log(`✅ تم جلب وإضافة ${discoveredTargets.length} موقع جديد. الإجمالي في الطابور: ${globalTargetsQueue.length}`);
}

// تشغيل البحث تلقائياً عند بدء تشغيل السيرفر (أو يمكن جدولته)
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

  // نقطة فحص الحالة والاطمئنان على الطابور
  if (parsedUrl.pathname === '/' || parsedUrl.pathname === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      status: 'active',
      message: 'Outreach Core Server with Integrated Scraper is Running',
      queuedTargets: globalTargetsQueue.length
    }));
    return;
  }

  // زر تشغيل البحث يدوياً لو احتجت تجدد الداتا في أي وقت
  if (parsedUrl.pathname === '/api/run-search' && req.method === 'POST') {
    runFastSearchEngine();
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({ success: true, message: 'تم تشغيل اسكربت البحث وجلب الروابط بنجاح', total: globalTargetsQueue.length }));
    return;
  }

  // نقطة سحب الروابط للـ 6 سيرفرات (Workers)
  if (parsedUrl.pathname === '/api/get-targets' && req.method === 'GET') {
    const workerId = parsedUrl.query.workerId || 1;
    
    // سحب دفعة لكل سيرفر (مثلاً 100 رابط في كل طلب)
    const batchSize = 100;
    const workerBatch = globalTargetsQueue.splice(0, batchSize);

    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      success: true,
      workerId: workerId,
      targets: workerBatch
    }));
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
