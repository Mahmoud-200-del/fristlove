# app.py - تطبيق ويب باستخدام Streamlit
import streamlit as st
import datetime
import random
import json
import pandas as pd
import plotly.express as px

# إعداد الصفحة
st.set_page_config(
    page_title="💖 قلبان متصلان 2026",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS مخصص
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B8B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .love-card {
        background: linear-gradient(135deg, #FFE4EC, #FFF5F7);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .heart-beat {
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# التطبيق الرئيسي
def main():
    # الشريط الجانبي
    with st.sidebar:
        st.title("⚙️ الإعدادات")
        
        # إدخال الأسماء
        st.subheader("👫 معلومات الشركاء")
        col1, col2 = st.columns(2)
        
        with col1:
            partner1 = st.text_input("الشريك الأول", "أحمد")
        with col2:
            partner2 = st.text_input("الشريك الثاني", "سارة")
        
        st.divider()
        
        # تاريخ البدء
        start_date = st.date_input("تاريخ بدء العلاقة", datetime.date(2023, 1, 1))
        
        # لغات الحب
        st.subheader("💬 لغات الحب")
        love_languages = st.multiselect(
            "اختر لغات الحب المفضلة",
            ["كلمات التأكيد", "الوقت الجودة", "الهدايا", "خدمات التقديم", "اللمسة الجسدية"],
            default=["كلمات التأكيد", "الوقت الجودة"]
        )
    
    # المحتوى الرئيسي
    st.markdown(f'<h1 class="main-header">💖 {partner1} & {partner2}</h1>', unsafe_allow_html=True)
    
    # علامات التبويب
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 الرئيسية", "💌 رسائل", "📅 ذكريات", "📊 إحصائيات", "🎯 تحديات"])
    
    with tab1:
        # بطاقة الترحيب
        col1, col2, col3 = st.columns([1,2,1])
        
        with col2:
            st.markdown(f"""
            <div class="love-card">
                <h2 style="text-align: center;">✨ مرحباً بكم في رحلتكم الرومانسية! ✨</h2>
                <p style="text-align: center; font-size: 1.2rem;">
                اليوم هو يوم جميل لمشاركة المزيد من الحب والمشاعر الجميلة ❤️
                </p>
                <div style="text-align: center; font-size: 3rem;" class="heart-beat">
                    💖
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # الإحصاءات السريعة
        st.subheader("📈 لمحة سريعة عن علاقتكما")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            days_together = (datetime.date.today() - start_date).days
            st.metric("🎉 أيام معاً", f"{days_together:,}")
        
        with col2:
            st.metric("💞 مستوى التوافق", f"{random.randint(85, 99)}%")
        
        with col3:
            st.metric("📝 الذكريات", f"{random.randint(10, 50)}")
        
        with col4:
            st.metric("✨ نقاط الحب", f"{random.randint(500, 2000)}")
        
        # مولد رسائل الحب
        st.subheader("✍️ مولد رسائل الحب")
        
        col1, col2 = st.columns(2)
        
        with col1:
            letter_type = st.selectbox(
                "نوع الرسالة",
                ["رومانسية", "مرحة", "حنين", "شكر", "مفاجئة"]
            )
            
            if st.button("🎲 إنشاء رسالة", type="primary"):
                messages = {
                    "رومانسية": [
                        f"عزيزي/عزيزتي {partner2}،\n\nقلبي ينبض باسمك في كل لحظة...",
                        f"يا حبيبي/حبيبتي {partner1}،\n\nعيونك هي نجومي في كل ليلة..."
                    ],
                    "مرحة": [
                        f"يا {partner2}،\n\nإذا كنت لعبة، لكنت المفضلة دائماً! 😄",
                        f"مرحباً {partner1}،\n\nأعلن أنك الفائز بجائزة 'أفضل شخص'! 🏆"
                    ]
                }
                
                letter = random.choice(messages.get(letter_type, ["أفكر فيك اليوم ❤️"]))
                st.session_state.generated_letter = letter
        
        with col2:
            if 'generated_letter' in st.session_state:
                st.text_area("📜 الرسالة", st.session_state.generated_letter, height=150)
                
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button("💾 حفظ الرسالة"):
                        st.success("تم حفظ الرسالة!")
                with col_btn2:
                    if st.button("📤 مشاركة"):
                        st.info("ميزة المشاركة قيد التطوير")
    
    with tab2:
        st.subheader("💌 رسائلكم المحفوظة")
        
        # عرض الرسائل المحفوظة
        sample_letters = [
            {"date": "2026-01-15", "from": partner1, "to": partner2, "content": "رسالة حب رومانسية...", "type": "💖"},
            {"date": "2026-01-10", "from": partner2, "to": partner1, "content": "رسالة شكر وتقدير...", "type": "🙏"},
            {"date": "2026-01-05", "from": partner1, "to": partner2, "content": "رسالة مفاجئة...", "type": "🎁"}
        ]
        
        for letter in sample_letters:
            with st.expander(f"{letter['type']} {letter['date']}: من {letter['from']} إلى {letter['to']}"):
                st.write(letter['content'])
                st.caption(f"النوع: {letter['type']}")
        
        # نموذج إرسال رسالة جديدة
        st.divider()
        st.subheader("📤 إرسال رسالة جديدة")
        
        with st.form("new_message"):
            col1, col2 = st.columns(2)
            with col1:
                receiver = st.selectbox("المستلم", [partner1, partner2])
            with col2:
                message_type = st.selectbox("النوع", ["💖 رومانسية", "😄 مرحة", "🎯 تحفيزية", "🎁 مفاجئة"])
            
            message_content = st.text_area("محتوى الرسالة", height=100)
            
            if st.form_submit_button("إرسال الرسالة ✨"):
                st.success("تم إرسال الرسالة بنجاح! 💝")
    
    with tab3:
        st.subheader("📅 خط زمني للذكريات")
        
        # إنشاء بيانات نموذجية للرسم البياني
        dates = pd.date_range(start=start_date, end=datetime.date.today(), freq='M')
        memories_data = pd.DataFrame({
            'date': dates,
            'memories': [random.randint(1, 5) for _ in range(len(dates))],
            'emotion': [random.choice(['سعادة', 'رومانسية', 'فرح', 'هدوء']) for _ in range(len(dates))]
        })
        
        # رسم بياني
        fig = px.line(memories_data, x='date', y='memories', 
                     title='📊 تطور الذكريات مع الوقت',
                     labels={'date': 'التاريخ', 'memories': 'عدد الذكريات'})
        st.plotly_chart(fig, use_container_width=True)
        
        # إضافة ذكرى جديدة
        st.subheader("➕ إضافة ذكرى جديدة")
        
        col1, col2 = st.columns(2)
        
        with col1:
            memory_date = st.date_input("تاريخ الذكرى", datetime.date.today())
            memory_location = st.text_input("المكان")
        
        with col2:
            memory_title = st.text_input("عنوان الذكرى")
            memory_emotion = st.select_slider(
                "مستوى المشاعر",
                options=["😊", "😍", "🥰", "🤗", "😭", "🥺"],
                value="🥰"
            )
        
        memory_description = st.text_area("وصف الذكرى")
        
        if st.button("💾 حفظ الذكرى", type="primary"):
            st.success(f"تم حفظ ذكرى '{memory_title}' بنجاح!")
    
    with tab4:
        st.subheader("📊 إحصائيات مفصلة")
        
        # بيانات التوافق
        compatibility_data = pd.DataFrame({
            'الجانب': ['التواصل', 'الاحترام', 'المشاعر', 'الاهتمامات', 'الأهداف'],
            'النسبة': [random.randint(70, 100) for _ in range(5)]
        })
        
        fig_compat = px.bar(compatibility_data, x='الجانب', y='النسبة',
                           title='📈 تحليل جوانب العلاقة',
                           color='النسبة',
                           color_continuous_scale='RdPu')
        st.plotly_chart(fig_compat, use_container_width=True)
        
        # مخطط دائري للعواطف
        emotions_data = pd.DataFrame({
            'العاطفة': ['سعادة', 'رومانسية', 'فرح', 'هدوء', 'حماس'],
            'التكرار': [random.randint(10, 30) for _ in range(5)]
        })
        
        fig_emotions = px.pie(emotions_data, values='التكرار', names='العاطفة',
                             title='💖 توزيع المشاعر في العلاقة',
                             hole=0.4)
        st.plotly_chart(fig_emotions, use_container_width=True)
    
    with tab5:
        st.subheader("🎯 تحديات الحب اليومية")
        
        # التحدي اليومي
        daily_challenge = random.choice([
            "📖 اقرأا قصة رومانسية معاً",
            "🎵 استمعا لأغنية تحبانها وتحدثا عن الذكريات",
            "🍳 اطبخا وجبة معاً",
            "📸 التقطا صورة رومانسية",
            "💌 اكتبا رسالة حب لبعضكما"
        ])
        
        st.info(f"### تحدي اليوم:\n\n**{daily_challenge}**\n\n🎁 المكافأة: {random.randint(10, 50)} نقطة حب!")
        
        if st.button("✅ أكملت التحدي!"):
            st.balloons()
            st.success(f"🎉 مبروك! لقد ربحت {random.randint(10, 50)} نقطة حب!")
        
        st.divider()
        
        # قائمة التحديات
        st.subheader("📋 تحديات أخرى يمكنكم تجربتها")
        
        challenges = [
            {"challenge": "خططا لحلم مشترك", "points": 50, "time": "أسبوع"},
            {"challenge": "سافرا إلى مكان جديد", "points": 100, "time": "شهر"},
            {"challenge": "تعلما شيئاً جديداً معاً", "points": 75, "time": "أسبوعين"},
            {"challenge": "أنشئا تقليدا عائلياً", "points": 60, "time": "شهر"}
        ]
        
        for i, challenge in enumerate(challenges):
            col1, col2, col3 = st.columns([3,1,1])
            with col1:
                st.write(f"**{i+1}. {challenge['challenge']}**")
            with col2:
                st.metric("النقاط", challenge['points'])
            with col3:
                if st.button("بدء", key=f"start_{i}"):
                    st.success(f"بدأت تحدي: {challenge['challenge']}")

# تشغيل التطبيق
if __name__ == "__main__":
    main()