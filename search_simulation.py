"""Streamlit presentation for Unit 2; algorithms live in core."""

import networkx as nx
import streamlit as st
from matplotlib.figure import Figure

from core.search_algorithms import bfs, dfs


GRAPH = {
    "A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F", "G"],
    "D": ["B"], "E": ["B"], "F": ["C"], "G": ["C"],
}
POSITIONS = {
    "A": (0, 2), "B": (-1, 1), "C": (1, 1),
    "D": (-1.5, 0), "E": (-0.5, 0), "F": (0.5, 0), "G": (1.5, 0),
}


def graph_figure(step, path):
    graph = nx.Graph(GRAPH)
    figure = Figure(figsize=(6, 3.8), facecolor="white")
    ax = figure.subplots()
    colors = [
        "#86efac" if node in path else
        "#fbbf24" if node == step.current else
        "#93c5fd" if node in step.visited_order else "#e2e8f0"
        for node in graph
    ]
    nx.draw_networkx(
        graph, pos=POSITIONS, ax=ax, node_color=colors, node_size=1150,
        font_size=21, font_weight="bold", font_color="#0f172a",
        edge_color="#94a3b8", linewidths=2,
        edgecolors=["#b45309" if n == step.current else "#475569" for n in graph],
    )
    if path:
        nx.draw_networkx_edges(graph, POSITIONS, ax=ax,
                               edgelist=list(zip(path, path[1:])),
                               edge_color="#15803d", width=4)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-0.45, 2.45)
    ax.axis("off")
    figure.tight_layout(pad=0.3)
    return figure


def reset_step():
    st.session_state.search_step = 0


def render_search_simulation():
    st.markdown("### ทดลองค้นหาบนกราฟ (Graph / State Space)")
    st.write("โหนด A–G แทนสถานะ และเส้นเชื่อมแทนการเดินทางได้ทั้งสองทิศทาง โดยทุกเส้นมีต้นทุนเท่ากัน")
    st.write("BFS ค้นหาเป็นระดับและใช้ Queue (FIFO) ส่วน DFS ค้นหาลึกตามกิ่งและใช้ Stack (LIFO)")
    algorithm = st.selectbox("เลือกอัลกอริทึม", ["BFS", "DFS"], key="search_algorithm", on_change=reset_step)
    start = st.selectbox("จุดเริ่มต้น (Start)", list(GRAPH), key="search_start", on_change=reset_step)
    goal = st.selectbox("จุดเป้าหมาย (Goal)", list(GRAPH), index=6, key="search_goal", on_change=reset_step)
    result = (bfs if algorithm == "BFS" else dfs)(GRAPH, start, goal)
    st.write(f"**อัลกอริทึม: {algorithm} · จุดเริ่มต้น: {start} · จุดเป้าหมาย: {goal}**")
    st.caption("ลำดับเพื่อนบ้านเรียง A–G: ข้ามโหนดที่ค้นพบแล้ว และไม่เพิ่มซ้ำ "
               "DFS ใส่เพื่อนบ้านลง Stack ย้อนลำดับเพื่อดึงตัวแรกก่อน "
               "จาก A จึงสำรวจซ้ายก่อนขวา ลำดับ DFS อาจต่างกันได้เมื่อเปลี่ยนลำดับเพื่อนบ้าน")
    # Reserve the graph above the slider, then fill it using this run's value.
    graph_slot = st.empty()
    step_index = st.slider("ขั้นตอนการค้นหา", 0, len(result.history) - 1, key="search_step")
    step = result.history[step_index]
    visible_path = result.path if step.found else []
    figure = graph_figure(step, visible_path)
    graph_slot.pyplot(figure, width="stretch")
    figure.clear()
    st.caption("สีเทา: ยังไม่เยี่ยมชม · สีฟ้า: เยี่ยมชมแล้ว · สีเหลือง/ขอบส้ม: โหนดปัจจุบัน · สีเขียว: เส้นทางที่พบ")
    st.write(f"**โหนดปัจจุบัน:** {step.current or '—'}")
    st.write(f"**เยี่ยมชมแล้ว (Visited):** {', '.join(sorted(step.visited_order)) or '—'}")
    st.write(f"**ลำดับการค้นหา (Search Order):** {' → '.join(step.visited_order) or '—'}")
    structure = "Queue" if algorithm == "BFS" else "Stack"
    st.write(f"**{structure}:** [{', '.join(step.frontier)}]")
    st.caption("Queue: ดึงด้านซ้ายก่อน (FIFO)" if algorithm == "BFS" else "Stack: ด้านขวาคือยอด ดึงด้านขวาก่อน (LIFO)")
    st.caption("แต่ละขั้นแสดงสถานะหลังเยี่ยมชมโหนดและเพิ่มเพื่อนบ้าน หยุดทันทีเมื่อเยี่ยมชมเป้าหมาย "
               "โหนดที่รอใน Queue/Stack ยังไม่นับว่าเยี่ยมชมแล้ว")
    if step.found:
        st.success(f"เส้นทางที่พบ: {' → '.join(visible_path)}")
        st.write(f"**จำนวนเส้นเชื่อม (Number of edges):** {len(visible_path) - 1}")
        st.caption("พบเป้าหมายแล้ว จึงหยุดค้นหาแม้อาจมีโหนดเหลือใน Queue/Stack")
    elif step_index == len(result.history) - 1:
        st.warning("ไม่พบเส้นทางไปยังเป้าหมาย")
    else:
        st.info("เลื่อนขั้นตอนเพื่อสำรวจต่อ ยังไม่แสดงเส้นทางจนกว่าจะเยี่ยมชมเป้าหมาย")
    st.markdown("#### เปรียบเทียบ BFS และ DFS")
    st.markdown("""
| หัวข้อ | BFS | DFS |
| :--- | :--- | :--- |
| โครงสร้างข้อมูล | Queue (FIFO) | Stack (LIFO) |
| วิธีค้นหา | ทีละระดับ | ลงลึกตามกิ่ง แล้วถอยกลับ |
| รับประกันเส้นทางสั้นที่สุดในกราฟไม่มีน้ำหนัก | ใช่ | ไม่รับประกัน |
""")
    st.caption("กราฟตัวอย่างนี้เป็นต้นไม้ จึงมีเส้นทางเดียวระหว่างแต่ละคู่โหนด "
               "BFS และ DFS จึงได้เส้นทางเดียวกัน แต่อาจเยี่ยมชมโหนดต่างลำดับกัน "
               "ผลนี้ไม่ได้หมายความว่า DFS รับประกันเส้นทางสั้นที่สุดในกราฟทั่วไป")
