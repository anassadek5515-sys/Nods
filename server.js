const http = require('http');
const url = require('url');

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  // إعدادات CORS للسماح بالاتصال من أي واجهة
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = url.parse(req.url, true);

  // نقطة فحص الحالة (Health Check)
  if (parsedUrl.pathname === '/' || parsedUrl.pathname === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      status: 'active',
      message: 'Node outreach server is running smoothly',
      node: process.env.VERCEL_URL || 'distributed-node'
    }));
    return;
  }

  // نقطة تزويد الـ 6 سيرفرات بروابط الشركات المستهدفة للإرسال
  if (parsedUrl.pathname === '/api/get-targets' && req.method === 'GET') {
    const workerId = parsedUrl.query.workerId || 1;
    
    // هنا قاعدة بيانات الروابط اللي السيرفرات الـ 6 بتسحب منها حصتها (اليومية)
    const mockTargets = [
      "https://example-company1.com/contact",
      "https://example-company2.com/contact-us"
    ];

    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      success: true,
      workerId: workerId,
      targets: mockTargets
    }));
    return;
  }

  // نقطة استلام وتوزيع طلبات البحث والاتصال
  if (parsedUrl.pathname === '/api/search' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk.toString(); });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body || '{}');
        
        const result = {
          success: true,
          companyQuery: payload.query || null,
          message: 'تم استقبال طلب البحث وتوجيهه بنجاح لشبكة السيرفرات',
          processedAt: new Date().toISOString(),
          executedByNode: process.env.VERCEL_URL || 'node-instance'
        };

        res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify(result));
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ error: 'Invalid JSON payload' }));
      }
    });
    return;
  }

  // في حال طلب مسار غير معروف
  res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
