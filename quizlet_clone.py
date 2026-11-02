import random
import streamlit as st

# Cấu hình trang web
st.set_page_config(
    page_title="IELTS Vocabulary Flashcards", page_icon="📚", layout="centered"
)

# Custom CSS để làm đẹp giao diện, tạo khung thẻ từ vựng nổi bật
st.markdown(
    """
    <style>
    .vocab-card {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #e9ecef;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    .vocab-word {
        font-size: 40px;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 10px;
    }
    .vocab-def {
        font-size: 20px;
        color: #2c3e50;
        margin-top: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Tiêu đề chính ứng dụng
st.title("📚 Ôn Tập Từ Vựng IELTS Chuyên Sâu")
st.markdown(
    "Hệ thống flashcard trực quan giúp t ôn luyện từ vựng Anh - Anh chuẩn xác"
    " nhất."
)
st.markdown("---")

# Danh sách từ vựng tích hợp sẵn đầy đủ các lô
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
        "(adj.) treating serious issues with deliberately inappropriate humor;"
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
    ("ubiquitous", "(adj.) present, appearing, or found everywhere."),
    ("acerbic", "(adj.) sharp and forthright; expressing harsh or sharp criticism."),
    ("bellicose", "(adj.) demonstrating aggression and willingness to fight."),
    (
        "capricious",
        "(adj.) given to sudden and unaccountable changes of mood or behavior.",
    ),
    ("deleterious", "(adj.) causing harm or damage."),
    ("effrontery", "(n.) insolent or impertinent behavior."),
    (
        "fastidious",
        "(adj.) very attentive to and concerned about accuracy and detail.",
    ),
    ("gargantuan", "(adj.) enormous; gigantic."),
    ("hedonistic", "(adj.) engaged in the pursuit of pleasure."),
    ("ignoble", "(adj.) not honorable in character or purpose."),
    ("jejune", "(adj.) naive, simplistic, and superficial."),
]

# Khởi tạo trạng thái phiên làm việc
if "current_idx" not in st.session_state:
  st.session_state.current_idx = random.randint(0, len(vocab_list) - 1)
  st.session_state.show_def = False

word, definition = vocab_list[st.session_state.current_idx]

# Khung hiển thị thẻ từ vựng (Flashcard Box)
st.markdown(
    f"""
    <div class="vocab-card">
        <div style="font-size: 14px; color: #888; margin-bottom: 5px;">THẺ TỪ VỰNG</div>
        <div class="vocab-word">{word}</div>
    </div>
""",
    unsafe_allow_html=True,
)

# Hiển thị nghĩa nếu người dùng bấm nút xem
if st.session_state.show_def:
  st.markdown(
      f"""
        <div style="background-color: #e8f4fd; padding: 20px; border-radius: 10px; border-left: 5px solid #29b6f6; margin-bottom: 20px;">
            <div style="font-weight: bold; color: #0277bd; margin-bottom: 5px;">Định nghĩa Anh - Anh:</div>
            <div style="font-size: 18px; color: #333;">{definition}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

# Chia cột cho các nút bấm điều hướng gọn gàng
col1, col2 = st.columns(2)

with col1:
  if not st.session_state.show_def:
    if st.button(
        "🔍 Lật xem nghĩa", use_container_width=True, type="primary"
    ):
      st.session_state.show_def = True
      st.rerun()
  else:
    if st.button("👁️ Ẩn nghĩa", use_container_width=True):
      st.session_state.show_def = False
      st.rerun()

with col2:
  if st.button("➡️ Từ tiếp theo", use_container_width=True):
    st.session_state.current_idx = random.randint(0, len(vocab_list) - 1)
    st.session_state.show_def = False
    st.rerun()

# Phần thông tin phụ bên dưới
st.markdown("---")
st.caption(
    f"💡 Tổng số từ vựng trong kho: **{len(vocab_list)} từ** | Bấm 'Từ tiếp theo'"
    " để random từ ngẫu nhiên."
)
