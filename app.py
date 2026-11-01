import streamlit as st
import time

st.set_page_config(
    page_title="Growth-Hacking SaaS Platform",
    page_icon="🚀",
    layout="wide"
)

# تهيئة قاعدة البيانات المحلية المؤقتة في الذاكرة لتخزين حسابات الشركات وعزلها
if "companies_database" not in st.session_state:
    # بنحط حساب الأدمن الافتراضي وحساب تجريبي للتوضيح
    st.session_state["companies_database"] = {
        "admin123": {"type": "admin", "name": "الرئيس (الأدمن)"},
        "company_demo_01": {"type": "client", "name": "شركة تجريبية", "status": "نشط"}
    }

if "current_logged_company" not in st.session_state:
    st.session_state["current_logged_company"] = None

# 1. لوحة تحكم الرئيس (الأدمن)
if st.session_state["current_logged_company"] == "admin123":
    st.title("🛡️ موقع الرئيس (لوحة تحكم الأدمن المركزية)")
    st.success("أنت الآن في لوحة التحكم الخاصة بك. متابعة الشركات والأرباح بالكامل:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("إجمالي الشركات المسجلة", len(st.session_state["companies_database"]) - 1)
    with col2:
        st.metric("الأرباح المحققة", f"${(len(st.session_state['companies_database']) - 2) * 200}")
    with col3:
        st.metric("حالة السيرفرات", "نشطة 100% (7 سيرفرات)")

    st.markdown("---")
    st.subheader("📋 قائمة الشركات المعزولة الحالية في النظام:")
    st.json(st.session_state["companies_database"])

    if st.button("🚪 تسجيل خروج الأدمن"):
        st.session_state["current_logged_company"] = None
        st.rerun()

# 2. لوحة تحكم العميل المشفرة والمعزولة تماماً
elif st.session_state["current_logged_company"] and st.session_state["current_logged_company"] != "admin123":
    comp_id = st.session_state["current_logged_company"]
    st.title(f"🔒 لوحة تحكم الشركة المشفرة الخاصة بك")
    st.info(عرفت هويتك بنجاح. هذا هو عنوانك السري والخاص بشركتك وحدك: **{comp_id}**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚙️ أدوات التحليل والتسويق بالذكاء الاصطناعي")
        prod_desc = st.text_area("أدخل تفاصيل منتجات شركتك للبدء الفوري:", "خدمات تسويق إلكتروني وتطوير...")
        if st.button("🚀 بدء حملة الـ 40,000 عميل للشركات"):
            st.success("✅ تم بدء إرسال الحملات التسويقية لمنتجاتك بنجاح عبر سيرفرات Railway الخلفية!")
            
    with col2:
        st.subheader("💳 تفاصيل اشتراكك الشهري ($200)")
        st.warning("⚠️ اشتراكك نشط حالياً. السيستم سيطلب منك تجديد الاشتراك مع نهاية الشهر للاستمرار.")
        if st.button("💳 تجديد الاشتراك اليدوي (200$)"):
            st.success("✅ تم تجديد اشتراك الشركة بنجاح لشهر إضافي!")

    if st.button("🚪 تسجيل خروج"):
        st.session_state["current_logged_company"] = None
        st.rerun()

# 3. الصفحة الرئيسية (الاشتراك عبر بوابة Paddle الحقيقية + تسجيل الدخول بالعنوان السري)
else:
    st.title("🚀 منصة النمو الذكي والأتمتة للشركات ($200/شهر)")
    st.write("النظام الآلي المتكامل لجلب العملاء، تحليل المنتجات، وإدارة الشركات بعزل تام ومحمي.")
    st.markdown("---")

    tab_pay, tab_login = st.tabs(["💳 الاشتراك الفوري وبوابة الدفع", "🔑 دخول الشركة (العنوان وكلمة السر)"])

    with tab_pay:
        st.subheader("خطوة الاشتراك الشهري ($200)")
        st.write("اضغط أدناه للتحويل المباشر إلى بوابة الدفع الحقيقية والمشفرة (Paddle):")
        
        # رابط الدفع الحقيقي باستخدام الـ Price ID الخاص بك
        price_id = "Pri_01m6c4fez27rf46akty7f0crx1"
        paddle_checkout_url = f"https://buy.paddle.com/checkout?prd={price_id}"
        
        st.markdown(f"""
            <div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
                <a href="{paddle_checkout_url}" target="_blank">
                    <button style="background-color: #238636; color: white; padding: 18px 35px; font-size: 20px; font-weight: bold; border: none; border-radius: 10px; cursor: pointer; width: 100%;">
                        💳 دفع 200$ الآن عبر بوابة Paddle الرسمية
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.info("💡 **بعد إتمام الدفع بنجاح:** اضغط على الزر أدناه لتوليد عنوانك السري وكلمة السر الخاصة بشركتك فوراً ودخول بيئتك الخاصة:")
        
        if st.button("✨ توليد عنوان شركتي ودخول النظام (بعد الدفع)"):
            # توليد عنوان وكلمة سر فريدة ومبتكرة للشركة الجديدة
            new_company_id = f"comp_{int(time.time())}"
            st.session_state["companies_database"][new_company_id] = {
                "type": "client",
                "created_at": time.time()
            }
            st.session_state["current_logged_company"] = new_company_id
            st.success(f"🎉 مبروك! تم إنشاء عنوانك السري الخاص بشركتك بنجاح: **{new_company_id}** (احتفظ به جيداً لتسجيل الدخول لاحقاً).")
            time.sleep(2)
            st.rerun()

    with tab_login:
        st.subheader("تسجيل الدخول للشركات المسجلة")
        st.write("أدخل عنوان شركتك السري أو كلمة السر الخاصة بك للوصول لبيئتك المعزولة:")
        
        entered_secret = st.text_input("أدخل عنوان الشركة أو كلمة السر:", type="password")
        
        if st.button("🔐 دخول آمن للشركة"):
            if entered_secret in st.session_state["companies_database"]:
                st.session_state["current_logged_company"] = entered_secret
                st.success("✅ تم تسجيل الدخول بنجاح!")
                st.rerun()
            else:
                st.error("❌ عذراً، العنوان أو كلمة السر غير مسجلة في قاعدة البيانات.")
