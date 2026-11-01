const http = require('http');
const url = require('url');

const PORT = process.env.PORT || 3000;

// ذاكرة مؤقتة لحفظ الروابط التي يجلبها اسكربت البحث (يمكن ربطها بقاعدة بيانات لاحقاً)
let globalTargetsQueue = [];

const server = http.createServer((req, res) => {
  // إعدادات CORS للسماح بالاتصال من أي مكان
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = url.parse(req.url, true);

  // 1. نقطة فحص الحالة (Health Check)
  if (parsedUrl.pathname === '/' || parsedUrl.pathname === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      status: 'active',
      message: 'Node outreach server is running smoothly',
      queuedTargets: globalTargetsQueue.length
    }));
    return;
  }

  // 2. النقطة اللي هيفتحها اسكربت البحث السريع عشان يرمي الـ 40 ألف موقع دفعة واحدة
  if (parsedUrl.pathname === '/api/upload-targets' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk.toString(); });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body || '{}');
        const incomingTargets = payload.targets || []; // الـ 40 ألف موقع
        
        // إضافة المواقع الجديدة للطابور
        globalTargetsQueue = globalTargetsQueue.concat(incomingTargets);

        console.log(`📥 تم استلام ${incomingTargets.length} موقع جديد! الإجمالي الحالي في الطابور: ${globalTargetsQueue.length}`);

        res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({
          success: true,
          message: `تم استقبال وتخزين الروابط بنجاح`,
          totalQueued: globalTargetsQueue.length
        }));
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ error: 'Invalid JSON payload' }));
      }
    });
    return;
  }

  // 3. النقطة اللي الـ 6 سيرفرات (Workers) هتسحب منها حصتها عشان تبدأ الإرسال
  if (parsedUrl.pathname === '/api/get-targets' && req.method === 'GET') {
    const workerId = parsedUrl.query.workerId || 1;
    
    // سحب دفعة صغيرة (مثلاً أول 100 رابط لكل سيرفر وقت الطلب)
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

  // في حال طلب مسار غير معروف
  res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
