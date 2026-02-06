import streamlit as st
import os
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("AI StudyMate")

prompt = st.text_input("Nhập câu hỏi:")

if st.button("Hỏi AI") and prompt:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    st.write(response.text)

# 3. Giao diện ứng dụng
st.set_page_config(page_title="AISTUDYMATE", layout="centered")
st.title("🎓 AISTUDYMATE - Trợ lý học tập AI")
st.info("Giải pháp cá nhân hóa lộ trình học tập")
st.markdown("---")

# Nhập liệu
name = st.text_input("Họ và tên", "Học sinh")
subject = st.selectbox("Môn học", ["Toán học", "Ngữ Văn", "Tiếng Anh", "Vật Lý"])
score = st.slider("Điểm số hiện tại", 0.0, 10.0, 5.0)
weakness = st.text_area("Phần kiến thức bạn thấy khó nhất?")

# 4. Xử lý tạo lộ trình
if st.button("Phân tích & Tạo lộ trình"):
    if weakness:
        with st.spinner('AI đang làm việc...'):
            try:
                # Tạo prompt
                prompt = f"Học sinh {name}, môn {subject}, điểm {score}. Khó khăn: {weakness}. Lập lộ trình 7 ngày."
                
                # Gọi AI
                response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)
                
                # Hiện kết quả
                st.success(f"Lộ trình dành cho {name}:")
                st.markdown(response.text)
                
            except Exception as e:
                # Nếu vẫn lỗi 404, dùng dự phòng model 'gemini-pro'
                st.error(f"Lỗi: {e}")
    else:
        st.warning("Vui lòng nhập khó khăn!")
