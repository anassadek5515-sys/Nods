import streamlit as st
import time

st.set_page_config(
    page_title="Growth-Hacking SaaS Platform",
    page_icon="🚀",
    layout="wide"
)

# 1. قاعدة البيانات المحلية للشركات والاشتراكات
if "companies_database" not in st.session_state:
    st.session_state["companies_database"] = {
        "admin123": {"type": "admin", "name": "الأدمن", "status": "active"}
    }

if "current_logged_company" not in st.session_state:
    st.session_state["current_logged_company"] = None

# 2. لوحة تحكم الأدمن
if st.session_state["current_logged_company"] == "admin123":
    st.title("🛡️ لوحة تحكم الأدمن")
    st.success("متابعة الشركات المشتركة وإدارتها:")
    
    total_clients = len(st.session_state["companies_database"]) - 1
    col1, col2 = st.columns(2)
    with col1:
        st.metric("الشركات المشتركة الفاعلة", f"{total_clients} شركة")
    with col2:
        st.metric("إجمالي الإيرادات", f"${total_clients * 200}")

    st.markdown("---")
    st.subheader("📋 سجل المعاملات والشركات:")
    st.json(st.session_state["companies_database"])

    if st.button("🚪 خروج الأدمن"):
        st.session_state["current_logged_company"] = None
        st.rerun()

# 3. لوحة تحكم العميل المشترك
elif st.session_state["current_logged_company"] and st.session_state["current_logged_company"] != "admin123":
    comp_id = st.session_state["current_logged_company"]
    st.title(f"🔒 لوحة تحكم شركتك المعزولة")
    st.success(f"✅ اشتراكك مفعل بنجاح! معرف شركتك السري: **{comp_id}**")
    
    st.info("مرحباً بك في بيئة الـ Growth Hacking الخاصة بشركتك. جميع أدواتك جاهزة للعمل.")
    
    if st.button("🚪 تسجيل خروج"):
        st.session_state["current_logged_company"] = None
        st.rerun()

# 4. الواجهة الرئيسية (بوابة الاشتراك والدفع)
else:
    st.title("🚀 منصة النمو الذكي للشركات ($200/شهر)")
    st.write("نظام آلي متكامل لجلب العملاء للشركات مع عزل تام لكل عميل.")
    st.markdown("---")

    tab_pay, tab_login = st.tabs(["💳 الاشتراك والدفع الفوري", "🔑 دخول الشركة"])

    with tab_pay:
        st.subheader("خطوات الدفع والتفعيل المباشر")
        
        # عنوان المحفظة الخاص بك اللي طلعته من التطبيق
        my_usdt_wallet = "0x9426A467E0fFF34981656bd98580f60CFE395364" 
        
        st.markdown(f"""
        <div style="background-color: #0f172a; padding: 20px; border-radius: 10px; border: 1px solid #1e293b; margin-bottom: 20px;">
            <h4 style="color: #38bdf8; margin-top: 0;">🌐 معلومات الدفع المباشر (USDT - BEP20):</h4>
            <p style="color: #e2e8f0;">1️⃣ قم بتحويل مبلغ <b>$200 (USDT)</b> إلى عنوان محفظتك التالي:</p>
            <div style="background: #1e293b; padding: 12px; border-radius: 6px; font-family: monospace; color: #10b981; font-size: 15px; text-align: center; margin: 10px 0; word-break: break-all;">
                {my_usdt_wallet}
            </div>
            <p style="color: #cbd5e1; margin-bottom: 0;">2️⃣ شبكة التحويل المطلوبة: <b>BNB Smart Chain (BEP20)</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        tx_hash = st.text_input("أدخل رقم المعاملة أو كود التحويل (TXID):")
        
        if st.button("✨ تفعيل الحساب فوراً"):
            if len(tx_hash.strip()) >= 5:
                new_company_id = f"comp_sec_{int(time.time())}"
                st.session_state["companies_database"][new_company_id] = {
                    "type": "client",
                    "status": "active",
                    "tx_hash": tx_hash,
                    "amount": 200,
                    "created_at": time.time()
                }
                st.session_state["current_logged_company"] = new_company_id
                st.success(f"🎉 تم تفعيل حسابك بنجاح! كود شركتك السري هو: **{new_company_id}**")
                time.sleep(2)
                st.rerun()
            else:
                st.error("❌ برجاء إدخال رقم المعاملة أو كود التحويل الصحيح.")

    with tab_login:
        st.subheader("تسجيل الدخول للشركات المسجلة")
        entered_secret = st.text_input("أدخل كود شركتك السري:", type="password")
        
        if st.button("🔐 دخول"):
            if entered_secret in st.session_state["companies_database"]:
                st.session_state["current_logged_company"] = entered_secret
                st.rerun()
            else:
                st.error("❌ عذراً، هذا الكود غير مسجل أو خطأ في البيانات.")
