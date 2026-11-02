import math
import os
import pandas as pd
import streamlit as st

# Cấu hình trang giao diện tối màu chuẩn app desktop
st.set_page_config(
    page_title="Massive IELTS Flashcards", page_icon="🪶", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #12121f;
        color: #ffffff;
    }
    header {visibility: hidden;}
    
    /* Khung thẻ Flashcard y hệt bản desktop */
    .desktop-card {
        background-color: #1e1e2f;
        border: 1px solid #2d2d44;
        border-radius: 12px;
        padding: 50px 20px;
        text-align: center;
        min-height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        margin-bottom: 20px;
    }
    
    .vocab-word {
        font-size: 42px;
        font-weight: bold;
        color: #ffffff;
        letter-spacing: 1px;
    }
    
    .def-text {
        font-size: 22px;
        color: #29b6f6;
        line-height: 1.6;
    }
    
    .badge {
        background-color: #2b2b40;
        color: #a0a0c0;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 12px;
        margin-bottom: 25px;
        text-transform: uppercase;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Đọc file vocabulary.csv từ GitHub với cơ chế tìm đường dẫn linh hoạt
@st.cache_data
def load_vocab():
  possible_paths = ["vocabulary.csv", "./vocabulary.csv", "data/vocabulary.csv"]
  df = None
  for path in possible_paths:
    if os.path.exists(path):
      try:
        df = pd.read_csv(path, header=None, names=["Word", "Definition"])
        break
      except Exception:
        pass
  if df is not None:
    df = df.dropna()
    return df.values.tolist()
  return []


all_words = load_vocab()

if not all_words:
  st.error(
      "⚠️ Không tìm thấy file `vocabulary.csv`! T hãy chắc chắn là file"
      " `vocabulary.csv` đã được đẩy lên **cùng thư mục gốc** với file `app.py`"
      " trên GitHub nhé."
  )
else:
  # Chia tự động thành các phần (mỗi phần 20 từ y hệt ảnh)
  chunk_size = 20
  batches = {}
  total_sets = math.ceil(len(all_words) / chunk_size)

  for i in range(total_sets):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, len(all_words))
    set_name = f"Phần {i + 1}: IELTS Vocab ({start_idx + 1}-{end_idx})"
    batches[set_name] = all_words[start_idx:end_idx]

  # Top bar giả lập thanh tiêu đề app desktop
  top_c1, top_c2 = st.columns([3, 1])
  with top_c1:
    selected_batch = st.selectbox(
        "☰ Chọn phần học từ vựng", list(batches.keys()), label_visibility="collapsed"
    )
  with top_c2:
    vocab_list = batches[selected_batch]
    if (
        "current_idx" not in st.session_state
        or "last_batch" not in st.session_state
        or st.session_state.last_batch != selected_batch
    ):
      st.session_state.current_idx = 0
      st.session_state.last_batch = selected_batch
      st.session_state.flipped = False

    if st.session_state.current_idx >= len(vocab_list):
      st.session_state.current_idx = 0

    current_num = st.session_state.current_idx + 1
    total_num = len(vocab_list)
    st.markdown(
        f"<h3 style='text-align: right; color: #fff; margin-top: 5px;'>{current_num} / {total_num}</h3>",
        unsafe_allow_html=True,
    )

  st.markdown("<hr style='border-color: #2d2d44;'>", unsafe_allow_html=True)

  word, definition = vocab_list[st.session_state.current_idx]

  # Khu vực thẻ Flashcard
  if not st.session_state.flipped:
    st.markdown(
        f"""
        <div class="desktop-card">
            <div class="badge">Mới</div>
            <div class="vocab-word">{word}</div>
        </div>
    """,
        unsafe_allow_html=True,
    )
  else:
    st.markdown(
        f"""
        <div class="desktop-card" style="background-color: #161625;">
            <div class="badge" style="background-color: #1f3a60; color: #64b5f6;">Định nghĩa Anh - Anh</div>
            <div class="def-text">{definition}</div>
            <div style="margin-top: 20px; color: #777; font-size: 14px;">Từ vựng: <b style="color: #fff;">{word}</b></div>
        </div>
    """,
        unsafe_allow_html=True,
    )

  # Nút bấm lật nghĩa màu xanh đậm to bản y hệt desktop
  if not st.session_state.flipped:
    if st.button("LẬT XEM ĐỊNH NGHĨA", use_container_width=True, type="primary"):
      st.session_state.flipped = True
      st.rerun()
  else:
    col_prev, col_next = st.columns(2)
    with col_prev:
      if st.button("⬅️ Từ trước", use_container_width=True):
        st.session_state.current_idx = (
            st.session_state.current_idx - 1
        ) % total_num
        st.session_state.flipped = False
        st.rerun()
    with col_next:
      if st.button("Từ tiếp ➡️", use_container_width=True):
        st.session_state.current_idx = (
            st.session_state.current_idx + 1
        ) % total_num
        st.session_state.flipped = False
        st.rerun()
