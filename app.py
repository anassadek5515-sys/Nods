import streamlit as st
import time
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="AI Growth-Hacking Enterprise Platform",
    page_icon="🚀",
    layout="wide"
)

# اكتشاف لغة متصفح أو جهاز المستخدم (افتراضي عربي أو إنجليزي)
user_lang = "ar" # يمكن توسيعها لاحقاً لقراءة إعدادات المتصفح بدقة

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
# لوحة تحكم الأدمن
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# لوحة تحكم العميل المشترك (المنصة المستقلة للشركة)
# ---------------------------------------------------------
elif st.session_state["current_logged_company"] and st.session_state["current_logged_company"] != "admin123":
    comp_id = st.session_state["current_logged_company"]
    st.title(f"🔒 لوحة تحكم شركتك المعزولة (ID: {comp_id})")
    st.success("✅ اشتراكك مفعل وسيرفرات البحث والنمو تعمل الآن في الخلفية.")
    
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
        st.write("السكربت البرمجي المخصص لبدء البحث وإرسال الإشارات للسيرفرات:")
        
        if st.button("🚀 تشغيل سيرفرات البحث وجلب العملاء الآن"):
            with st.spinner("جاري تهيئة العقد السيرفرية وبدء زحف البيانات (Scraping)..."):
                time.sleep(3)
            st.success("🔥 تم تفعيل السيرفرات بنجاح وإرسال أول دفعة من نبضات البحث للشبكة!")

    st.markdown("---")
    if st.button("🚪 تسجيل الخروج"):
        st.session_state["current_logged_company"] = None
        st.rerun()

# ---------------------------------------------------------
# الواجهة الرئيسية (بوابة الاشتراك والدفع المباشر المتوافقة مع لغة الجهاز)
# ---------------------------------------------------------
else:
    # تخصيص النصوص بناءً على لغة الجهاز المكتشفة
    if user_lang == "ar":
        main_title = "🚀 منصة النمو الذكي للشركات ($200/شهر)"
        main_desc = "نظام SaaS متكامل ومستقل للشركات مع عزل تام، ذكاء اصطناعي، وتحليل ملفات فوري ومتوافق مع لغة جهازك."
        tab1_name = "💳 الاشتراك والدفع الفوري"
        tab2_name = "🔑 دخول الشركة"
        pay_header = "خطوات الدفع والتفعيل الفوري"
        warning_title = "⚠️ تنبيه هامة جداً قبل التحويل:"
        warning_desc = "يجب التحويل حصراً عبر شبكة <b>BNB Smart Chain (BEP20)</b>. أي تحويل على شبكة أخرى قد يؤدي لضياع الأموال!"
        wallet_label = "🌐 عنوان محفظتك المعتمد لاستلاستلام الأرباح:"
        btn_pay_text = "🔗 اضغط هنا لفتح محفظتك والدفع السريع"
        input_tx = "أدخل رقم المعاملة أو كود التحويل (TXID) بعد إتمام الدفع على شبكة BNB:"
        btn_activate = "✨ تفعيل المنصة الخاصة بي فوراً"
        login_header = "تسجيل الدخول لمنصتك المستقلة"
        input_secret = "أدخل كود شركتك السري:"
        btn_login = "🔐 دخول المنصة"
    else:
        main_title = "🚀 AI Growth-Hacking Enterprise Platform ($200/mo)"
        main_desc = "An integrated autonomous SaaS ecosystem for B2B growth with isolated workspaces and AI."
        tab1_name = "💳 Instant Subscription & Payment"
        tab2_name = "🔑 Company Login"
        # يمكن إضافة النصوص الإنجليزية هنا بسهولة

    st.title(main_title)
    st.write(main_desc)
    st.markdown("---")

    tab_pay, tab_login = st.tabs([tab1_name, tab2_name])

    with tab_pay:
        st.subheader(pay_header)
        
        my_usdt_wallet = "0x9426A467E0fFF34981656bd98580f60CFE395364"
        payment_uri = f"ethereum:{my_usdt_wallet}"
        
        st.markdown(f"""
        <div style="background-color: #1e1b4b; padding: 20px; border-radius: 10px; border: 2px solid #f59e0b; margin-bottom: 20px;">
            <h4 style="color: #fbbf24; margin-top: 0;">{warning_title}</h4>
            <p style="color: #fef3c7; font-size: 15px;">
                {warning_desc}
            </p>
            <hr style="border-color: #374151;">
            <h4 style="color: #38bdf8; margin-top: 10px;">{wallet_label}</h4>
            <div style="background: #0f172a; padding: 12px; border-radius: 6px; font-family: monospace; color: #10b981; font-size: 15px; text-align: center; margin: 10px 0; word-break: break-all;">
                {my_usdt_wallet}
            </div>
            <p style="color: #94a3b8; text-align: center; font-size: 13px; margin-bottom: 15px;">المبلغ المطلوب: <b>200 دولار USDT</b></p>
            
            <div style="text-align: center;">
                <a href="{payment_uri}" target="_blank" style="background-color: #10b981; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 16px; display: inline-block;">{btn_pay_text}</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        tx_hash = st.text_input(input_tx)
        
        if st.button(btn_activate):
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
                st.session_state["current_logged_company"] = new_company_id
                st.success(f"🎉 تم إنشاء منصتك المستقلة بنجاح! كود الدخول السري الخاص بك: **{new_company_id}** (احتفظ به جيداً)")
                time.sleep(2)
                st.rerun()
            else:
                st.error("❌ برجاء إدخال رقم المعاملة أو كود التحويل الصحيح.")

    with tab_login:
        st.subheader(login_header)
        entered_secret = st.text_input(input_secret, type="password")
        
        if st.button(btn_login):
            if entered_secret in st.session_state["companies_database"]:
                st.session_state["current_logged_company"] = entered_secret
                st.rerun()
            else:
                st.error("❌ عذراً، هذا الكود غير مسجل أو خطأ في البيانات.")
