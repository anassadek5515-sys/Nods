const express = require('express');
const nodemailer = require('nodemailer');
const axios = require('axios');
const cheerio = require('cheerio');

const app = express();
app.use(express.json());

const MY_WALLET = process.env.MY_WALLET || "0x9426A467E0fFF34981656bd98580f60CFE395364";
const PLATFORM_URL = process.env.PLATFORM_URL || "https://your-platform-domain.com";
const SMTP_HOST = process.env.SMTP_HOST || "smtp.gmail.com";
const SMTP_PORT = process.env.SMTP_PORT ? parseInt(process.env.SMTP_PORT, 10) : 587;
const SMTP_USER = process.env.SMTP_USER || "your-email@gmail.com";
const SMTP_PASS = process.env.SMTP_PASS || "your-email-password";

const transporter = nodemailer.createTransport({
  host: SMTP_HOST,
  port: SMTP_PORT,
  secure: false,
  auth: {
    user: SMTP_USER,
    pass: SMTP_PASS
  }
});

async function crawlAndExtractContact(companyWebsite, companyId) {
  const contactPageUrl = `${companyWebsite.replace(/\/$/, '')}/contact`;
  try {
    const response = await axios.get(contactPageUrl, { timeout: 4000 });
    const $ = cheerio.load(response.data);

    const langAttr = $('html').attr('lang') || 'en';
    const pageText = $('body').text();
    const isArabic = langAttr.includes('ar') || /[\u0600-\u06FF]/.test(pageText);

    let extractedEmail = null;
    $('a[href^="mailto:"]').each((_, el) => {
      const mailto = $(el).attr('href');
      if (mailto) {
        extractedEmail = mailto.replace('mailto:', '').split('?')[0];
      }
    });

    return {
      email: extractedEmail || `contact@company-target-${companyId}-example.com`,
      language: isArabic ? 'ar' : 'en',
      contactUrl: contactPageUrl
    };
  } catch (error) {
    return {
      email: `contact@company-target-${companyId}-example.com`,
      language: 'en',
      contactUrl: contactPageUrl
    };
  }
}

function getLocalizedEmailContent(companyName, platformUrl, wallet, lang) {
  if (lang === 'ar') {
    return {
      subject: `🚀 عرض شراكة ونمو استراتيجي لشركة ${companyName}`,
      html: `
        <div style="font-family: Arial, sans-serif; direction: rtl; text-align: right; color: #333; line-height: 1.6; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px; max-width: 600px; margin: auto;">
          <h2 style="color: #1e3a8a; text-align: center;">⚡ منصة النمو الذكي وتوليد العملاء</h2>
          <p>مرحباً فريق <strong>${companyName}</strong>،</p>
          <p>قمنا بزيارة موقعكم عبر صفحة اتصل بنا، واكتشفنا فرصاً ضخمة لمضاعفة مبيعاتكم عبر محرك النمو الأوتوماتيكي الخاص بنا (يعمل 24/7).</p>
          <div style="background-color: #f8fafc; border-right: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
            <h3 style="margin-top: 0; color: #047857;">💳 تفاصيل الاشتراك والتفعيل الفوري ($200/شهر):</h3>
            <p>للاشتراك الفوري وتفعيل نظامك المعزول، يرجى التحويل حصراً عبر شبكة <b>BNB Smart Chain (BEP20)</b> إلى المحفظة المعتمدة:</p>
            <p style="background: #1e293b; color: #10b981; padding: 10px; font-family: monospace; text-align: center; border-radius: 4px; word-break: break-all;">${wallet}</p>
            <p style="text-align: center; margin-top: 15px;">
              <a href="${platformUrl}" target="_blank" style="background-color: #10b981; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold;">🌐 زيارة المنصة وبوابة الدفع</a>
            </p>
          </div>
          <p>بعد إتمام التحويل، أرسل رقم المعاملة (TXID) عبر موقعنا ليتم تفعيل حسابك أوتوماتيكياً خلال ثوانٍ.</p>
          <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 20px 0;">
          <p style="font-size: 12px; color: #64748b; text-align: center;">AI Growth & B2B Scaling Team</p>
        </div>
      `
    };
  } else {
    return {
      subject: `🚀 Partnership & B2B Growth Proposal for ${companyName}`,
      html: `
        <div style="font-family: Arial, sans-serif; color: #333; line-height: 1.6; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px; max-width: 600px; margin: auto;">
          <h2 style="color: #1e3a8a; text-align: center;">⚡ AI Growth & Client Acquisition Platform</h2>
          <p>Hello team at <strong>${companyName}</strong>,</p>
          <p>Our autonomous growth crawler visited your contact channel and identified high potential for automated B2B scaling.</p>
          <div style="background-color: #f8fafc; border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; border-radius: 4px;">
            <h3 style="margin-top: 0; color: #047857;">💳 Instant Subscription ($200/month):</h3>
            <p>To activate your secure environment, transfer exclusively via <b>BNB Smart Chain (BEP20)</b> to our wallet:</p>
            <p style="background: #1e293b; color: #10b981; padding: 10px; font-family: monospace; text-align: center; border-radius: 4px; word-break: break-all;">${wallet}</p>
            <p style="text-align: center; margin-top: 15px;">
              <a href="${platformUrl}" target="_blank" style="background-color: #10b981; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold;">🌐 Visit Platform & Activate</a>
            </p>
          </div>
          <p>Send your TXID after payment for instant automated provisioning.</p>
          <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 20px 0;">
          <p style="font-size: 12px; color: #64748b; text-align: center;">AI Growth & Scaling Team</p>
        </div>
      `
    };
  }
}

app.get('/api/execute-campaign', async (req, res) => {
  try {
    const batchSize = 15;
    let processedCount = 0;
    let results = [];

    for (let i = 1; i <= batchSize; i++) {
      const companyId = Math.floor(Math.random() * 40000) + 1;
      const company = {
        id: companyId,
        name: `Target Company #${companyId}`,
        website: `https://company-target-${companyId}-example.com`
      };

      const contactInfo = await crawlAndExtractContact(company.website, company.id);
      const emailContent = getLocalizedEmailContent(company.name, PLATFORM_URL, MY_WALLET, contactInfo.language);

      try {
        await transporter.sendMail({
          from: `"AI Growth Platform" <${SMTP_USER}>`,
          to: contactInfo.email,
          subject: emailContent.subject,
          html: emailContent.html
        });
        results.push({ company: company.name, email: contactInfo.email, lang: contactInfo.language, status: 'sent' });
        processedCount++;
      } catch (mailError) {
        results.push({ company: company.name, email: contactInfo.email, status: 'failed', error: mailError.message });
      }
    }

    res.status(200).json({
      success: true,
      message: `Vercel Serverless Batch executed! Successfully processed ${processedCount} emails.`,
      details: results,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

app.get('/', (req, res) => {
  res.status(200).json({
    status: 'Vercel Autonomous Outreach Engine is Online 🟢',
    message: 'Serverless architecture ready for 40k batch execution via Cron.'
  });
});

module.exports = app;
