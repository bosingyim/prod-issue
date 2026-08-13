import streamlit as st
from database import get_all_issues

st.set_page_config(page_title="แดชบอร์ดสรุปรายงาน", page_icon="📊")
st.subheader("📊 สถิติและประวัติปัญหาการผลิตย้อนหลัง")

data = get_all_issues()

if data.empty:
    st.info("ยังไม่มีประวัติการแจ้งปัญหาในระบบ")
else:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("จำนวนปัญหารวมทั้งหมด", f"{len(data)} เคส")
    with col2:
        st.metric("จำนวนไลน์ผลิตที่มีปัญหา", f"{data['line'].nunique()} ไลน์")
        
    st.markdown("---")
    st.dataframe(data, use_container_width=True)