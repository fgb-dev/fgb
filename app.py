import streamlit as st

st.title("簡易診断アプリ")

st.write("以下の質問に1〜5でお答えください")

q1 = st.slider("質問①：計画的に物事を進める方だ", 1, 5, 3)
q2 = st.slider("質問②：思いついたらすぐに行動する方だ", 1, 5, 3)
q3 = st.slider("質問③：新しいアイデアを出すのが得意だ", 1, 5, 3)

if st.button("診断する"):
    score = q1 + q2 + q3

    if score >= 12:
        result = "あなたは【実行クリエイター型】です！"
    elif score >= 8:
        result = "あなたは【バランス型プランナー】です！"
    else:
        result = "あなたは【慎重ストラテジスト型】です！"

    st.subheader("診断結果")
    st.write(result)