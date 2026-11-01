const http = require('http');
const urlModule = require('url');
const TelegramBot = require('node-telegram-bot-api');
const https = require('https');
const nodemailer = require('nodemailer');

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

// 2. إعدادات الإرسال الفعلي للإيميلات (SMTP)
const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST || 'smtp.gmail.com',
  port: process.env.SMTP_PORT ? parseInt(process.env.SMTP_PORT, 10) : 587,
  secure: false,
  auth: {
    user: process.env.SMTP_USER || 'your-email@gmail.com',
    pass: process.env.SMTP_PASS || 'your-email-password'
  }
});

// 3. طابور الشركات (مُجهز بملء البيانات أوتوماتيكياً حسب اسم الشركة وموقعها)
const WORKER_ID = process.env.WORKER_ID ? parseInt(process.env.WORKER_ID, 10) : 1;
let liveTargetsQueue = [
  { name: "TechNova Solutions", email: process.env.TEST_TARGET_EMAIL || "test-target@example.com", website: "https://technova-example.com" },
  { name: "Global Growth Partners", email: process.env.TEST_TARGET_EMAIL || "test-target@example.com", website: "https://globalgrowth-example.com" }
];

// 4. محرك الحملات والنموذج التسويقي المعبأ تلقائياً (High-Converting Template)
async function executeRealOutreach(company) {
  console.log(`🚀 [Outreach - Live] يتم الآن إرسال الإيميل المخصص إلى الشركة: ${company.name}`);

  // نموذج الإيميل التسويقي الفتاك (بيملأ اسم الشركة والموقع أوتوماتيك في كل رسالة)
  const emailSubject = `Quick question about ${company.name}'s customer acquisition`;
  
  const emailHtml = `
    <div style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
      <p>Hi Team at <strong>${company.name}</strong>,</p>
      
      <p>I was browsing through <strong>${company.website}</strong> and noticed your strong positioning, but I saw an opportunity to scale your inbound B2B lead generation on complete autopilot.</p>
      
      <p>We built an <strong>Autonomous 24/7 Growth-Hacking Engine</strong> that runs live web prospecting, extracts verified leads, and dispatches hyper-personalized outreach without human intervention.</p>
      
      <p>Would you be open to seeing a quick 2-minute demo of how this can inject a steady stream of clients into ${company.name}?</p>
      
      <p>Best regards,<br>
      <strong>AI Growth Automation Team</strong><br>
      <a href="https://t.me/storyanalyzer2026_bot" target="_blank">Activate Your Engine on Telegram</a></p>
    </div>
  `;

  try {
    const info = await transporter.sendMail({
      from: '"AI Growth Platform" <' + (process.env.SMTP_USER || 'no-reply@saas.com') + '>',
      to: company.email,
      subject: emailSubject,
      html: emailHtml
    });
    console.log(`✅ تم إرسال الرسالة المخصصة بنجاح للشركة ${company.name}! Message ID: ${info.messageId}`);
  } catch (error) {
    console.error(`❌ فشل إرسال الرسالة للشركة ${company.name}:`, error.message);
  }
}

// 5. خادم الـ HTTP
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
      liveQueueSize: liveTargetsQueue.length,
      message: 'High-Converting Dynamic Outreach Engine is Active'
    }));
    return;
  }

  if (parsedUrl.pathname === '/api/execute-campaign' && req.method === 'GET') {
    if (liveTargetsQueue.length === 0) {
      res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
      res.end(JSON.stringify({ success: false, message: 'Queue is empty.' }));
      return;
    }

    const batch = liveTargetsQueue.splice(0, 2);
    batch.forEach(company => executeRealOutreach(company));

    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify({
      success: true,
      message: `Dynamic personalized campaign executed on ${batch.length} companies!`,
      processed: batch
    }));
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

server.listen(PORT, () => {
  console.log(`🔥 Dynamic Outreach Server running on port ${PORT}`);
});
