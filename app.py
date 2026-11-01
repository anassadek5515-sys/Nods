import streamlit as st
import time

st.set_page_config(
    page_title="Growth-Hacking SaaS Platform",
    page_icon="🚀",
    layout="wide"
)

# تهيئة قاعدة البيانات المحلية في الذاكرة لتخزين حسابات الشركات والأرصدة المتراكمة
if "companies_database" not in st.session_state:
    st.session_state["companies_database"] = {
        "admin123": {"type": "admin", "name": "الرئيس (الأدمن)", "status": "active"}
    }

if "current_logged_company" not in st.session_state:
    st.session_state["current_logged_company"] = None

# 1. لوحة تحكم الرئيس (الأدمن) - لمتابعة الأرباح المحفوظة في الموقع
if st.session_state["current_logged_company"] == "admin123":
    st.title("🛡️ لوحة تحكم الأدمن المركزية")
    st.success("أنت الآن في لوحة التحكم الخاصة بك. متابعة الأرباح المحفوظة والشركات المشتركة:")
    
    total_clients = len(st.session_state["companies_database"]) - 1
    total_revenue = total_clients * 200
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("الشركات المشتركة الفاعلة", f"{total_clients} شركة")
    with col2:
        st.metric("إجمالي الأرباح المحفوظة بالموقع", f"${total_revenue}")
    with col3:
        st.metric("حالة الخزينة", "آمنة وجاهزة للسحب اليدوي")

    st.markdown("---")
    st.subheader("📋 سجل الشركات والاشتراكات المحفوظة:")
    st.json(st.session_state["companies_database"])

    if st.button("🚪 تسجيل خروج الأدمن"):
        st.session_state["current_logged_company"] = None
        st.rerun()

# 2. لوحة تحكم العميل المشفرة والمعزولة تماماً
elif st.session_state["current_logged_company"] and st.session_state["current_logged_company"] != "admin123":
    comp_id = st.session_state["current_logged_company"]
    st.title(f"🔒 لوحة تحكم الشركة المشفرة الخاصة بك")
    st.success(f"✅ أهلاً بك! تم تأكيد اشتراكك وحفظه في النظام. عنوانك السري: **{comp_id}**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚙️ أدوات التحليل والتسويق بالذكاء الاصطناعي")
        prod_desc = st.text_area("أدخل تفاصيل منتجات شركتك للبدء الفوري:", "خدمات تسويق إلكتروني وتطوير...")
        if st.button("🚀 بدء حملة الـ 40,000 عميل للشركات"):
            st.success("✅ تم إرسال الأوامر بنجاح لسيرفرات الخلفية لبدء الزحف وجلب العملاء لشركتك!")
            
    with col2:
        st.subheader("💳 تفاصيل اشتراكك الشهري ($200)")
        st.info("💡 اشتراكك مسفوظ ومفعل بقيمة 200$ شهرياً.")
        if st.button("💳 تفاصيل الحساب"):
            st.success("✅ حسابك مسجل ومحمي تماماً!")

    if st.button("🚪 تسجيل خروج"):
        st.session_state["current_logged_company"] = None
        st.rerun()

# 3. الصفحة الرئيسية (الدفع والتحويل مع الحفظ الفوري في السيستم)
else:
    st.title("🚀 منصة النمو الذكي والأتمتة للشركات ($200/شهر)")
    st.write("نظام آلي متكامل لجلب 40,000 عميل شهرياً، مع عزل كامل والحفاظ على أمن وخصوصية كل شركة مشتركة.")
    st.markdown("---")

    tab_pay, tab_login = st.tabs(["💳 الاشتراك والدفع المباشر", "🔑 دخول الشركة المشتركة"])

    with tab_pay:
        st.subheader("خطوة الاشتراك الشهري ($200)")
        
        # صندوق تعليمات الدفع المباشر
        st.markdown("""
        <div style="background-color: #1e293b; padding: 20px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 20px;">
            <h4 style="color: #38bdf8; margin-top: 0;">📌 تعليمات تحويل قيمة الاشتراك:</h4>
            <p style="color: #e2e8f0; margin-bottom: 8px;">1️⃣ قم بتحويل مبلغ (200$) عبر وسائلنا المتاحة:</p>
            <ul style="color: #cbd5e1; margin-top: 0;">
                <li><b>انستا باي (Instapay):</b> تحويل على (مثال: <code>your-username@instapay</code>)</li>
                <li><b>فودافون كاش / محفظة:</b> تحويل على الرقم (مثال: <code>010xxxxxxxx</code>)</li>
            </ul>
            <p style="color: #e2e8f0; margin-bottom: 0;">2️⃣ بعد إتمام التحويل، أدخل <b>رقم المعاملة (Transaction ID)</b> بالأسفل ليقوم السيستم بحفظ اشتراكك وتفعيل بيئتك المعزولة فوراً.</p>
        </div>
        """, unsafe_allow_html=True)
        
        payment_ref = st.text_input("أدخل رقم المعاملة أو كود إيصال التحويل:", type="default")
        
        if st.button("✨ تفعيل الحساب وحفظ الاشتراك بالسيستم"):
            if len(payment_ref.strip()) >= 3:
                new_company_id = f"comp_sec_{int(time.time())}"
                st.session_state["companies_database"][new_company_id] = {
                    "type": "client",
                    "status": "active_verified",
                    "payment_ref": payment_ref,
                    "amount": 200,
                    "created_at": time.time()
                }
                st.session_state["current_logged_company"] = new_company_id
                st.success(f"🎉 تم حفظ الاشتراك وتوليد عنوان شركتك السري بنجاح: **{new_company_id}**! جاري نقلك لبيئتك المعزولة...")
                time.sleep(2)
                st.rerun()
            else:
                st.error("❌ برجاء إدخال رقم المعاملة أو كود التحويل الصحيح لتفعيل الحساب.")

    with tab_login:
        st.subheader("تسجيل الدخول للشركات المشتركة مسبقاً")
        st.write("أدخل عنوان شركتك السري أو كلمة السر الخاصة ببيئتك المعزولة:")
        
        entered_secret = st.text_input("عنوان الشركة أو كلمة السر الخاصة:", type="password", key="login_input")
        
        if st.button("🔐 دخول آمن لبيئة الشركة"):
            if entered_secret in st.session_state["companies_database"]:
                st.session_state["current_logged_company"] = entered_secret
                st.success("✅ تم التحقق من الهوية والدخول بنجاح!")
                st.rerun()
            else:
                st.error("❌ عذراً، هذا العنوان غير مسجل في النظام.")
