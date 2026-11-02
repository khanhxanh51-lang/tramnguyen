import math
import os
import streamlit as st

# Cấu hình giao diện tối màu chuẩn app desktop
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
    
    .desktop-card {
        background-color: #1e1e2f;
        border: 1px solid #2d2d44;
        border-radius: 12px;
        padding: 40px 20px;
        text-align: center;
        min-height: 280px;
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
        font-size: 20px;
        color: #29b6f6;
        line-height: 1.5;
    }
    
    .badge {
        background-color: #2b2b40;
        color: #a0a0c0;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 12px;
        margin-bottom: 20px;
        text-transform: uppercase;
    }
    </style>
""",
    unsafe_allow_html=True,
)


@st.cache_data
def load_vocab():
  words = []
  possible_paths = ["vocabulary.csv", "./vocabulary.csv", "data/vocabulary.csv"]
  path_found = None
  for p in possible_paths:
    if os.path.exists(p):
      path_found = p
      break

  if path_found:
    try:
      with open(path_found, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
          line = line.strip()
          if not line:
            continue
          parts = line.split(",", 1)
          if len(parts) == 2:
            word = parts[0].strip().strip('"').strip("'")
            definition = parts[1].strip().strip('"').strip("'")
            if word and definition:
              words.append((word, definition))
    except Exception:
      pass

  if not words:
    words = [
        ("ambiguous", "(adj.) open to more than one interpretation."),
        ("resilient", "(adj.) able to withstand or recover quickly."),
    ]
  return words


all_words = load_vocab()

# Chia tự động thành các phần (mỗi phần 20 từ)
chunk_size = 20
batches = {}
total_sets = math.ceil(len(all_words) / chunk_size)

for i in range(total_sets):
  start_idx = i * chunk_size
  end_idx = min((i + 1) * chunk_size, len(all_words))
  set_name = f"Phần {i + 1}: IELTS Vocab ({start_idx + 1}-{end_idx})"
  batches[set_name] = all_words[start_idx:end_idx]

# Top bar: Chọn phần học & số đếm thẻ
top_c1, top_c2 = st.columns([2.5, 1])
with top_c1:
  selected_batch = st.selectbox(
      "☰ Chọn phần học từ vựng", list(batches.keys())
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
      f"<h4 style='text-align: right; color: #fff; margin-top:"
      f" 8px;'>{current_num} / {total_num}</h4>",
      unsafe_allow_html=True,
  )

st.markdown("<hr style='border-color: #2d2d44;'>", unsafe_allow_html=True)

word, definition = vocab_list[st.session_state.current_idx]

# Khu vực hiển thị thẻ Flashcard (Mặt trước / Mặt sau)
if not st.session_state.flipped:
  st.markdown(
      f"""
      <div class="desktop-card">
          <div class="badge">Từ mới</div>
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
          <div style="margin-top: 15px; color: #777; font-size: 13px;">Từ vựng: <b style="color: #fff;">{word}</b></div>
      </div>
  """,
      unsafe_allow_html=True,
  )

# LOGIC NÚT BẤM:
# 1. Nếu chưa lật: Chỉ hiện nút "LẬT XEM ĐỊNH NGHĨA" và nút lùi/tiến đơn giản.
# 2. Nếu đã lật: Ẩn nút lật đi, hiện đầy đủ 4 nút đánh giá (Xem lại, Khó, Ổn, Dễ) hoặc nút "Từ trước / Từ tiếp".

if not st.session_state.flipped:
  # Nút lật to bản chính giữa
  if st.button("LẬT XEM ĐỊNH NGHĨA", use_container_width=True, type="primary"):
    st.session_state.flipped = True
    st.rerun()

  # Hàng phụ cho phép bấm chuyển qua lại ngay cả khi chưa lật nếu muốn
  nav_c1, nav_c2 = st.columns(2)
  with nav_c1:
    if st.button("⬅️ Từ trước", use_container_width=True):
      st.session_state.current_idx = (
          st.session_state.current_idx - 1
      ) % total_num
      st.session_state.flipped = False
      st.rerun()
  with nav_c2:
    if st.button("Từ tiếp ➡️", use_container_width=True):
      st.session_state.current_idx = (
          st.session_state.current_idx + 1
      ) % total_num
      st.session_state.flipped = False
      st.rerun()

else:
  # Khi đã lật ra nghĩa -> Hiện các nút đánh giá mức độ
  st.markdown(
      "<p style='text-align: center; color: #aaa; font-size: 14px; margin-bottom:"
      " 5px;'>Đánh giá mức độ ghi nhớ của từ này:</p>",
      unsafe_allow_html=True,
  )
  c1, c2, c3, c4 = st.columns(4)

  with c1:
    if st.button("Xem lại", use_container_width=True):
      st.session_state.current_idx = (
          st.session_state.current_idx + 1
      ) % total_num
      st.session_state.flipped = False
      st.rerun()
  with c2:
    if st.button("Khó", use_container_width=True):
      st.session_state.current_idx = (
          st.session_state.current_idx + 1
      ) % total_num
      st.session_state.flipped = False
      st.rerun()
  with c3:
    if st.button("Ổn", use_container_width=True):
      st.session_state.current_idx = (
          st.session_state.current_idx + 1
      ) % total_num
      st.session_state.flipped = False
      st.rerun()
  with c4:
    if st.button("Dễ", use_container_width=True):
      st.session_state.current_idx = (
          st.session_state.current_idx + 1
      ) % total_num
      st.session_state.flipped = False
      st.rerun()

  st.markdown(
      """
      <table style="width: 100%; text-align: center; color: #888; font-size: 11px; margin-top: 5px;">
          <tr>
              <td>Tối đa 1 phút</td>
              <td>Tối đa 5 phút</td>
              <td>Tối đa 10 phút</td>
              <td>4 ngày</td>
          </tr>
      </table>
  """,
      unsafe_allow_html=True,
  )

  # Thêm hàng nút phụ bên dưới để quay lại từ trước hoặc làm lại từ đầu bộ học
  sub_c1, sub_c2 = st.columns(2)
  with sub_c1:
    if st.button("⬅️ Xem lại từ trước", use_container_width=True):
      st.session_state.current_idx = (
          st.session_state.current_idx - 1
      ) % total_num
      st.session_state.flipped = False
      st.rerun()
  with sub_c2:
    if st.button("🔄 Làm lại từ đầu phần này", use_container_width=True):
      st.session_state.current_idx = 0
      st.session_state.flipped = False
      st.rerun()
