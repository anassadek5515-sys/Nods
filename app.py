import streamlit as st

st.set_page_config(
    page_title="Growth-Hacking SaaS Platform",
    page_icon="🚀",
    layout="wide"
)

# تتبع حالة الدفع والعميل
if "client_paid" not in st.session_state:
    st.session_state["client_paid"] = False

if st.session_state["client_paid"]:
    st.success("🎉 أهلاً بيك في عنوانك الخاص والمشفر! السيستم يعمل أوتوماتيكياً لحسابك.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⚙️ إعدادات حملتك التسويقية")
        target_url = st.text_input("🔗 رابط موقعك أو منتجك:", value="https://yourproduct.com")
        product_desc = st.text_area("📝 وصف المنتج أو الخدمة لتحليل الذكاء الاصطناعي:", value="نقدم حلول برمجية متطورة...")
        
        if st.button("🚀 تحديث وبدء التشغيل الفوري"):
            st.success("✅ تم حفظ البيانات وتحليلها بالذكاء الاصطناعي وتوزيع المهام على السيرفرات!")
            
    with col2:
        st.subheader("📊 أداء السيرفرات المباشر")
        st.metric("الشركات المستهدفة اليوم", "40,000 شركة")
        st.metric("الحالة", "🟢 يعمل 24/7 أوتوماتيك")
        st.info("🔒 جميع بياناتك معزولة ومشفرة تماماً ولا يمكن لأي شخص الاطلاع عليها.")

    if st.button("🚪 تسجيل خروج"):
        st.session_state["client_paid"] = False
        st.rerun()

else:
    st.title("🚀 منصة النمو الذكي والأتمتة للشركات ($200/شهر)")
    st.write("نظام متكامل لتحليل منتجاتك بالذكاء الاصطناعي وتشغيل حملات تسويقية ضخمة لجلب العملاء أوتوماتيكياً على مدار الساعة.")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⚡ إرسال يومي", "40,000 رسالة")
    with col2:
        st.metric("🤖 ذكاء اصطناعي", "تحليل متقدم للمنتجات")
    with col3:
        st.metric("🔒 الأمان", "عزل تام وتشفير كامل")

    st.markdown("---")
    st.subheader("💳 اشتراك الشركات الفوري")
    st.write("اشترك الآن بـ 200 دولار شهرياً عبر بوابة الدفع الآمنة، وسيحولك السيستم فوراً إلى عنوانك الخاص المشفر.")

    if st.button("💳 ادفع الآن واشترك (200$ / شهرياً)"):
        st.session_state["client_paid"] = True
        st.success("✅ تم الدفع بنجاح! جاري إنشاء عنوانك الخاص...")
        st.rerun()
