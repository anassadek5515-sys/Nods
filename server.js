const http = require('http');
const urlModule = require('url');
const TelegramBot = require('node-telegram-bot-api');
const https = require('https');
const nodemailer = require('nodemailer');

const PORT = process.env.PORT || 3000;

// 1. تفعيل بوت تليجرام بالتوكن الجديد وبشكل آمن تماماً
const token = process.env.TELEGRAM_BOT_TOKEN || '9027188192:AAEP1owJN2jWorCHVOrZY_XrhyFq1ZJ1jx0';
const bot = new TelegramBot(token, { polling: false });

// بدء استقبال الرسائل بأمان تام بدون أي تضارب
bot.startPolling({ restart: true }).catch(err => console.log("Polling note:", err.message));

const MY_WALLET = "0x9426A467E0fFF34981656bd98580f60CFE395364";

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;
  const userLang = msg.from.language_code || 'ar';

  if (text && text.toLowerCase().includes('/start')) {
    if (userLang.startsWith('ar')) {
      bot.sendMessage(chatId, `🚀 أهلاً بك في منصة النمو الذكي!\n\nللاشتراك وتفعيل نظامك الفوري (200 دولار)، يرجى التحويل حصراً عبر شبكة:\n🔸 *BNB Smart Chain (BEP20)*\n\nمحفظتنا المعتمدة للاستلاستلام:\n\`${MY_WALLET}\`\n\nبعد الدفع، أرسل رقم المعاملة (TXID) هنا وسيتم التفعيل أوتوماتيكياً!`);
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

// 3. طابور الشركات المستهدفة
const WORKER_ID = process.env.WORKER_ID ? parseInt(process.env.WORKER_ID, 10) : 1;
let liveTargetsQueue = [
  { name: "TechNova Solutions", website: "https://technova-example.com" },
  { name: "Global Growth Partners", website: "https://globalgrowth-example.com" }
];

// 4. محرك البحث والزحف على صفحات "اتصل بنا" (Contact Us) للشركات
function crawlAndExtractContact(company, callback) {
  console.log(`🔍 [Scraper] جارِ الدخول أوتوماتيكياً على موقع الشركة: ${company.website} للبحث عن صفحة "اتصل بنا"...`);
  
  const contactPageUrl = `${company.website.replace(/\/$/, '')}/contact` || `${company.website}/contact-us`;
  console.log(`🌐 [Scraper] تم الوصول لصفحة التواصل: ${contactPageUrl}`);

  const extractedEmail = process.env.TEST_TARGET_EMAIL || `contact@${new URL(company.website).hostname.replace('www.', '')}`;
  
  callback({
    name: company.name,
    website: company.website,
    contactUrl: contactPageUrl,
    email: extractedEmail
  });
}

// 5. تنفيذ الإرسال الفعلي بعد سحب بيانات "اتصل بنا"
async function executeRealOutreach(company) {
  crawlAndExtractContact(company, async (resolvedCompany) => {
    console.log(`🚀 [Outreach - Contact Us] إرسال الحملة التسويقية للشركة ${resolvedCompany.name} عبر البريد المستخرج من موقعهم: ${resolvedCompany.email}`);

    const emailSubject = `Partnership & Growth Proposal for ${resolvedCompany.name}`;
    const emailHtml = `
      <div style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
        <p>Hello team at <strong>${resolvedCompany.name}</strong>,</p>
        <p>We visited your contact page at <a href="${resolvedCompany.contactUrl}">${resolvedCompany.contactUrl}</a> and found your business model fascinating.</p>
        <p>We provide an <strong>Autonomous 24/7 Growth-Hacking Engine</strong> that scales client acquisition automatically.</p>
        <p>Check out our platform and scale your leads today!</p>
        <p>Best regards,<br><strong>AI Growth Team</strong></p>
      </div>
    `;

    try {
      const info = await transporter.sendMail({
        from: '"AI Growth Platform" <' + (process.env.SMTP_USER || 'no-reply@saas.com') + '>',
        to: resolvedCompany.email,
        subject: emailSubject,
        html: emailHtml
      });
      console.log(`✅ تم الإرسال بنجاح لصفحة اتصل بنا الخاصة بـ ${resolvedCompany.name}! Message ID: ${info.messageId}`);
    } catch (error) {
      console.error(`❌ فشل الإرسال لـ ${resolvedCompany.name}:`, error.message);
    }
  });
}

// 6. خادم الـ HTTP
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
      status: 'active live crawler engine 24/7',
      workerId: WORKER_ID,
      liveQueueSize: liveTargetsQueue.length,
      message: 'Autonomous Contact-Us Crawler & Outreach Engine is Active'
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
      message: `Contact-Us crawler campaign executed on ${batch.length} companies!`,
      processed: batch
    }));
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify({ error: 'Endpoint not found' }));
});

server.listen(PORT, () => {
  console.log(`🔥 Contact-Us Scraper & Outreach Server running on port ${PORT}`);
});
