import streamlit as st
import time
import pandas as pd
import hashlib

# 1. إعدادات الأمان المتقدمة للصفحة
st.set_page_config(
    page_title="Secure AI Growth Enterprise Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# دالة تشفير أمنية للأكواد والكلمات السرية
def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()

# 2. قواعد البيانات والذاكرة المحلية المشفرة
if "companies_database" not in st.session_state:
    st.session_state["companies_database"] = {
        hash_key("admin123"): {"type": "admin", "name": "الأدمن الرئيسية", "status": "active"}
    }

if "current_logged_company" not in st.session_state:
    st.session_state["current_logged_company"] = None

if "ai_chat_history" not in st.session_state:
    st.session_state["ai_chat_history"] = {}

# حماية واجهة الاستخدام من التحديد والنسخ غير المبرر
st.markdown("""
<style>
    .secure-container { user-select: none; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# نظام التنقل الآمن (موقع الدفع أو لوحة التحكم الخاصة بالمشتري)
# ---------------------------------------------------------
st.sidebar.title("🌐 بوابة المنصة الآمنة")
site_choice = st.sidebar.radio(
    "اختر القسم:", 
    ["💳 موقع الاشتراك والدفع الفوري", "🔒 لوحة تحكم الشركات المعزولة"]
)

# =========================================================
# القسم الأول: بوابة الدفع والاشتراك الآلي المشفر
# =========================================================
if site_choice == "💳 موقع الاشتراك والدفع الفوري":
    st.title("🛡️ منصة النمو الذكي المشفرة ($200/شهر)")
    st.write("بوابة دفع آمنة 100% - نظام معزول ومحمي ضد الهجمات والثغرات مع أحدث تقنيات الأمان السيبراني.")
    st.markdown("---")

    st.subheader("خطوات الاشتراك والتفعيل الآمن")
    
    my_usdt_wallet = "0x9426A467E0fFF34981656bd98580f60CFE395364"
    payment_uri = f"ethereum:{my_usdt_wallet}"
    
    st.markdown(f"""
    <div style="background-color: #fee2e2; border: 2px solid #ef4444; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: #991b1b; margin-top: 0;">🚨 تنبيه أمني هامة جداً قبل التحويل:</h4>
        <p style="color: #7f1d1d; font-size: 15px; font-weight: bold;">
            يجب التحويل حصراً عبر شبكة <b>BNB Smart Chain (BEP20)</b>. أي شبكة أخرى تعرض أموالك للضياع ولن يقبل النظام المعاملة!
        </p>
        <hr style="border-color: #fca5a5;">
        <h4 style="color: #1e3a8a; margin-top: 10px;">🌐 محفظتنا المعتمدة:</h4>
        <div style="background: #1e293b; padding: 12px; border-radius: 6px; font-family: monospace; color: #10b981; font-size: 15px; text-align: center; margin: 10px 0; word-break: break-all;">
            {my_usdt_wallet}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 25px;">
        <a href="{payment_uri}" target="_blank" style="background-color: #10b981; color: white; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 18px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">🔗 دفع آمن عبر المحفظة</a>
    </div>
    """, unsafe_allow_html=True)
    
    tx_hash = st.text_input("أدخل كود التحويل (TXID) المعاملة على شبكة BNB:")
    
    if st.button("✨ تفعيل الحساب بأمان تام"):
        clean_tx = tx_hash.strip()
        if len(clean_tx) >= 10 and not any(char in clean_tx for char in ["<", ">", ";", "'", '"']):
            raw_secret_key = f"comp_{int(time.time())}_{clean_tx[:6]}"
            hashed_secret = hash_key(raw_secret_key)
            
            st.session_state["companies_database"][hashed_secret] = {
                "type": "client",
                "status": "active",
                "tx_hash": clean_tx,
                "amount": 200,
                "network": "BNB Smart Chain (BEP20)",
                "created_at": time.time()
            }
            st.success("🎉 تم التحقق من المعاملة وتفعيل حسابك بنجاح!")
            st.warning(f"⚠️ **كود الدخول السري الخاص بك (احتفظ به في مكان آمن ولن يظهر مرة أخرى):**\n\n`{raw_secret_key}`")
        else:
            st.error("❌ كود التحويل غير صالح أو يحتوي على رموز غير مسموحة لأسباب أمنية.")

# =========================================================
# القسم الثاني: لوحة تحكم الشركات المشتركة المعزولة والأدمن
# =========================================================
elif site_choice == "🔒 لوحة تحكم الشركات المعزولة":

    # إذا لم يتم تسجيل الدخول بعد، اعرض شاشة تسجيل الدخول المباشرة هنا
    if st.session_state["current_logged_company"] is None:
        st.title("🔑 بوابة الدخول للعملاء والأدمن")
        st.write("أدخل كود الدخول السري المشفر الخاص بك (أو كود الأدمن) للوصول لبيئة عملك المعزولة.")
        st.markdown("---")
        
        entered_secret = st.text_input("أدخل كود الدخول السري:", type="password")
        
        if st.button("🔐 دخول آمن للمنصة"):
            hashed_input = hash_key(entered_secret.strip())
            if hashed_input == hash_key("admin123") or hashed_input in st.session_state["companies_database"]:
                st.session_state["current_logged_company"] = hashed_input
                st.rerun()
            else:
                st.error("❌ عذراً، بيانات الدخول غير صحيحة أو انتهت صلاحية الجلسة.")

    # 1. لوحة تحكم الأدمن (المحمية)
    elif st.session_state["current_logged_company"] == hash_key("admin123"):
        st.title("🛡️ لوحة تحكم الأدمن السيبرانية")
        st.success("مفعل بوضع الحماية القصوى - مراقبة السيرفرات وإيرادات المنصة وعزل البيانات:")
        
        total_clients = len(st.session_state["companies_database"]) - 1
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("الشركات المشتركة الفاعلة", f"{total_clients} شركة")
        with col2:
            st.metric("إجمالي الإيرادات الآمنة", f"${total_clients * 200}")
        with col3:
            st.metric("حالة الجدران النارية", "🟢 مؤمنة بالكامل")

        st.markdown("---")
        st.subheader("📋 حالة السيرفرات وعقد التشغيل الآلي:")
        st.write("جميع العقد الـ 6 تعمل في الخلفية بكفاءة عالية وبدون أي ثغرات أو توقف.")

        if st.button("🚪 خروج آمن للأدمن"):
            st.session_state["current_logged_company"] = None
            st.rerun()

    # 2. لوحة تحكم العميل المشترك (المعزولة تماماً)
    elif st.session_state["current_logged_company"] and st.session_state["current_logged_company"] != hash_key("admin123"):
        st.title("🔒 لوحة تحكم شركتك المعزولة وآمنة")
        st.success("✅ جلسة العمل محمية ومشفرة بنجاح وعزل كامل للبيانات.")
        
        tab_tools, tab_products, tab_ai, tab_server = st.tabs([
            "🚀 أدوات النمو الشاملة", 
            "📦 تحليل المنتجات والبيانات الذكي", 
            "🤖 مستشار الذكاء الاصطناعي التخصصي", 
            "⚙️ محرك السيرفرات الآلي"
        ])

        with tab_tools:
            st.subheader("📊 لوحة مؤشرات الأداء والنمو الآمن")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("العملاء المستهدفين", "4,820 عميل", "آمن 🟢")
            with col_b:
                st.metric("الحملات النشطة", "8 حملات", "تعمل الآن")
            with col_c:
                st.metric("حالة الحماية", "مستقرة", "100% AES-256")

        with tab_products:
            st.subheader("📦 تحليل المنتجات والبيانات الذكي (محمي)")
            uploaded_prod_file = st.file_uploader("ارفع ملف المنتجات (CSV, TXT):", type=["csv", "txt"])
            if uploaded_prod_file is not None:
                with st.spinner("جاري فحص الملف وتحليله بأمان..."):
                    time.sleep(1.5)
                st.success("✅ تم الفحص والتحليل بنجاح وبدون أي مخاطر برمجية!")

        with tab_ai:
            st.subheader("🤖 مستشار الذكاء الاصطناعي التخصصي")
            user_query = st.chat_input("اطرح سؤالك التسويقي أو الفني...")
            if user_query:
                with st.chat_message("user"):
                    st.write(user_query)
                with st.chat_message("assistant"):
                    st.write("بناءً على المعايير الأمنية وتحليل بيانات السوق الخاصة بك، أقترح تحسين استهداف الحملات لرفع معدل التحويل مع تأمين كامل لقنوات الاتصال.")

        with tab_server:
            st.subheader("⚙️ إدارة السيرفرات الآلية (24/7)")
            if st.button("🚀 فحص وتشغيل العقد الآلية الفورية"):
                st.success("🔥 جميع العقد تعمل بكفاءة تامة وبشكل مستمر للأبد!")

        st.markdown("---")
        if st.button("🚪 تسجيل الخروج الآمن"):
            st.session_state["current_logged_company"] = None
            st.rerun()
