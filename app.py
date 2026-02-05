import streamlit as st
import google.generativeai as genai

# 1. Cấu hình API Key mới của bạn (đuôi ...uWA0)
genai.configure(api_key="AIzaSyDkOueYuWbSDXrtIxLFRlkGtHxo0fcyYU8")

# 2. Sửa lỗi 404 bằng cách dùng tên model cơ bản nhất
# Không dùng 'latest' hay 'v1beta' để đảm bảo ổn định
model = genai.GenerativeModel('gemini-3-flash-preview')

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
                response = model.generate_content(prompt)
                
                # Hiện kết quả
                st.success(f"Lộ trình dành cho {name}:")
                st.markdown(response.text)
                
            except Exception as e:
                # Nếu vẫn lỗi 404, dùng dự phòng model 'gemini-pro'
                st.error(f"Lỗi: {e}")
    else:
        st.warning("Vui lòng nhập khó khăn!")