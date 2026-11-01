const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware لقراءة الـ JSON
app.use(express.json());

// مسار رئيسي للتأكد إن النود شغالة وصاحية
app.get('/', (req, res) => {
    res.status(200).json({
        status: 'online',
        message: 'Node is active and running successfully!',
        timestamp: new Date()
    });
});

// مسار معالجة البيانات والطلبات الخاصة بالمنصة
app.post('/api/process', (req, res) => {
    const data = req.body;
    // هنا بيتم معالجة صفقات الـ 14 نود
    res.status(200).json({
        success: true,
        processedData: data,
        note: 'Data processed successfully by the active node.'
    });
});

// تشغيل السيرفر على البورت المتاح
app.listen(PORT, () => {
    console.log(`Node server is running on port ${PORT}`);
});
