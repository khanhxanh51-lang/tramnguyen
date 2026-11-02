import random
import streamlit as st

st.set_page_config(
    page_title="Quizlet IELTS", page_icon="📚", layout="centered"
)

st.title("📚 Ứng Dụng Ôn Thi Từ Vựng IELTS")

# Danh sách từ vựng tích hợp sẵn trong code để không bị lỗi đọc file CSV
vocab_list = [
    ("alacrity", "(n.) brisk and cheerful readiness."),
    ("cacophony", "(n.) a harsh, discordant mixture of sounds."),
    (
        "debacle",
        "(n.) a sudden and ignominious failure; a fiasco. / (adj.) showing"
        " fearlessness and determination.",
    ),
    ("ebullient", "(adj.) cheerful and full of energy."),
    (
        "facetious",
        "(adj.) treating serious issues with deliberately inappropriate humor;",
        " flippant.",
    ),
    ("gainsay", "(v.) deny or contradict (a fact or statement)."),
    (
        "hackneyed",
        "(adj.) (of a phrase or idea) lacking significance through having been"
        " overused.",
    ),
    (
        "iconoclast",
        "(n.) a person who attacks cherished beliefs or institutions.",
    ),
    (
        "juxtapose",
        "(v.) place or deal with close together for contrasting effect.",
    ),
    ("kudos", "(n.) praise and honor received for an achievement."),
    ("lachrymose", "(adj.) tearful or given to weeping."),
    ("maverick", "(n.) an unorthodox or independent-minded person."),
    ("nefarious", "(adj.) wicked or criminal."),
    (
        "obdurate",
        "(adj.) stubbornly refusing to change one's opinion or course of"
        " action.",
    ),
    ("palliate", "(v.) make a disease or its symptoms less severe."),
    ("quixotic", "(adj.) exceedingly idealistic; unrealistic and impractical."),
    (
        "recalcitrant",
        "(adj.) having an uncooperative attitude toward authority or"
        " discipline.",
    ),
    (
        "sagacious",
        "(adj.) having or showing keen mental discernment and good judgment;",
        " wise.",
    ),
    (
        "taciturn",
        "(adj.) (of a person) reserved or uncommunicative in speech; saying"
        " little.",
    ),
    (
        "ubiquitous",
        "(adj.) present, appearing, or found everywhere.",
    ),  # Thêm các từ vựng khác nếu muốn
]

# Khởi tạo trạng thái ngẫu nhiên từ vựng
if "current_idx" not in st.session_state:
  st.session_state.current_idx = random.randint(0, len(vocab_list) - 1)
  st.session_state.show_def = False

word, definition = vocab_list[st.session_state.current_idx]

st.markdown("### Từ vựng:")
st.markdown(f"<h2 style='color: #29b6f6;'>{word}</h2>", unsafe_allow_html=True)

if st.session_state.show_def:
  st.success(f"**Nghĩa:** {definition}")

col1, col2 = st.columns(2)
with col1:
  if not st.session_state.show_def:
    if st.button("🔍 Xem nghĩa", use_container_width=True):
      st.session_state.show_def = True
      st.rerun()
with col2:
  if st.button("➡️ Từ tiếp theo", use_container_width=True):
    st.session_state.current_idx = random.randint(0, len(vocab_list) - 1)
    st.session_state.show_def = False
    st.rerun()
