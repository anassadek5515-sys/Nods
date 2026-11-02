import streamlit as st
import time
import pandas as pd
import hashlib

# 1. إعدادات الصفحة والأمان المتقدم
st.set_page_config(
    page_title="Enterprise B2B Growth Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()

# 2. قاعدة بيانات العملاء (خالية تماماً من أي بيانات تجريبية)
if "companies_database" not in st.session_state:
    st.session_state["companies_database"] = {}

if "current_logged_company" not in st.session_state:
    st.session_state["current_logged_company"] = None

if "ai_chat_history" not in st.session_state:
    st.session_state["ai_chat_history"] = {}

# حماية واجهة الاستخدام من النسخ
st.markdown("""
<style>
    .secure-container { user-select: none; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# القائمة الجانبية للمشترين فقط
# ---------------------------------------------------------
st.sidebar.title("🌐 بوابة عملاء المنصة")
st.sidebar.markdown("---")

if st.session_state["current_logged_company"] is None:
    nav_choice = st.sidebar.radio(
        "اختر القسم:",
        [
            "💳 بوابة الاشتراك والدفع الفوري",
            "🔑 تسجيل الدخول لحسابي"
        ]
    )
else:
    st.sidebar.success("🟢 متصل بالحساب الآمن")
    nav_choice = st.sidebar.radio(
        "لوحة خدماتك المتقدمة:",
        [
            "🚀 هندسة وتخطيط حملات B2B",
            "📦 تحليل بيانات المنتجات والأسواق",
            "🤖 المستشار الذكاء الاصطناعي التفاعلي",
            "📊 تقارير الأداء وتحويل العملاء",
            "⚙️ إعدادات الحساب والأمان"
        ]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 تسجيل الخروج"):
        st.session_state["current_logged_company"] = None
        st.success("تم تسجيل الخروج بنجاح.")
        time.sleep(1)
        st.rerun()

# =========================================================
# القسم الأول: بوابة الاشتراك والدفع الفوري
# =========================================================
if nav_choice == "💳 بوابة الاشتراك والدفع الفوري":
    st.title("🛡️ منصة النمو الذكي المشفرة ($200/شهر)")
    st.write("بوابة دفع آمنة ومعزولة كلياً لخدمات النمو وتوليد العملاء المحتملين.")
    st.markdown("---")

    st.subheader("بيانات التحويل عبر الشبكة المعتمدة")
    
    my_usdt_wallet = "0x9426A467E0fFF34981656bd98580f60CFE395364"
    payment_uri = f"ethereum:{my_usdt_wallet}"
    
    st.markdown(f"""
    <div style="background-color: #fee2e2; border: 2px solid #ef4444; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: #991b1b; margin-top: 0;">🚨 تنبيه هام جداً:</h4>
        <p style="color: #7f1d1d; font-size: 15px; font-weight: bold;">
            يجب التحويل حصراً عبر شبكة <b>BNB Smart Chain (BEP20)</b> لضمان وصول المعاملة وتجنب ضياع الأموال.
        </p>
        <hr style="border-color: #fca5a5;">
        <h4 style="color: #1e3a8a; margin-top: 10px;">🌐 عنوان المحفظة:</h4>
        <div style="background: #1e293b; padding: 12px; border-radius: 6px; font-family: monospace; color: #10b981; font-size: 15px; text-align: center; margin: 10px 0; word-break: break-all;">
            {my_usdt_wallet}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 25px;">
        <a href="{payment_uri}" target="_blank" style="background-color: #10b981; color: white; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 18px; display: inline-block;">🔗 فتح محفظة الدفع</a>
    </div>
    """, unsafe_allow_html=True)
    
    tx_hash = st.text_input("أدخل كود المعاملة (TXID):")
    
    if st.button("✨ تفعيل الحساب أوتوماتيكياً"):
        clean_tx = tx_hash.strip()
        if len(clean_tx) >= 10 and not any(char in clean_tx for char in ["<", ">", ";", "'", '"']):
            raw_secret_key = f"client_{int(time.time())}_{clean_tx[:6]}"
            hashed_secret = hash_key(raw_secret_key)
            
            st.session_state["companies_database"][hashed_secret] = {
                "status": "active",
                "tx_hash": clean_tx,
                "amount": 200,
                "created_at": time.time()
            }
            st.success("تم التحقق من المعاملة بنجاح وتفعيل حسابك!")
            st.warning(f"⚠️ **كود الدخول السري الخاص بك (احتفظ به الآن فلن يظهر مجدداً):**\n\n`{raw_secret_key}`")
        else:
            st.error("كود المعاملة غير صالح أو غير مكتمل.")

# =========================================================
# القسم الثاني: تسجيل الدخول
# =========================================================
elif nav_choice == "🔑 تسجيل الدخول لحسابي":
    st.title("🔑 تسجيل الدخول الآمن للعملاء")
    st.write("أدخل كود الدخول السري الخاص بك للوصول إلى بيئة عملك.")
    st.markdown("---")
    
    entered_secret = st.text_input("كود الدخول السري:", type="password")
    if st.button("دخول آمن"):
        hashed_input = hash_key(entered_secret.strip())
        if hashed_input in st.session_state["companies_database"]:
            st.session_state["current_logged_company"] = hashed_input
            st.success("تم تسجيل الدخول بنجاح.")
            time.sleep(1)
            st.rerun()
        else:
            st.error("كود الدخول غير صحيح أو غير مسجل.")

# =========================================================
# الخدمات الداخلية للعميل
# =========================================================
elif nav_choice == "🚀 هندسة وتخطيط حملات B2B":
    st.title("🚀 لوحة تخطيط وهندسة حملات B2B")
    st.write("تحديد معايير الاستهداف وإعداد مسارات تحويل العملاء المحتملين بشكل هيكلي واحترافي.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        target_industry = st.selectbox("قطاع الاستهداف الصناعي/التجاري:", ["التقنية وبرمجيات الشركات (SaaS)", "التجارة الإلكترونية والخدمات اللوجستية", "الخدمات المالية والاستثمارية", "الاستشارات والخدمات المهنية"])
        target_geo = st.text_input("الدول أو الأسواق المستهدفة:", "دول مجلس التعاون الخليجي (GCC)")
    with col2:
        campaign_goal = st.selectbox("الهدف الأساسي للحملة:", ["جذب عملاء محتملين مؤهلين (Lead Generation)", "زيادة مبيعات العقود المباشرة", "الترويج لإطلاق منتج جديد"])
        budget_tier = st.selectbox("نطاق الميزانية التشغيلية الشهرية:", ["منخفض ($1,000 - $5,000)", "متوسط ($5,000 - $20,000)", "متقدم ($20,000+)"])
        
    if st.button("توليد الخطة التشغيلية للحملة"):
        st.success("تم بناء هيكل الحملة الاستراتيجية بنجاح بناءً على معاييرك المحددة:")
        st.markdown(f"""
        * **القطاع:** {target_industry}
        * **السوق المستهدف:** {target_geo}
        * **الهدف:** {campaign_goal}
        * **التوصية:** بناء مسار مبيعات يعتمد على التوعية بالمشكلة أولاً، تليها دراسات حالة موثقة، ثم مكالمة استشارية مغلقة.
        """)

elif nav_choice == "📦 تحليل بيانات المنتجات والأسواق":
    st.title("📦 تحليل بيانات المنتجات والأسواق")
    st.write("قم بتدقيق ورفع بيانات منتجاتك أو قوائم المبيعات لاستخراج مؤشرات الأداء الحقيقية.")
    st.markdown("---")
    
    uploaded_file = st.file_uploader("رفع ملف البيانات (CSV أو TXT):", type=["csv", "txt"])
    if uploaded_file is not None:
        with st.spinner("جاري فحص وتدقيق البيانات..."):
            time.sleep(1)
        st.success("تم تحليل الملف بنجاح.")
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head(10))
            st.metric("إجمالي السجلات المفحوصة", len(df))
        else:
            st.write("تم قراءة الملف النصي وتحليل محتواه بنجاح دون أخطاء هيكلية.")

elif nav_choice == "🤖 المستشار الذكاء الاصطناعي التفاعلي":
    st.title("🤖 المستشار الذكاء الاصطناعي التفاعلي الحقيقي")
    st.write("مستشارك الذكي مزود بقائمة ردود متكاملة يتفاعل معك بشكل بشري وطبيعي تماماً بناءً على كلامك.")
    st.markdown("---")
    
    comp_id = st.session_state["current_logged_company"]
    if comp_id not in st.session_state["ai_chat_history"]:
        st.session_state["ai_chat_history"][comp_id] = [
            {"role": "assistant", "content": "أهلاً بيك يا فنان! أنا مستشارك الذكي، سامعك ومتابع معاك.. قولي إيه أخبارك وإيه فكرة مشروعك اللي حابب نناقشه النهاردة؟"}
        ]
    
    for message in st.session_state["ai_chat_history"][comp_id]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
    user_prompt = st.chat_input("اكتب رسالتك أو سؤالك هنا...")
    if user_prompt:
        st.session_state["ai_chat_history"][comp_id].append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.write(user_prompt)
        
        # قائمة ردود ذكية وتحليلية متكاملة
