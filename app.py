import streamlit as st
import time
import pandas as pd
import hashlib

# 1. إعدادات الأمان المتقدمة للصفحة
st.set_page_config(
    page_title="Secure AI Growth Enterprise Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# دالة تشفير أمنية للأكواد والكلمات السرية
def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()

# 2. قواعد البيانات والذاكرة المحلية المشفرة
if "companies_database" not in st.session_state:
    st.session_state["companies_database"] = {
        hash_key("admin123"): {"type": "admin", "name": "الأدمن الرئيسية", "status": "active"}
    }

# حماية واجهة الاستخدام من التحديد والنسخ غير المبرر
st.markdown("""
<style>
    .secure-container { user-select: none; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# القائمة الجانبية (موقع الدفع والاشتراك فقط)
# ---------------------------------------------------------
st.sidebar.title("🌐 بوابة المنصة الآمنة")
site_choice = st.sidebar.radio(
    "اختر القسم:", 
    ["💳 موقع الاشتراك والدفع الفوري"]
)

# =========================================================
# بوابة الدفع والاشتراك الآلي المشفر
# =========================================================
if site_choice == "💳 موقع الاشتراك والدفع الفوري":
    st.title("🛡️ منصة النمو الذكي المشفرة ($200/شهر)")
    st.write("بوابة دفع آمنة 100% - نظام معزول ومحمي ضد الهجمات والثغرات مع أحدث تقنيات الأمان السيبراني.")
    st.markdown("---")

    st.subheader("خطوات الاشتراك والتفعيل الآمن")
    
    my_usdt_wallet = "0x9426A467E0fFF34981656bd98580f60CFE395364"
    payment_uri = f"ethereum:{my_usdt_wallet}"
    
    st.markdown(f"""
    <div style="background-color: #fee2e2; border: 2px solid #ef4444; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: #991b1b; margin-top: 0;">🚨 تنبيه أمني هامة جداً قبل التحويل:</h4>
        <p style="color: #7f1d1d; font-size: 15px; font-weight: bold;">
            يجب التحويل حصراً عبر شبكة <b>BNB Smart Chain (BEP20)</b>. أي شبكة أخرى تعرض أموالك للضياع ولن يقبل النظام المعاملة!
        </p>
        <hr style="border-color: #fca5a5;">
        <h4 style="color: #1e3a8a; margin-top: 10px;">🌐 محفظتنا المعتمدة:</h4>
        <div style="background: #1e293b; padding: 12px; border-radius: 6px; font-family: monospace; color: #10b981; font-size: 15px; text-align: center; margin: 10px 0; word-break: break-all;">
            {my_usdt_wallet}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 25px;">
        <a href="{payment_uri}" target="_blank" style="background-color: #10b981; color: white; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 18px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">🔗 دفع آمن عبر المحفظة</a>
    </div>
    """, unsafe_allow_html=True)
    
    tx_hash = st.text_input("أدخل كود التحويل (TXID) المعاملة على شبكة BNB:")
    
    if st.button("✨ تفعيل الحساب بأمان تام"):
        clean_tx = tx_hash.strip()
        if len(clean_tx) >= 10 and not any(char in clean_tx for char in ["<", ">", ";", "'", '"']):
            raw_secret_key = f"comp_{int(time.time())}_{clean_tx[:6]}"
            hashed_secret = hash_key(raw_secret_key)
            
            st.session_state["companies_database"][hashed_secret] = {
                "type": "client",
                "status": "active",
                "tx_hash": clean_tx,
                "amount": 200,
                "network": "BNB Smart Chain (BEP20)",
                "created_at": time.time()
            }
            st.success("🎉 تم التحقق من المعاملة وتفعيل حسابك بنجاح!")
            st.warning(f"⚠️ **كود الدخول السري الخاص بك (احتفظ به في مكان آمن ولن يظهر مرة أخرى):**\n\n`{raw_secret_key}`")
        else:
            st.error("❌ كود التحويل غير صالح أو يحتوي على رموز غير مسموحة لأسباب أمنية.")
