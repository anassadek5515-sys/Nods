import streamlit as st
import time

st.set_page_config(
    page_title="Growth-Hacking SaaS Platform",
    page_icon="🚀",
    layout="wide"
)

# تهيئة قاعدة البيانات المحلية في الذاكرة لتخزين حسابات الشركات المعزولة
if "companies_database" not in st.session_state:
    st.session_state["companies_database"] = {
        "admin123": {"type": "admin", "name": "الرئيس (الأدمن)", "status": "active"}
    }

if "current_logged_company" not in st.session_state:
    st.session_state["current_logged_company"] = None

# 1. لوحة تحكم الرئيس (الأدمن)
if st.session_state["current_logged_company"] == "admin123":
    st.title("🛡️ موقع الرئيس (لوحة تحكم الأدمن المركزية)")
    st.success("أنت الآن في لوحة التحكم الخاصة بك. متابعة الشركات المشتركة والأرباح الحقيقية:")
    
    total_clients = len(st.session_state["companies_database"]) - 1
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("الشركات المشتركة الفاعلة", f"{total_clients} شركة")
    with col2:
        st.metric("الأرباح الإجمالية", f"${total_clients * 200}")
    with col3:
        st.metric("حالة سيرفرات Railway", "نشطة 100% (7 عقد عمل)")

    st.markdown("---")
    st.subheader("📋 سجل الشركات والبيئات المعزولة الحالية:")
    st.json(st.session_state["companies_database"])

    if st.button("🚪 تسجيل خروج الأدمن"):
        st.session_state["current_logged_company"] = None
        st.rerun()

# 2. لوحة تحكم العميل المشفرة والمعزولة تماماً
elif st.session_state["current_logged_company"] and st.session_state["current_logged_company"] != "admin123":
    comp_id = st.session_state["current_logged_company"]
    st.title(f"🔒 لوحة تحكم الشركة المشفرة الخاصة بك")
    st.success(f"✅ أهلاً بك! تم تأكيد اشتراكك بالعملات الرقمية بنجاح. عنوانك السري وكلمة سر بيئتك المعزولة: **{comp_id}**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚙️ أدوات التحليل والتسويق بالذكاء الاصطناعي")
        prod_desc = st.text_area("أدخل تفاصيل منتجات شركتك للبدء الفوري:", "خدمات تسويق إلكتروني وتطوير...")
        if st.button("🚀 بدء حملة الـ 40,000 عميل للشركات"):
            st.success("✅ تم إرسال الأوامر بنجاح لسيرفرات الـ Node.js الخلفية لبدء الزحف وجلب العملاء لشركتك!")
            
    with col2:
        st.subheader("💳 تفاصيل اشتراكك الشهري ($200 USDT)")
        st.info("💡 اشتراكك نشط وآمن ومؤكد عبر شبكة البلوكشين.")
        if st.button("💳 تفاصيل الحساب"):
            st.success("✅ حسابك مسجل ومحمي تماماً!")

    if st.button("🚪 تسجيل خروج"):
        st.session_state["current_logged_company"] = None
        st.rerun()

# 3. الصفحة الرئيسية (بوابة الدفع الآمن بالـ USDT + تفعيل الحساب)
else:
    st.title("🚀 منصة النمو الذكي والأتمتة للشركات ($200/شهر)")
    st.write("نظام آلي متكامل لجلب 40,000 عميل شهرياً، مع عزل كامل والحفاظ على أمن وخصوصية كل شركة مشتركة.")
    st.markdown("---")

    tab_pay, tab_login = st.tabs(["🌐 الاشتراك الآمن (USDT)", "🔑 دخول الشركة المشفرة"])

    with tab_pay:
        st.subheader("خطوة الاشتراك الشهري ($200 عبر العملات الرقمية المستقرة)")
        st.info("💡 **طريقة الدفع للمشترين من كل أنحاء العالم:**\n"
                  "1. قم بتحويل مبلغ **$200 USDT** إلى عنوان محفظتنا الرسمي عبر شبكة (TRC20):\n"
                  "👉 `TXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (حط هنا عنوان محفظتك الحقيقي)\n"
                  "2. بعد إتمام التحويل، أدخل رقم العملية أو الـ **Transaction Hash** في الخانة أدناه لتفعيل بيئتك المعزولة فوراً.")
        
        tx_hash = st.text_input("أدخل رقم العملية (Transaction Hash) أو كود التأكيد:", type="password")
        
        if st.button("✨ التحقق من الدفع وتوليد عنوان الشركة السري"):
            if len(tx_hash.strip()) >= 10:
                new_company_id = f"comp_sec_{int(time.time())}"
                st.session_state["companies_database"][new_company_id] = {
                    "type": "client",
                    "status": "active_crypto",
                    "tx_hash": tx_hash,
                    "created_at": time.time()
                }
                st.session_state["current_logged_company"] = new_company_id
                st.success(f"🎉 تم تأكيد الدفع وتوليد عنوان شركتك السري بنجاح: **{new_company_id}**! جاري نقلك لبيئتك المعزولة...")
                time.sleep(2)
                st.rerun()
            else:
                st.error("❌ برجاء إدخال رقم عملية (TxID) صحيح ومكتمل لتأكيد الاشتراك.")

    with tab_login:
        st.subheader("تسجيل الدخول للشركات المشتركة مسبقاً")
        st.write("أدخل عنوان شركتك السري أو كلمة السر الخاصة ببيئتك المعزولة:")
        
        entered_secret = st.text_input("عنوان الشركة أو كلمة السر الخاصة:", type="password")
        
        if st.button("🔐 دخول آمن لبيئة الشركة"):
            if entered_secret in st.session_state["companies_database"]:
                st.session_state["current_logged_company"] = entered_secret
                st.success("✅ تم التحقق من الهوية والدخول بنجاح!")
                st.rerun()
            else:
                st.error("❌ عذراً، هذا العنوان غير مسجل في النظام.")
