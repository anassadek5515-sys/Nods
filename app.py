import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Growth Platform SaaS", page_icon="🚀", layout="wide")

st.title("🚀 منصة الأتمتة والنمو الذكي")
st.markdown("---")

# 🔐 لوحة التحكم الخاصة بك (الأدمن المشفر)
st.sidebar.header("🔐 لوحة التحكم الخاصة بك")
admin_pass = st.sidebar.text_input("كلمة مرور الإدارة", type="password")

if admin_pass == "admin123": # تقدر تغير كلمة المرور براحتك
    st.sidebar.success("✅ تم تسجيل الدخول بنجاح")
    st.sidebar.subheader("📊 إحصائيات الأرباح")
    st.sidebar.metric(label="إجمالي الأرباح", value="$1,250")
    st.sidebar.metric(label="بالجنيه المصري", value="62,500 EGP")
    st.sidebar.markdown("---")
    st.sidebar.subheader("🤖 حالة الـ 6 سيرفرات (Workers)")
    for i in range(1, 7):
        st.sidebar.text(f"Worker {i}: 🟢 شغال أوتوماتيك")
else:
    if admin_pass:
        st.sidebar.error("❌ كلمة المرور غير صحيحة")

# 🌐 واجهة العميل العامة والدفع
st.header("🌐 بوابة العملاء والاشتراك بالحملات")

# نظام الحملة النشطة الوحيدة (Single Active Campaign)
active_campaign = st.session_state.get("active_campaign", None)

if active_campaign:
    st.warning(f"⚠️ عذراً، هناك حملة نشطة حالياً لجلسة عميل آخر ('{active_campaign}'). زر الدفع متوقف مؤقتاً حتى تنتهي الحملة الحالية وتفرغ القاعدة تلقائياً.")
    st.info("⏰ انتظر قليلاً حتى تكتمل الحملة الحالية ليفتح لك الدور فوراً.")
else:
    st.success("🟢 النظام متاح حالياً! يمكنك إتمام الدفع وبدء حملتك الفورية.")
    
    with st.form("campaign_form"):
        st.subheader("💳 تفاصيل الدفع والاشتراك (عبر Paddle)")
        client_name = st.text_input("اسم الشركة / العميل")
        client_email = st.text_input("البريد الإلكتروني")
        target_url = st.text_input("رابط موقعك المطلوب الترويج له (Target URL)")
        campaign_message = st.text_area("نص الرسالة التسويقية أو تفاصيل الاتصال")
        
        duration = st.selectbox("اختر خطة المدة", ["12 ساعة", "يوم كامل (24 ساعة)", "7 أيام"])
        
        pay_button = st.form_submit_button("💳 ادفع الآن وابدأ الحملة أوتوماتيكياً")
        
        if pay_button:
            if client_name and target_url:
                st.session_state["active_campaign"] = client_name
                st.success(f"🎉 تم الدفع بنجاح! تم تفعيل حملتك وحجز السيستم خصيصاً لك يا {client_name}.")
                st.info(f"🚀 الـ 6 سيرفرات بدأت الآن في العمل والإرسال لموقعك: {target_url}")
                st.rerun()
            else:
                st.error("⚠️ برجاء إدخال اسم الشركة ورابط الموقع على الأقل.")

# زر تحكم بالأدمن لتصفير الحملة لو احتجت
if admin_pass == "admin123" and active_campaign:
    st.markdown("---")
    if st.button("🛑 إنهاء الحملة الحالية يدوياً وإتاحة النظام لعميل جديد"):
        st.session_state["active_campaign"] = None
        st.success("✅ تم إفراغ النظام وجاهز لعميل جديد!")
        st.rerun()
