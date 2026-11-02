import random
import streamlit as st

# Cấu hình trang web
st.set_page_config(
    page_title="IELTS Vocabulary Flashcards", page_icon="📚", layout="centered"
)

# Custom CSS để làm đẹp giao diện
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
    </style>
""",
    unsafe_allow_html=True,
)

# Tiêu đề chính ứng dụng
st.title("📚 Ôn Tập Từ Vựng IELTS Chuyên Sâu")
st.markdown(
    "Hệ thống flashcard trực quan & phân lô từ vựng Anh - Anh chuẩn xác."
)
st.markdown("---")

# Định nghĩa các lô từ vựng theo từng nhóm
batches = {
    "Lô 17 (F, G, H, I, J...)": [
        (
            "evanescent",
            (
                "(adj.) soon passing out of sight, memory, or existence; quickly"
                " fading."
            ),
        ),
        (
            "exacerbate",
            "(v.) make a problem, bad situation, or negative feeling worse.",
        ),
        (
            "exacting",
            (
                "(adj.) making great demands on one's skill, attention, or"
                " other resources."
            ),
        ),
        (
            "exculpate",
            (
                "(v.) show or declare that someone is not guilty of"
                " wrongdoing."
            ),
        ),
        ("execrable", "(adj.) extremely bad or unpleasant."),
        ("exigent", "(adj.) pressing; demanding."),
        (
            "exonerate",
            (
                "(v.) absolve (someone) from blame for a fault or"
                " wrongdoing."
            ),
        ),
        (
            "expediency",
            (
                "(n.) the quality of being convenient and practical despite"
                " possibly being improper."
            ),
        ),
        (
            "explicit",
            (
                "(adj.) stated clearly and in detail, leaving no room for"
                " confusion."
            ),
        ),
        (
            "extant",
            "(adj.) still in existence; surviving (of a document, object).",
        ),
        ("extol", "(v.) praise enthusiastically."),
        (
            "facetious",
            (
                "(adj.) treating serious issues with deliberately"
                " inappropriate humor."
            ),
        ),
        ("fallacious", "(adj.) based on a mistaken belief."),
        ("fatuous", "(adj.) silly and pointless."),
        (
            "fawning",
            (
                "(adj.) displaying exaggerated flattery or affection;"
                " obsequious."
            ),
        ),
        (
            "fervid",
            (
                "(adj.) intensely enthusiastic or passionate, especially to an"
                " excessive degree."
            ),
        ),
        (
            "fledgling",
            (
                "(n.) a person or organization that is immature or"
                " underdeveloped."
            ),
        ),
        (
            "florid",
            (
                "(adj.) having a red complexion; excessively intricate or"
                " elaborate."
            ),
        ),
        (
            "foment",
            (
                "(v.) instigate or stir up an undesirable or violent"
                " sentiment."
            ),
        ),
        (
            "forestall",
            "(v.) prevent or obstruct an anticipated event by taking action.",
        ),
    ],
    "Lô 18 (G, H, I, J, K...)": [
        ("gainsay", "(v.) deny or contradict a fact or statement."),
        (
            "galvanize",
            "(v.) shock or excite someone into taking action.",
        ),
        (
            "garrulous",
            "(adj.) excessively talkative, especially on trivial matters.",
        ),
        ("gauche", "(adj.) unsophisticated and socially awkward."),
        (
            "genealogy",
            "(n.) a line of descent traced continuously from an ancestor.",
        ),
        ("germane", "(adj.) relevant to a subject under consideration."),
        (
            "glib",
            "(adj.) fluent but insincere and shallow (of words/person).",
        ),
        (
            "goad",
            "(v.) provoke or annoy someone to stimulate some action.",
        ),
        (
            "gouge",
            "(v.) make a groove, hole, or scuff with a sharp tool.",
        ),
        (
            "grandiloquent",
            "(adj.) pompous or extravagant in language or style.",
        ),
        ("gregarious", "(adj.) fond of company; sociable."),
        ("guile", "(n.) sly or cunning intelligence."),
        ("gullible", "(adj.) easily persuaded to believe something; credulous."),
        (
            "hackneyed",
            "(adj.) lacking significance through having been overused.",
        ),
        (
            "halcyon",
            "(adj.) denoting a period of time in the past that was idyllically happy.",
        ),
        ("harangue", "(n.) a lengthy and aggressive speech."),
        ("hedonism", "(n.) the pursuit of pleasure; sensual self-indulgence."),
        (
            "heresy",
            "(n.) belief or opinion contrary to orthodox general doctrine.",
        ),
        ("heterogeneous", "(adj.) diverse in character or content."),
        (
            "iconoclast",
            "(n.) a person who attacks cherished beliefs or institutions.",
        ),
    ],
    "Lô 19-25 (Tổng hợp nâng cao)": [
        ("idiosyncrasy", "(n.) a mode of behavior peculiar to an individual."),
        ("ignominious", "(adj.) deserving or causing public disgrace or shame."),
        ("immutable", "(adj.) unchanging over time or unable to be changed."),
        ("impartial", "(adj.) treating all rivals equally; fair."),
        (
            "impasse",
            "(n.) a situation in which no progress is possible; a deadlock.",
        ),
        ("impecunious", "(adj.) having little or no money."),
        ("impediment", "(n.) a hindrance or obstruction in doing something."),
        (
            "imperious",
            "(adj.) assuming power without justification; arrogant.",
        ),
        ("impetuous", "(adj.) acting quickly without thought or care."),
        ("inchoate", "(adj.) just begun and not fully formed or developed."),
        ("indefatigable", "(adj.) persisting tirelessly."),
        ("indolent", "(adj.) wanting to avoid activity or exertion; lazy."),
        ("ineffable", "(adj.) too great to be expressed in words."),
        ("inert", "(adj.) lacking the ability or strength to move."),
        ("ingenuous", "(adj.) innocent and unsuspecting."),
        ("inimical", "(adj.) tending to obstruct or harm."),
        ("innocuous", "(adj.) not harmful or offensive."),
        ("insipid", "(adj.) lacking flavor or vigor/interest."),
        ("malediction", "(n.) a curse."),
        ("malleable", "(adj.) able to be pressed out of shape without breaking."),
    ],
}

# Thanh chọn mục (Selectbox) để lọc theo từng lô từ vựng mong muốn
selected_batch = st.selectbox(
    "📂 Chọn mục / Lô từ vựng muốn ôn tập:", list(batches.keys())
)
vocab_list = batches[selected_batch]

# Khởi tạo trạng thái phiên làm việc
if (
    "current_idx" not in st.session_state
    or "last_batch" not in st.session_state
    or st.session_state.last_batch != selected_batch
):
  st.session_state.current_idx = 0
  st.session_state.last_batch = selected_batch
  st.session_state.show_def = False

# Giới hạn index an toàn
if st.session_state.current_idx >= len(vocab_list):
  st.session_state.current_idx = 0

word, definition = vocab_list[st.session_state.current_idx]

# Hiển thị số thứ tự từ vựng trong lô
st.caption(
    f"Thẻ từ: **{st.session_state.current_idx + 1} / {len(vocab_list)}** trong"
    f" mục **{selected_batch}**"
)

# Khung thẻ từ vựng
st.markdown(
    f"""
    <div class="vocab-card">
        <div style="font-size: 13px; color: #888; margin-bottom: 5px; text-transform: uppercase;">IELTS Vocabulary</div>
        <div class="vocab-word">{word}</div>
    </div>
""",
    unsafe_allow_html=True,
)

# Hiển thị nghĩa khi bấm nút
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

# Các nút điều hướng thao tác
col1, col2, col3 = st.columns(3)

with col1:
  if st.button("⬅️ Từ trước", use_container_width=True):
    st.session_state.current_idx = (
        st.session_state.current_idx - 1
    ) % len(vocab_list)
    st.session_state.show_def = False
    st.rerun()

with col2:
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

with col3:
  if st.button("➡️ Từ tiếp", use_container_width=True):
    st.session_state.current_idx = (
        st.session_state.current_idx + 1
    ) % len(vocab_list)
    st.session_state.show_def = False
    st.rerun()
