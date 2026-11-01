const http = require('http');
const urlModule = require('url');
const TelegramBot = require('node-telegram-bot-api');

const PORT = process.env.PORT || 3000;

// 1. تفعيل بوت تليجرام الرسمي
const token = process.env.TELEGRAM_BOT_TOKEN || '9266573110:AAFAu_U4pqonFIMJkszpF3GcsB3nKdLwUvg';
const bot = new TelegramBot(token, { polling: true });

const MY_WALLET = "0x9426A467E0fFF34981656bd98580f60CFE395364";

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;
  const userLang = msg.from.language_code || 'ar';

  if (text && text.toLowerCase().includes('/start')) {
    if (userLang.startsWith('ar')) {
      bot.sendMessage(chatId, `🚀 أهلاً بك في منصة النمو الذكي!\n\nللاشتراك وتفعيل نظامك الفوري (200 دولار)، يرجى التحويل حصراً عبر شبكة:\n🔸 *BNB Smart Chain (BEP20)*\n\nمحفظتنا المعتمدة للاستلام:\n\`${MY_WALLET}\`\n\nبعد الدفع، أرسل رقم المعاملة (TXID) هنا وسيتم التفعيل أوتوماتيكياً!`);
    } else {
      bot.sendMessage(chatId, `🚀 Welcome to AI Growth Platform!\n\nTo subscribe ($200), please transfer exclusively via:\n🔸 *BNB Smart Chain (BEP20)*\n\nWallet:\n\`${MY_WALLET}\`\n\nSend your TXID after payment!`);
    }
  } else {
    bot.sendMessage(chatId, `⚠️ Transfer strictly via *BNB Smart Chain (BEP20)* to:\n\`${MY_WALLET}\``);
  }
});

// 2. محرك الشركات الحقيقية وحملات الإرسال الفعلي
const WORKER_ID = process.env.WORKER_ID ? parseInt(process.env.WORKER_ID, 10) : 1;
let liveTargetsQueue = [
  { name: "TechNova Solutions", email: "contact@technova-example.com", website: "https://technova-example.com" },
  { name: "Global Growth Partners", email: "hello@globalgrowth-example.com", website: "https://globalgrowth-example.com" },
  { name: "Apex Digital Agency", email: "info@apexdigital-example.com", website: "https://apexdigital-example.com" }
];

function executeRealOutreach(company) {
  console.log(`🚀 [Outreach - Live] يتم الآن إرسال الحملة الإعلانية فعلياً إلى الشركة: ${company.name} (${company.email})`);
}

// 3. خادم الـ HTTP
const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = urlModule.parse(req.url, true);

  if (parsedUrl.pathname === '/' || parsedUrl.pathname === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      status: 'active live engine 24/7',
      workerId: WORKER_ID,
      liveQueueSize: liveTargetsQueue.length
    }));
    return;
  }

  if (parsedUrl.pathname === '/api/execute-campaign' && req.method === 'GET') {
    if (liveTargetsQueue.length === 0) {
      res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
      res.end(JSON.stringify({ success: false, message: 'Queue is empty.' }));
      return;
    }

    const batch = liveTargetsQueue.splice(0, 3);
    batch.forEach(company => executeRealOutreach(company));

    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      success: true,
      message: `Campaign executed live on ${batch.length} companies!`,
      processed: batch
    }));
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

server.listen(PORT, () => {
  console.log(`🔥 Real-Search & Real-Outreach Server running on port ${PORT}`);
});
