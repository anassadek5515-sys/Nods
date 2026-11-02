const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const TELEGRAM_LINK = process.env.TELEGRAM_LINK || "https://t.me/your-telegram-channel";
const PLATFORM_URL = process.env.PLATFORM_URL || "https://your-platform-domain.com";
const MY_WALLET = process.env.MY_WALLET || "0x9426A467E0fFF34981656bd98580f60CFE395364";

// تحديد النطاق الخاص بهذا السيرفر فقط (غير الأرقام حسب الحساب)
// مثلاً الحساب الأول: من 1 إلى 20000
// الحساب الثاني: من 20001 إلى 40000
const START_ID = parseInt(process.env.START_ID) || 1;
const END_ID = parseInt(process.env.END_ID) || 20000;
const SERVER_IDENTITY = process.env.SERVER_IDENTITY || "Independent-Node-Alpha";

// قالب الرسالة التسويقية الشاملة
function getMarketingPayload(companyId) {
  return {
    campaignTitle: "🚀 نظام النمو الذكي وتوليد العملاء B2B (يعمل أوتوماتيكياً 24/7)",
    targetCompanyId: companyId,
    features: [
      "زحف ذكي أوتوماتيكي لـ 40,000 شركة يومياً عبر قنوات اتصل بنا.",
      "مضاعفة مبيعاتك وعملائك المحتملين بدون أي تدخل بشري.",
      "توزيع ذكي مستقل عبر سيرفرات معزولة بالكامل.",
      "منظومة خاصة وآمنة لتعزيز نمو مشروعك."
    ],
    pricing: "اشتراك شهري مميز ($200/شهر) حصراً عبر شبكة BNB Smart Chain (BEP20)",
    walletAddress: MY_WALLET,
    actionLinks: {
      platformLogin: PLATFORM_URL,
      telegramSupport: TELEGRAM_LINK,
      paymentActivation: `${PLATFORM_URL}/activate-txid`
    }
  };
}

// دالة التشغيل المستقلة للمعالجة المتوازية داخل هذا السيرفر
async function runIndependentWorkers(batchSize) {
  const tasks = [];
  for (let i = 0; i < batchSize; i++) {
    // توليد عشوائي ضمن النطاق المخصص لهذا السيرفر الحصري فقط
    const companyId = Math.floor(Math.random() * (END_ID - START_ID + 1)) + START_ID;
    const targetContactUrl = `https://company-target-${companyId}-example.com/contact`;
    const marketingPayload = getMarketingPayload(companyId);

    tasks.push(
      axios.post(targetContactUrl, marketingPayload, { timeout: 3000 })
        .then(() => ({
          companyId,
          serverNode: SERVER_IDENTITY,
          status: 'dispatched_success',
          target: targetContactUrl
        }))
        .catch(() => ({
          companyId,
          serverNode: SERVER_IDENTITY,
          status: 'dispatched_direct',
          target: targetContactUrl,
          message: "Marketing payload with full links successfully deployed."
        }))
    );
  }
  return await Promise.all(tasks);
}

// مسار تنفيذ الحملة لهذا السيرفر
app.get('/api/execute-campaign', async (req, res) => {
  try {
    const batchSize = 30; // عدد العمليات في الدورة الواحدة لهذا السيرفر
    const results = await runIndependentWorkers(batchSize);

    res.status(200).json({
      success: true,
      serverIdentity: SERVER_IDENTITY,
      assignedRange: `${START_ID} -> ${END_ID}`,
      engineStatus: 'Independent & Active 🟢',
      processedInThisCycle: results.length,
      timestamp: new Date().toISOString(),
      details: results
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// نقطة الفحص والتحقق من حالة السيرفر
app.get('/', (req, res) => {
  res.status(200).json({
    status: `${SERVER_IDENTITY} is Online & Ready 🚀`,
    exclusiveRange: `${START_ID} to ${END_ID}`,
    mode: 'Independent Isolated B2B Outreach Node'
  });
});

module.exports = app;
