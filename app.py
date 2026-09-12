"""Version 0.2 of the Artificial Intelligence teaching laboratory."""

import streamlit as st


UNITS = [
    ("ความรู้เบื้องต้นเกี่ยวกับปัญญาประดิษฐ์ (Introduction to AI)",
     "อธิบายแนวคิดพื้นฐานของปัญญาประดิษฐ์ และยกตัวอย่างการประยุกต์ใช้ AI ในชีวิตประจำวันได้"),
    ("อัลกอริทึมการค้นหา BFS / DFS",
     "อธิบายและเปรียบเทียบลำดับการสำรวจโหนดด้วย BFS และ DFS บนกราฟอย่างง่ายได้"),
    ("การค้นหาเส้นทางด้วย A* (A* Path Finding)",
     "อธิบายการใช้ต้นทุนเส้นทางและค่าฮิวริสติก (Heuristic) เพื่อค้นหาเส้นทางด้วย A* ได้"),
    ("ระบบผู้เชี่ยวชาญแบบใช้กฎ (Rule-Based Expert System)",
     "สร้างกฎ IF–THEN อย่างง่าย และอธิบายการอนุมานคำตอบจากข้อเท็จจริงและกฎได้"),
    ("พื้นฐานการเรียนรู้ของเครื่อง (Machine Learning Basics)",
     "แยกแยะการเรียนรู้แบบมีผู้สอนและไม่มีผู้สอน และอธิบายบทบาทของข้อมูลฝึกและข้อมูลทดสอบได้"),
    ("การถดถอยเชิงเส้น (Linear Regression)",
     "อธิบายความสัมพันธ์เชิงเส้นระหว่างตัวแปร และตีความความชัน จุดตัดแกน และความคลาดเคลื่อนในการพยากรณ์ได้"),
    ("การจำแนกประเภทข้อมูล (Classification)",
     "อธิบายการทำนายกลุ่มของข้อมูล และประเมินผลการจำแนกด้วยความแม่นยำและตารางความสับสน (Confusion Matrix) ได้"),
    ("โครงข่ายประสาทเทียมและฟังก์ชันกระตุ้น (Neural Networks & Activation Functions)",
     "อธิบายการทำงานของเซลล์ประสาทเทียม น้ำหนัก และไบแอส พร้อมเปรียบเทียบฟังก์ชันกระตุ้น Sigmoid และ ReLU ได้"),
    ("การประมวลผลภาพและภาษาธรรมชาติ (Computer Vision & NLP)",
     "อธิบายการแทนภาพด้วยพิกเซลและการแบ่งข้อความเป็นโทเคน พร้อมยกตัวอย่างงานด้านภาพและภาษาได้"),
    ("ปัญญาประดิษฐ์ที่อุปกรณ์ปลายทางและ AIoT (Edge AI / AIoT Project)",
     "ออกแบบแนวคิดโครงงานที่เชื่อมต่อเซนเซอร์กับ AI บนอุปกรณ์ปลายทาง โดยคำนึงถึงทรัพยากรและความเป็นส่วนตัวได้"),
]

st.set_page_config(
    page_title="Artificial Intelligence Laboratory",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stMainBlockContainer { max-width: 880px; padding-top: 2.5rem; }
    h1 { font-size: clamp(1.8rem, 5vw, 2.7rem) !important; }
    h1, h2, h3, p { overflow-wrap: anywhere; }
    [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        min-height: 48px;
    }
    [data-baseweb="select"] [data-baseweb="tag"],
    [role="option"] { white-space: normal; overflow-wrap: anywhere; }
    @media (max-width: 600px) {
        .stMainBlockContainer { padding: 1.5rem 1rem 2rem; }
        h3 { font-size: 1.25rem !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧠 Artificial Intelligence Laboratory")
st.markdown("Interactive AI Simulation for Teaching and Learning")
st.markdown("**Instructor: Sakda Wongadyarin**")
st.caption("ห้องปฏิบัติการปัญญาประดิษฐ์ · เวอร์ชัน 0.2 · 10 หน่วยการเรียนรู้")

st.write(
    "ห้องปฏิบัติการนี้ออกแบบให้นักศึกษาเรียนรู้ปัญญาประดิษฐ์ผ่านการจำลอง"
    "และการทดลองแบบโต้ตอบ เพื่อเชื่อมโยงแนวคิดในชั้นเรียนกับการลงมือปฏิบัติ "
    "เริ่มต้นด้วยการเลือกหน่วยการเรียนรู้และอ่านวัตถุประสงค์ด้านล่าง"
)

st.divider()
selected = st.selectbox(
    "เลือกหน่วยการเรียนรู้ / การทดลอง",
    options=range(len(UNITS)),
    format_func=lambda index: f"{index + 1}. {UNITS[index][0]}",
    key="selected_unit",
)
title, objective = UNITS[selected]

with st.container(border=True):
    st.caption(f"หน่วยที่ {selected + 1} / {len(UNITS)}")
    st.subheader(title)
    st.markdown("**วัตถุประสงค์การเรียนรู้**")
    st.write(objective)
    if selected == 1:
        from search_simulation import render_search_simulation

        render_search_simulation()
    else:
        st.info("Simulation coming soon", icon="🧪")
        st.caption("กำลังเตรียมการจำลองแบบโต้ตอบสำหรับหน่วยนี้ในเวอร์ชันถัดไป")

st.divider()
st.caption("Artificial Intelligence Laboratory")
st.caption("Developed for teaching and learning")
st.caption("Instructor: Sakda Wongadyarin")
