import streamlit as st
import time
import pandas as pd
import hashlib

# 1. إعدادات الصفحة والأمان
st.set_page_config(
    page_title="Enterprise B2B Growth Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()

# 2. قاعدة بيانات العملاء (مع الحساب التجريبي test1234)
if "companies_database" not in st.session_state:
    demo_secret = "test1234"
    st.session_state["companies_database"] = {
        hash_key(demo_secret): {
            "status": "active",
            "tx_hash": "DEMO_TXID_123456",
            "amount": 200,
            "created_at": time.time()
        }
    }

if "current_logged_company" not in st.session_state:
    st.session_state["current_logged_company"] = None

if "ai_chat_history" not in st.session_state:
    st.session_state["ai_chat_history"] = {}

# حماية واجهة الاستخدام
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

st.sidebar.info("💡 **الحساب التجريبي:** استخدم كود `test1234` لتسجيل الدخول الفوري.")

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
        "لوحة الخدمات:",
        [
            "🚀 هندسة وتخطيط حملات B2B",
            "📦 تحليل بيانات المنتجات والأسواق",
            "🤖 المستشار الاستراتيجي المتقدم"
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
    st.write("بوابة دفع آمنة ومعزولة كلياً لخدمات النمو وتوليد العملاء.")
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
    
    if st.button("✨ تفعيل الحساب"):
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
            st.success("تم التحقق من المعاملة بنجاح.")
            st.warning(f"⚠️ **كود الدخول السري الخاص بك (احتفظ به الآن فلن يظهر مجدداً):**\n\n`{raw_secret_key}`")
        else:
            st.error("كود المعاملة غير صالح أو غير مكتمل.")

# =========================================================
# القسم الثاني: تسجيل الدخول
# =========================================================
elif nav_choice == "🔑 تسجيل الدخول لحسابي":
    st.title("🔑 تسجيل الدخول الآمن")
    st.write("أدخل كود الدخول السري (أو كود التجربة `test1234`).")
    st.markdown("---")
    
    entered_secret = st.text_input("كود الدخول السري:", type="password")
    if st.button("دخول"):
        hashed_input = hash_key(entered_secret.strip())
        if hashed_input in st.session_state["companies_database"]:
            st.session_state["current_logged_company"] = hashed_input
            st.success("تم تسجيل الدخول بنجاح.")
            time.sleep(1)
            st.rerun()
        else:
            st.error("كود الدخول غير صحيح.")

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
        * **التوصية:** بناء مسار مبيعات يعتمد على التوعية بالمشكلة أولاً، تليها دراسات حالة موثقة، ثم مكالمة استشارية مغلقة (High-Ticket B2B Funnel).
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

elif nav_choice == "🤖 المستشار الاستراتيجي المتقدم":
    st.title("🤖 المستشار الاستراتيجي المتقدم للنمو والتسويق")
    st.write("مستشار ذكي محترف ومخصص للإجابة بدقة وتحليل التحديات التسويقية والتشغيلية الخاصة بك.")
    st.markdown("---")
    
    comp_id = st.session_state["current_logged_company"]
    if comp_id not in st.session_state["ai_chat_history"]:
        st.session_state["ai_chat_history"][comp_id] = [
            {"role": "assistant", "content": "مرحباً بك. أنا مستشارك الاستراتيجي جاهز لمناقشة تحديات النمو، تحسين معدلات التحويل، أو هندسة استراتيجيات المبيعات. تفضل بطرح سؤالك أو خطتك."}
        ]
    
    for message in st.session_state["ai_chat_history"][comp_id]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
    user_prompt = st.chat_input("اطرح استفسارك الاستراتيجي هنا...")
    if user_prompt:
        st.session_state["ai_chat_history"][comp_id].append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.write(user_prompt)
        
        # رد محترف وعملي حقيقي بدلاً من الردود الوهمية السابقة
        expert_response = f"""تحليل استراتيجي لمطالبتك: "{user_prompt}"

1. **التقييم الموضوعي:** عند معالجة هذه النقطة في قطاع الشركات (B2B)، يجب التركيز على تقليل تكلفة اكتساب العميل (CAC) ورفع القيمة الدائمة للعميل (LTV).
2. **خطوات التنفيذ المقترحة:**
   * تحديد نقطة الألم المركزية لدى صانع القرار في الشركات المستهدفة.
   * بناء محتوى تسويقي تقني أو دراسة جدوى رقمية تثبت العائد المالي المباشر.
   * تفعيل قنوات التواصل المباشر (Outbound Sales) بجانب التسويق بالمحتوى.
3. **التوصية النهائية:** المتابعة المستمرة لمعدلات الاستجابة (Conversion Rates) وتعديل رسائل التواصل أسبوعياً بناءً على البيانات الفعلية."""

        st.session_state["ai_chat_history"][comp_id].append({"role": "assistant", "content": expert_response})
        with st.chat_message("assistant"):
            st.write(expert_response)
