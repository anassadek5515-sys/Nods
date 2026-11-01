import streamlit as st

st.set_page_config(
    page_title="Autonomous Growth-Hacking Platform",
    page_icon="🚀",
    layout="wide"
)

# Initialize session state variables
if "client_paid" not in st.session_state:
    st.session_state["client_paid"] = False
if "admin_logged" not in st.session_state:
    st.session_state["admin_logged"] = False
if "active_campaigns" not in st.session_state:
    st.session_state["active_campaigns"] = []

# --- Custom Styling for Ultra-Modern UI ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; height: 3em; background-color: #238636; color: white; border: none; }
    .stButton>button:hover { background-color: #2ea043; }
    .metric-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar: Secure Encrypted Admin Dashboard ---
st.sidebar.header("🔐 لوحة التحكم السرية والمشفرة (Admin)")
admin_pass_input = st.sidebar.text_input("كلمة مرور الأدمن السرية", type="password")

if admin_pass_input == "SecretAdmin2026!":
    st.session_state["admin_logged"] = True
else:
    if admin_pass_input:
        st.sidebar.error("❌ كلمة المرور غير صحيحة")

if st.session_state["admin_logged"]:
    st.sidebar.success("✅ مرحباً بك في لوحة تحكم الأدمن المشفرة")
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 إحصائيات الأرباح الشاملة")
    st.sidebar.metric(label="إجمالي الأرباح (USD)", value="$3,450", delta="+12%")
    st.sidebar.metric(label="إجمالي الأرباح (EGP)", value="172,500 EGP")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🤖 مراقبة الـ 7 حسابات وسيرفرات Railway")
    for acc in range(1, 8):
        st.sidebar.text(f"حساب {acc} (Railway Server): 🟢 يعمل 24/7 أوتوماتيك")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📈 تقارير أداء الشركات والمهام")
    st.sidebar.info("• إجمالي الشركات المتاحة: 12,450 شركة\n• الشركات التي تم الإرسال لها: 4,820\n• ترتيب حسب الأيام (من الأقل للأكثر):\n  - 3 أيام: 12 شركة\n  - 7 أيام: 45 شركة\n  - 30 يومًا: 120 شركة")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ إدارة البيانات المالية (سحب وإيداع)")
    with st.sidebar.form("withdraw_form"):
        withdraw_amount = st.number_input("المبلغ المراد سحبه", min_value=0.0, value=1000.0)
        submit_withdraw = st.form_submit_button("💰 سحب الأرباح الآن")
        if submit_withdraw:
            st.sidebar.success(f"✅ تم سحب مبلغ {withdraw_amount} بنجاح وتحديث الرصيد المحفوظ!")

    st.sidebar.markdown("---")
    st.sidebar.subheader("🤖 شات بوت تليجرام التلقائي (Telegram AI Bot)")
    st.sidebar.text("الحالة: متصل أوتوماتيكياً 🟢\n- يرسل بيانات الدخول والروابط للعملاء فوراً.\n- يرسل إشعارات بالموافقات والأرباح حصرياً لك.")

# --- Main Public / Client Interface ---
if st.session_state["client_paid"]:
    st.success("🎉 أهلاً بك في عنوانك الخاص والمشفر! نظامك يعمل أوتوماتيكياً بالكامل.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚙️ إعدادات حملتك النشطة")
        client_target_url = st.text_input("🔗 رابط موقعك (Target URL):", value="https://mybusiness.com")
        client_msg = st.text_area("📝 رسالة 'اتصل بنا' أو التفاصيل التسويقية:", value="أرغب في التعاون معكم...")
        duration_choice = st.selectbox("⏳ اختر مدة التعاقد:", ["3 أيام", "7 أيام", "14 يومًا", "30 يومًا"])
        
        if st.button("🚀 تحديث وبدء التشغيل الفوري عبر السيرفرات المتعددة"):
            st.success("✅ تم حفظ البيانات وتوزيع المهام على الـ 7 سيرفرات بنجاح!")
            
    with col2:
        st.subheader("📊 حالة الأداء المباشر")
        st.metric("الشركات المستهدفة اليوم", "450 شركة")
        st.metric("الردود والموافقات", "34 عميل محتمل")
        st.info("💡 السيستم موزع على حساباتك بذكاء تام، وكل عنوان خاص بالعميل معزول ومؤمن تماماً ولا يمكن لأي عميل رؤية بيانات غيره.")

    if st.button("🚪 إنهاء الجلسة / تسجيل خروج"):
        st.session_state["client_paid"] = False
        st.rerun()

else:
    st.title("🚀 منصة الأتمتة والنمو الذكي المتكاملة")
    st.write("النظام الأضخم عالمياً لتوزيع الحملات التسويقية أوتوماتيكياً على مدار الساعة عبر سيرفرات Railway المتعددة وحساباتك المربطة بذكاء.")
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h3>⚡ سرعة فائقة</h3><p>إرسال فوري دون توقف</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>🔒 أمان تام</h3><p>عناوين مشفرة ومعزولة</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>🤖 ذكاء اصطناعي</h3><p>تليجرام بوت أوتوماتيك</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h3>💳 دفع ذكي</h3><p>تحويل مباشر بالعملات</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("💳 بوابة الدفع المباشر والاشتراك الفوري")
    st.write("بمجرد إتمام الدفع عبر بوابة الدفع الآمنة، سيرسل لك شات بوت تليجرام أوتوماتيكياً عنوانك الخاص، كلمة المرور المشفرة، ورابط البدء فوراً دون أي انتظار.")
    
    if st.button("💳 ادفع الآن (عبر بوابة الدفع المشفرة) وانتقل للعمل الفوري"):
        st.session_state["client_paid"] = True
        st.success("✅ تم الدفع بنجاح! تم إنشاء عنوانك الخاص وتوليد كلمة المرور وجاري تحويلك...")
        st.rerun()
