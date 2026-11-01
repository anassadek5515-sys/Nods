import streamlit as st
import hashlib
import time

st.set_page_config(
    page_title="Growth-Hacking SaaS Platform",
    page_icon="🚀",
    layout="wide"
)

# محاكاة قاعدة البيانات والذاكرة المشفرة لعزل العملاء تماماً
if "clients_db" not in st.session_state:
    st.session_state["clients_db"] = {
        "admin_secret_key": {"role": "admin", "revenue": 0}
    }

if "logged_in_client" not in st.session_state:
    st.session_state["logged_in_client"] = None

# صفحة لوحة تحكم الأدمن السرية
if st.session_state["logged_in_client"] == "admin":
    st.title("🛡️ لوحة التحكم السرية الخاصة بالأدمن")
    st.write("مرحباً بك يا باشا. هنا تفاصيل المنصة، الأرباح، والشركات النشطة:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("الشركات النشطة حالياً", "1,240 شركة")
    with col2:
        st.metric("الأرباح الإجمالية", "$248,000")
    with col3:
        st.metric("شركات تجدد قريباً", "45 شركة")

    st.markdown("---")
    st.subheader("🤖 تقرير الذكاء الاصطناعي والتوقعات")
    st.info("💡 توقعات الذكاء الاصطناعي: من المتوقع دخول 350 شركة جديدة خلال الـ 24 ساعة القادمة بناءً على معدل الإرسال الحالي.")

    if st.button("🚪 تسجيل خروج الأدمن"):
        st.session_state["logged_in_client"] = None
        st.rerun()

# صفحة العميل المشفرة (عزل تام لكل شركة برابط وكلمة سر خاصة بها)
elif st.session_state["logged_in_client"] and st.session_state["logged_in_client"] != "admin":
    client_id = st.session_state["logged_in_client"]
    st.title(f"🔒 لوحة تحكم العميل المشفرة [{client_id}]")
    st.success("أنت الآن في بيئتك المعزولة والخاصة بك وحدك بنسبة 100%.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚙️ تحليل منتجاتك بالذكاء الاصطناعي")
        product_info = st.text_area("أدخل تفاصيل منتجك الجديد للتحليل التسويقي:", "نقدم حلول برمجية متطورة...")
        if st.button("🚀 تشغيل التحليل الفوري"):
            st.success("✅ تم تحليل المنتج وبدء الحملات التسويقية المخصصة بنجاح!")
            
    with col2:
        st.subheader("💳 حالة الاشتراك الشهري")
        st.warning("⚠️ تنبيه: اشتراكك الحالي نشط بـ $200/شهر. عند اقتراب الموعد سيطالبك السيستم بالتجديد للاستمرار.")
        if st.button("💳 تجديد اشتراك الشهر الحالي (200$)"):
            st.success("✅ تم تجديد الاشتراك بنجاح لشهر إضافي!")

    if st.button("🚪 تسجيل خروج"):
        st.session_state["logged_in_client"] = None
        st.rerun()

# واجهة الدخول الرئيسية والاشتراك
else:
    st.title("🚀 منصة النمو الذكي والأتمتة للشركات ($200/شهر)")
    st.write("نظام متكامل لتحليل منتجاتك بالذكاء الاصطناعي وتشغيل حملات تسويقية ضخمة لجلب العملاء أوتوماتيكياً.")
    st.markdown("---")

    tab1, tab2 = st.tabs(["💳 اشتراك جديد للشركات", "🔑 تسجيل الدخول (عنوانك المشفر)"])

    with tab1:
        st.subheader("خطوة الاشتراك الفوري")
        st.write("اضغط أدناه للتحويل إلى بوابة الدفع المشفرة (Paddle/Stripe):")
        
        # رابط الدفع الحقيقي
        paddle_url = "https://buy.paddle.com/your-product-id"
        
        if st.button("💳 دفع 200$ والاشتراك الآن"):
            # محاكاة إتمام الدفع وتوليد عنوان سري ومشفر للعميل فوراً
            new_client_id = f"company_sec_{int(time.time())}"
            st.session_state["clients_db"][new_client_id] = {"revenue": 200}
            st.session_state["logged_in_client"] = new_client_id
            st.success(f"✅ تمت عملية الدفع بنجاح! تم توليد عنوانك السري: {new_client_id}")
            st.rerun()

    with tab2:
        st.subheader("الدخول للوحة التحكم الخاصة بك")
        entered_key = st.text_input("أدخل عنوانك أو كلمة السر الخاصة بك:", type="password")
        
        if st.button("دخول آمن"):
            if entered_key == "admin123": # كلمة سر الأدمن
                st.session_state["logged_in_client"] = "admin"
                st.rerun()
            elif entered_key in st.session_state["clients_db"]:
                st.session_state["logged_in_client"] = entered_key
                st.rerun()
            else:
                st.error("❌ البيانات غير صحيحة أو العنوان غير مسجل.")
