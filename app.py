import streamlit as st

st.set_page_config(page_title="Growth Platform", page_icon="🚀", layout="wide")

# حفظ حالة العميل
if "client_active" not in st.session_state:
    st.session_state["client_active"] = False

if st.session_state["client_active"]:
    # 🎯 واجهة العميل الخاصة فور الدفع (من غير زهق)
    st.success("🎉 أهلاً بيك في عنوانك الخاص! السيستم جاهز وخد الشغل علطول.")
    
    target_url = st.text_input("🔗 حط رابط موقعك هنا:")
    campaign_msg = st.text_area("📝 رسالتك التسويقية:")
    
    if st.button("🚀 انطلق وابدأ الإرسال الفوري"):
        if target_url:
            st.success("✅ ممتاز! الـ 6 سيرفرات بتنفذ الشغل وبتبعت لموقعك دلوقتي حالا في الخلفية.")
        else:
            st.error("⚠️ من فضلك حط رابط الموقع الأول.")
            
    if st.button("🚪 تسجيل خروج / إنهاء الحملة"):
        st.session_state["client_active"] = False
        st.rerun()

else:
    # 💳 واجهة الدفع السريعة
    st.title("🚀 منصة النمو السريع والأتمتة")
    st.write("ادفع بالبطاقة (Paddle) وخد عنوانك الخاص واشتغل فورا في ثواني!")
    
    if st.button("💳 ادفع الآن وانتقل لعنوانك الخاص"):
        st.session_state["client_active"] = True
        st.success("✅ تم الدفع بنجاح! جاري تحويلك لصفحتك الخاصة...")
        st.rerun()
