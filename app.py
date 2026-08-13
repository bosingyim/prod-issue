import streamlit as st
from database import init_db

init_db()

st.set_page_config(page_title="Prod-Issue System", layout="wide", page_icon="🏭")

st.title("🏭 Prod-Issue: ระบบแจ้งปัญหาในไลน์การผลิต")
st.write("ยินดีต้อนรับสู่ระบบจัดการปัญหาหน้างานอัจฉริยะ")

st.info("👈 **คำแนะนำ:** กรุณาเลือกเมนูการทำงานจากแถบด้านซ้าย (Sidebar) เพื่อ **แจ้งปัญหาหน้างาน** หรือ **ดูแดชบอร์ดสรุปรายงาน**")