import streamlit as st

# 예시 단어 리스트
subjects = ["わたし", "あなた", "せんせい", "ともだち"]
objects = ["がくせい", "にほんじん", "こうこうせい", "せんせい"]
verb_patterns = {
    "정중형(긍정)": "です",
    "부정형": "じゃありません",
    "의문형": "ですか"
}

st.title("고등학교 일본어 교과서 1과 - 단어 연결 문장 만들기")

col1, col2, col3 = st.columns(3)
with col1:
    subject = st.selectbox("주어", subjects)
with col2:
    obj = st.selectbox("목적어/보어", objects)
with col3:
    verb_type = st.selectbox("서술어 패턴", list(verb_patterns.keys()))

verb = verb_patterns[verb_type]
sentence = f"{subject} は {obj} {verb}"
if verb_type == "의문형":
    sentence += "？"
else:
    sentence += "。"

st.markdown(f"**만든 문장:** {sentence}")

st.info("예시: わたし は がくせい です。 / あなた は せんせい じゃありません。 / ともだち は にほんじん ですか？")