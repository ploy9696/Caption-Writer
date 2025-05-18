
import streamlit as st
import openai

st.set_page_config(page_title="📝 GPT Caption Writer", page_icon="💫")

st.title("📝 GPT Caption Writer")
st.write("ใส่ keyword แล้วให้ AI เขียน SEO Title, Subtitle และ Caption แบบ emotional healing jewelry")

# ให้เบนใส่ OpenAI API Key แบบปลอดภัย
api_key = st.text_input("🔐 ใส่ OpenAI API Key", type="password")

keyword = st.text_input("✨ ใส่คำ keyword ที่ต้องการ (เช่น: soul necklace, healing pendant)")

if api_key and keyword:
    with st.spinner("🧠 กำลังเขียน caption ให้คุณ..."):
        openai.api_key = api_key
        prompt = f"""
คุณคือนักเขียน Copywriter สายจิตวิญญาณและอารมณ์ลึก  
ช่วยเขียน SEO Title, Subtitle, และ Instagram Caption  
สำหรับสินค้าที่ชื่อว่า "{keyword}" ซึ่งเป็นของแทนใจสำหรับผู้หญิงอายุ 28–45 ปี  
ที่กำลังมองหาสิ่งเชื่อมโยงกับ healing, energy, soul connection

เขียนโดยให้รู้สึกว่า 'สิ่งนี้พูดกับหัวใจ' จริง ๆ
เนื้อหาอบอุ่น จริงใจ และไม่ขายของเกินจริง

ตอบกลับในรูปแบบนี้เท่านั้น:
Title:
Subtitle:
Caption:
""".strip()

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "คุณคือนักเขียน emotional jewelry professional"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=400
            )
            result = response.choices[0].message["content"]
            st.success("✅ เขียนสำเร็จแล้ว!")
            st.text_area("💬 ผลลัพธ์:", result, height=300)
        except Exception as e:
            st.error(f"⚠️ เกิดข้อผิดพลาด: {e}")
else:
    st.info("กรุณาใส่ API Key และ keyword ก่อนเพื่อเริ่มเขียน caption")
