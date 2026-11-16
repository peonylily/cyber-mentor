import streamlit as st
import pandas as pd
from model import train_and_evaluate, predict_topic

st.set_page_config(
    page_title="Cyber Mentor | المرشد السيبراني",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { direction: rtl; text-align: right; font-family: 'IBM Plex Sans Arabic', sans-serif; }
.stApp { background: radial-gradient(circle at 85% 0%, #123b3b 0%, #07151d 38%, #061018 100%); color: #e8f1f2; }
section[data-testid="stSidebar"] { background: #081820; border-left: 1px solid #1b4447; }
section[data-testid="stSidebar"] * { color: #dce9e9; }
.block-container { padding-top: 2rem; max-width: 1250px; }
h1, h2, h3 { color: #effafa !important; }
p, label, .stMarkdown { color: #c5d6d8; }
div[data-testid="stMetric"] { background: linear-gradient(145deg,#102b32,#0b2029); border: 1px solid #1b5050; padding: 16px; border-radius: 14px; }
div[data-testid="stMetricLabel"] { color: #9bb9b9; }
div[data-testid="stMetricValue"] { color: #76e0b0; }
div.stButton > button { background: linear-gradient(90deg,#0e8c72,#1caa85); color: white; border: 0; border-radius: 10px; padding: .65rem 1.2rem; font-weight: 700; }
div.stButton > button:hover { background: #27bd94; color: #061018; border: 0; }
.panel { background: rgba(13,38,47,.88); border: 1px solid #1b4c50; border-radius: 16px; padding: 20px 22px; margin: 10px 0 16px; }
.eyebrow { color: #66d8ae; letter-spacing: 1px; font-size: .82rem; font-weight: 700; }
.hero-title { font-size: 2.2rem; font-weight: 700; color: #f1ffff; margin: 4px 0 8px; }
.hero-sub { color: #b5cbcd; font-size: 1.02rem; line-height: 1.9; }
.tag { display:inline-block; border:1px solid #2b7167; color:#8be7bf; background:#0d302d; border-radius:30px; padding:5px 12px; margin:3px; font-size:.82rem; }
.small-muted { color:#8ba7aa; font-size:.88rem; }
hr { border-color: #1b4148; }
[data-testid="stProgressBar"] > div > div { background-color: #4bd2a0; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return train_and_evaluate()

model, metrics = load_model()

with st.sidebar:
    st.markdown("## 🛡️ CYBER MENTOR")
    st.caption("منصة الإرشاد والتعلّم السيبراني")
    st.markdown("---")
    page = st.radio(
        "لوحة التنقل",
        ["الرئيسية", "تقييم المتعلم", "مركز التعلم", "عن المشروع"],
        label_visibility="visible"
    )
    st.markdown("---")
    st.markdown('<span class="tag">نموذج تعليمي</span><span class="tag">بيانات اصطناعية</span>', unsafe_allow_html=True)
    st.caption("الإصدار الأولي · 2026")

def header(kicker, title, subtitle):
    st.markdown(f"""
    <div class="panel">
      <div class="eyebrow">{kicker}</div>
      <div class="hero-title">{title}</div>
      <div class="hero-sub">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

if page == "الرئيسية":
    header("SECURITY LEARNING ENVIRONMENT / 01",
           "مرحبًا بك في Cyber Mentor",
           "مساحة تعليمية تساعدك على اكتشاف مهاراتك الرقمية، وتحديد الموضوع الذي يحتاج إلى مزيد من التدريب، ثم الانتقال إلى محتوى تعليمي مناسب.")
    c1, c2, c3 = st.columns(3)
    c1.metric("موضوعات التعلّم", "03", "مسارات أساسية")
    c2.metric("سجلات البيانات التجريبية", f"{metrics['total_size']}", "بيانات اصطناعية")
    c3.metric("دقة النموذج التجريبية", f"{metrics['accuracy']*100:.1f}%", "على مجموعة الاختبار")
    st.markdown("### مسارات التعلّم")
    cols = st.columns(3)
    cards = [
        ("01", "التصيد الإلكتروني", "التعرّف على الرسائل والروابط المشبوهة ومؤشرات الخداع."),
        ("02", "حماية الخصوصية", "فهم البيانات الشخصية وأذونات التطبيقات والمشاركة الآمنة."),
        ("03", "كلمات المرور", "التعرّف على خصائص كلمات المرور القوية والتحقق متعدد العوامل.")
    ]
    for col, (num, title, desc) in zip(cols, cards):
        with col:
            st.markdown(f'<div class="panel"><div class="eyebrow">LEARNING PATH {num}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
    st.markdown("### كيف تعمل المنصة؟")
    st.markdown("""
    <div class="panel">
      <span class="tag">01 · قيّم</span>
      <span class="tag">02 · حلّل</span>
      <span class="tag">03 · تعلّم</span>
      <p>أدخل نتائجك التعليمية في صفحة التقييم، ثم يحلل نموذج شجرة القرار الدرجات ويقترح مسارًا للتدريب. بعد ذلك يمكنك فتح مركز التعلم للاطلاع على إرشادات الموضوع المقترح.</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("هذه نسخة تعليمية تجريبية. لا تراقب الأجهزة أو الشبكات، ولا تنفّذ فحصًا أمنيًا حقيقيًا.")

elif page == "تقييم المتعلم":
    header("LEARNER ASSESSMENT / 02",
           "تقييم المهارات السيبرانية",
           "أدخل درجاتك في الأنشطة التعليمية. سيستخدم النظام نموذج تعلم آلة لتقدير الموضوع الأنسب للتدريب.")
    st.markdown('<div class="panel">الدرجات من 0 إلى 100. استخدم نتائج تدريبية أو افتراضية فقط، ولا تدخل أي بيانات شخصية.</div>', unsafe_allow_html=True)
    with st.form("assessment_form"):
        a, b = st.columns(2)
        with a:
            phishing = st.slider("التصيد الإلكتروني", 0, 100, 70, 5)
            privacy = st.slider("حماية الخصوصية", 0, 100, 65, 5)
        with b:
            passwords = st.slider("كلمات المرور", 0, 100, 75, 5)
            errors = st.slider("عدد الإجابات غير الصحيحة", 0, 10, 3, 1)
        submitted = st.form_submit_button("تحليل النتائج")
    if submitted:
        topic, confidence = predict_topic(model, phishing, privacy, passwords, errors)
        st.markdown("### نتيجة التحليل")
        st.success(f"المسار المقترح للتدريب: **{topic}**")
        st.metric("درجة ثقة النموذج", f"{confidence*100:.1f}%")
        st.caption("درجة الثقة تعبّر عن احتمالات النموذج بين الفئات، ولا تعني ضمان صحة التوصية.")
        score_df = pd.DataFrame({
            "المهارة": ["التصيد الإلكتروني", "حماية الخصوصية", "كلمات المرور"],
            "الدرجة": [phishing, privacy, passwords]
        }).set_index("المهارة")
        st.markdown("#### ملخص الدرجات")
        st.bar_chart(score_df)
        st.session_state["recommended_topic"] = topic
        st.markdown("يمكنك الآن الانتقال إلى **مركز التعلم** لعرض إرشادات المسار المقترح.")

elif page == "مركز التعلم":
    header("LEARNING CENTER / 03",
           "مركز التعلم",
           "محتوى توعوي مختصر يساعدك على بناء عادات رقمية أكثر أمانًا.")
    default_topic = st.session_state.get("recommended_topic", "التصيد الإلكتروني")
    topic = st.selectbox("اختر موضوعًا للتعلّم", ["التصيد الإلكتروني", "حماية الخصوصية", "كلمات المرور"],
                         index=["التصيد الإلكتروني", "حماية الخصوصية", "كلمات المرور"].index(default_topic))
    content = {
        "التصيد الإلكتروني": [
            "تحقق من عنوان المرسل قبل التفاعل مع الرسالة.",
            "لا تضغط على رابط لمجرد أن الرسالة تبدو عاجلة أو مغرية.",
            "افتح الموقع بكتابة عنوانه المعروف بدل استخدام رابط غير متوقع.",
            "استشر شخصًا موثوقًا أو جهة مختصة عند الشك."
        ],
        "حماية الخصوصية": [
            "راجع أذونات التطبيقات، واسمح فقط بما تحتاجه الوظيفة.",
            "تجنب نشر معلوماتك الشخصية أو موقعك أو تفاصيل حساباتك.",
            "استخدم إعدادات الخصوصية المناسبة في الخدمات التي تستخدمها.",
            "لا ترفع معلومات سرية أو ملفات شخصية إلى أدوات عامة."
        ],
        "كلمات المرور": [
            "استخدم كلمة مرور طويلة وفريدة لكل حساب مهم.",
            "لا تشارك كلمات المرور مع الآخرين.",
            "فعّل التحقق متعدد العوامل عندما يكون متاحًا.",
            "استخدم مدير كلمات مرور موثوقًا بمساعدة ولي الأمر عند الحاجة."
        ]
    }
    st.markdown(f'<div class="panel"><div class="eyebrow">RECOMMENDED LEARNING PATH</div><h2>{topic}</h2></div>', unsafe_allow_html=True)
    for i, item in enumerate(content[topic], 1):
        st.markdown(f'<div class="panel"><span class="eyebrow">TIP 0{i}</span><p>{item}</p></div>', unsafe_allow_html=True)
    st.warning("المحتوى للتوعية والتعليم، ولا يُعد بديلًا عن إرشادات المدرسة أو الجهات المختصة.")

else:
    header("PROJECT OVERVIEW / 04",
           "عن Cyber Mentor",
           "مشروع تعليمي يوظف تعلم الآلة لتخصيص مسار تعلّم مبسط في موضوعات الأمن السيبراني.")
    st.markdown("""
    <div class="panel">
      <h3>فكرة المشروع</h3>
      <p>تستقبل المنصة درجات المتعلم في ثلاثة موضوعات، ثم تستخدم نموذج شجرة قرار مدرّبًا على بيانات اصطناعية لتوقع الموضوع الذي يحتاج إلى تدريب إضافي.</p>
    </div>
    <div class="panel">
      <h3>كيف استُخدم الذكاء الاصطناعي؟</h3>
      <p>يُستخدم مصنّف Decision Tree من مكتبة Scikit-learn. تُقسّم البيانات إلى تدريب واختبار، ثم تُعرض مقاييس التقييم مثل Accuracy وPrecision وRecall.</p>
    </div>
    <div class="panel">
      <h3>حدود النسخة التجريبية</h3>
      <ul>
        <li>مجموعة البيانات اصطناعية وليست نتائج طلاب حقيقيين.</li>
        <li>التقييم يقيس أداء النموذج على بيانات تجريبية من المجموعة نفسها.</li>
        <li>لا تجمع المنصة أسماء أو كلمات مرور أو معلومات شخصية.</li>
        <li>التوصية تعليمية وليست تشخيصًا أو حكمًا على مستوى الأمان الفعلي.</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### مؤشرات تقييم النموذج")
    m1, m2, m3 = st.columns(3)
    m1.metric("Accuracy", f"{metrics['accuracy']*100:.1f}%")
    m2.metric("Precision", f"{metrics['precision']*100:.1f}%")
    m3.metric("Recall", f"{metrics['recall']*100:.1f}%")
    st.caption(f"التدريب: {metrics['train_size']} سجل · الاختبار: {metrics['test_size']} سجل · البيانات كلها اصطناعية.")
    cm = pd.DataFrame(metrics["confusion_matrix"], index=metrics["labels"], columns=metrics["labels"])
    st.markdown("#### مصفوفة الالتباس")
    st.dataframe(cm, use_container_width=True)

st.markdown("---")
st.markdown('<p class="small-muted">CYBER MENTOR · مشروع تعليمي تجريبي · لا يتصل بأنظمة أو شبكات خارجية</p>', unsafe_allow_html=True)
