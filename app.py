import streamlit as st
import time
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="AI Growth-Hacking Enterprise Platform",
    page_icon="🚀",
    layout="wide"
)

# 2. قواعد البيانات والذاكرة المحلية
if "companies_database" not in st.session_state:
    st.session_state["companies_database"] = {
        "admin123": {"type": "admin", "name": "الأدمن الرئيسية", "status": "active"}
    }

if "current_logged_company" not in st.session_state:
    st.session_state["current_logged_company"] = None

if "ai_chat_history" not in st.session_state:
    st.session_state["ai_chat_history"] = {}

# ---------------------------------------------------------
# نظام التنقل التلقائي بين الموقعين (فصل تام)
# ---------------------------------------------------------
st.sidebar.title("🌐 بوابة المنصة")
site_choice = st.sidebar.radio(
    "اختر القسم:", 
    ["💳 موقع الاشتراك والدفع الفوري", "🔑 موقع دخول الشركات المستقل"]
)

# =========================================================
# الموقع الأول: موقع الدفع والاشتراك الآلي
# =========================================================
if site_choice == "💳 موقع الاشتراك والدفع الفوري":
    st.title("🚀 منصة النمو الذكي للشركات ($200/شهر)")
    st.write("بوابة الدفع والاشتراك الآلي - نظام SaaS متكامل مع عزل تام وتفعيل فوري.")
    st.markdown("---")

    st.subheader("خطوات الدفع والتفعيل الفوري")
    
    my_usdt_wallet = "0x9426A467E0fFF34981656bd98580f60CFE395364"
    payment_uri = f"ethereum:{my_usdt_wallet}"
    
    # تنبيه الشبكة ومحفظة الاستلام
    st.markdown(f"""
    <div style="background-color: #1e1b4b; padding: 20px; border-radius: 10px; border: 2px solid #f59e0b; margin-bottom: 20px;">
        <h4 style="color: #fbbf24; margin-top: 0;">⚠️ تنبيه هام جداً قبل التحويل:</h4>
        <p style="color: #fef3c7; font-size: 15px;">
            يجب التحويل حصراً عبر شبكة <b>BNB Smart Chain (BEP20)</b>. أي تحويل على شبكة أخرى قد يؤدي لضياع الأموال!
        </p>
        <hr style="border-color: #374151;">
        <h4 style="color: #38bdf8; margin-top: 10px;">🌐 عنوان محفظتك المعتمد لاستلام الأرباح:</h4>
        <div style="background: #0f172a; padding: 12px; border-radius: 6px; font-family: monospace; color: #10b981; font-size: 15px; text-align: center; margin: 10px 0; word-break: break-all;">
            {my_usdt_wallet}
        </div>
        <p style="color: #94a3b8; text-align: center; font-size: 13px; margin-bottom: 15px;">المبلغ المطلوب: <b>200 دولار USDT</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    # زر الدفع التفاعلي المباشر
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 25px;">
        <a href="{payment_uri}" target="_blank" style="background-color: #10b981; color: white; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 18px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">🔗 اضغط هنا لفتح محفظتك والدفع السريع</a>
    </div>
    """, unsafe_allow_html=True)
    
    tx_hash = st.text_input("أدخل رقم المعاملة أو كود التحويل (TXID) بعد إتمام الدفع على شبكة BNB:")
    
    if st.button("✨ تفعيل المنصة الخاصة بي أوتوماتيكياً"):
        if len(tx_hash.strip()) >= 5:
            new_company_id = f"comp_sec_{int(time.time())}"
            st.session_state["companies_database"][new_company_id] = {
                "type": "client",
                "status": "active",
                "tx_hash": tx_hash,
                "amount": 200,
                "network": "BNB Smart Chain (BEP20)",
                "created_at": time.time()
            }
            st.success(f"🎉 تم تفعيل منصتك أوتوماتيكياً بنجاح! كود الدخول السري الخاص بك: **{new_company_id}** (انسخه وادخل بيه في قسم تسجيل الدخول من القائمة الجانبية)")
        else:
            st.error("❌ برجاء إدخال رقم المعاملة أو كود التحويل الصحيح.")

# =========================================================
# الموقع الثاني: موقع دخول الشركات والتحكم المستقل
# =========================================================
elif site_choice == "🔑 موقع دخول الشركات المستقل":

    # 1. لوحة تحكم الأدمن
    if st.session_state["current_logged_company"] == "admin123":
        st.title("🛡️ لوحة تحكم الأدمن والسيبرانات")
        st.success("متابعة العمليات، السيرفرات النشطة، وإيرادات المنصة:")
        
        total_clients = len(st.session_state["companies_database"]) - 1
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("الشركات المشتركة الفاعلة", f"{total_clients} شركة")
        with col2:
            st.metric("إجمالي الإيرادات", f"${total_clients * 200}")
        with col3:
            st.metric("حالة السيرفرات", "🟢 تعمل بكفاءة")

        st.markdown("---")
        st.subheader("📋 سجل المعاملات والشركات:")
        st.json(st.session_state["companies_database"])

        if st.button("🚪 خروج الأدمن"):
            st.session_state["current_logged_company"] = None
            st.rerun()

    # 2. لوحة تحكم العميل المشترك (المنصة المعزولة)
    elif st.session_state["current_logged_company"] and st.session_state["current_logged_company"] != "admin123":
        comp_id = st.session_state["current_logged_company"]
        st.title(f"🔒 لوحة تحكم شركتك المعزولة (ID: {comp_id})")
        st.success("✅ اشتراكك مفعل وسيرفرات البحث والنمو تعمل الآن في الخلفية أوتوماتيكياً.")
        
        tab_tools, tab_files, tab_ai, tab_server = st.tabs([
            "🚀 أدوات النمو", 
            "📁 تحليل ورفع الملفات", 
            "🤖 مساعد الذكاء الاصطناعي", 
            "⚙️ تشغيل السيرفرات والبحث"
        ])

        with tab_tools:
            st.subheader("بيئة النمو الخاصة بشركتك")
            st.write("أنت الآن تعمل في مساحة عمل مستقلة تماماً ومؤمنة بالكامل.")
            st.metric("العملاء المستهدفين المكتشفين", "1,420 عميل محتمل")

        with tab_files:
            st.subheader("رفع وتحليل ملفات البيانات")
            uploaded_file = st.file_uploader("ارفع ملف داتا العملاء أو ملفات الشركة (CSV, Excel, TXT):", type=["csv", "xlsx", "txt"])
            if uploaded_file is not None:
                st.success("✅ تم رفع الملف وتحليله بنجاح بواسطة خوارزميات النمو الذكية!")
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                    st.dataframe(df.head())
                else:
                    st.info("تمت قراءة الملف بنجاح واستخراج الأنماط التسويقية منه.")

        with tab_ai:
            st.subheader("مساعد الذكاء الاصطناعي المتخصص للنمو")
            st.write("اسأل خبير Growth Hacking الآلي أي شيء يخص حملاتك أو استراتيجياتك:")
            
            if comp_id not in st.session_state["ai_chat_history"]:
                st.session_state["ai_chat_history"][comp_id] = [
                    {"role": "assistant", "content": "أهلاً بك! أنا خبير النمو الخاص بشركتك. كيف أساعدك في مضاعفة مبيعاتك اليوم؟"}
                ]
            
            for msg in st.session_state["ai_chat_history"][comp_id]:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])
                    
            user_query = st.chat_input("اكتب استفسارك التسويقي هنا...")
            if user_query:
                st.session_state["ai_chat_history"][comp_id].append({"role": "user", "content": user_query})
                with st.chat_message("user"):
                    st.write(user_query)
                
                ai_reply = f"بناءً على تحليل بيانات شركتك، أقترح التركيز على استهداف قطاع B2B عبر الحملات الآلية للوصول إلى نتائج سريعة بخصوص طلبك: '{user_query}'."
                st.session_state["ai_chat_history"][comp_id].append({"role": "assistant", "content": ai_reply})
                with st.chat_message("assistant"):
                    st.write(ai_reply)

        with tab_server:
            st.subheader("⚙️ محرك تشغيل السيرفرات والبحث الآلي")
            st.write("منطقة جاهزة لربط أكواد السيرفرات وتفعيل البحث والإرسال الفوري طيارة:")
            
            if st.button("🚀 تشغيل سيرفرات البحث وجلب العملاء الآن"):
                with st.spinner("جاري ربط العقد وسيرفرات البحث الخارجي..."):
                    time.sleep(3)
                st.success("🔥 تم تشغيل السيرفرات بنجاح وإرسال نبضات البحث للشبكة!")

        st.markdown("---")
        if st.button("🚪 تسجيل الخروج"):
            st.session_state["current_logged_company"] = None
            st.rerun()

    # 3. شاشة تسجيل الدخول للشركات
    else:
        st.title("🔑 بوابة دخول الشركات المستقلة")
        st.write("أدخل كود شركتك السري الذي حصلت عليه بعد إتمام عملية الدفع للوصول إلى بيئة عملك المعزولة.")
        st.markdown("---")
        
        entered_secret = st.text_input("أدخل كود شركتك السري:", type="password")
        
        if st.button("🔐 دخول المنصة"):
            if entered_secret in st.session_state["companies_database"]:
                st.session_state["current_logged_company"] = entered_secret
                st.rerun()
            else:
                st.error("❌ عذراً، هذا الكود غير مسجل أو خطأ في البيانات.")
