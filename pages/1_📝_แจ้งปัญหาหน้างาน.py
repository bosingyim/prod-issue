import streamlit as st
from database import insert_issue

st.set_page_config(page_title="แจ้งปัญหาหน้างาน", page_icon="📝")
st.subheader("📝 บันทึกปัญหาเครื่องจักร / ไลน์ผลิต")

with st.form("issue_form", clear_on_submit=True):
    line_name = st.selectbox("เลือกไลน์การผลิต", ["Line 1", "Line 2", "Line 3", "Line 4"])
    machine_name = st.text_input("ชื่อเครื่องจักร / จุดเกิดเหตุ")
    issue_type = st.selectbox("ประเภทปัญหา", ["เครื่องจักรขัดข้อง", "วัตถุดิบมีปัญหา", "คุณภาพชิ้นงาน (Defect)", "อื่น ๆ"])
    description = st.text_area("รายละเอียดอาการเบื้องต้น")
    
    submitted = st.form_submit_button("ส่งแจ้งปัญหา")
    
    if submitted:
        if machine_name.strip() == "":
            st.warning("กรุณาระบุชื่อเครื่องจักรก่อนส่งข้อมูล")
        else:
            insert_issue(line_name, machine_name, issue_type, description)
            st.success("บันทึกข้อมูลลงฐานข้อมูลเรียบร้อยแล้ว!")
