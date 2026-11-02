import math
import os
import random
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

# Chia tự động thành các phần (mỗi phần 20 từ) và thêm chế độ thi thử Random 20 từ
chunk_size = 20
batches = {}
total_sets = math.ceil(len(all_words) / chunk_size)

for i in range(total_sets):
  start_idx = i * chunk_size
  end_idx = min((i + 1) * chunk_size, len(all_words))
  set_name = f"Phần {i + 1}: IELTS Vocab ({start_idx + 1}-{end_idx})"
  batches[set_name] = all_words[start_idx:end_idx]

# Thêm mục thi thử random 20 từ từ toàn bộ kho
if len(all_words) >= 20:
  batches["🎯 Thi thử Random 20 từ"] = random.sample(all_words, 20)
else:
  batches["🎯 Thi thử Random 20 từ"] = all_words

# Top bar: Chọn phần học & trạng thái
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
    st.session_state.history = {}
    st.session_state.show_summary = False

  current_num = st.session_state.current_idx + 1
  total_num = len(vocab_list)

  if not st.session_state.show_summary:
    st.markdown(
        f"<h4 style='text-align: right; color: #fff; margin-top:"
        f" 8px;'>{current_num} / {total_num}</h4>",
        unsafe_allow_html=True,
    )
  else:
    st.markdown(
        "<h4 style='text-align: right; color: #29b6f6; margin-top:"
        " 8px;'>Hoàn thành</h4>",
        unsafe_allow_html=True,
    )

st.markdown("<hr style='border-color: #2d2d44;'>", unsafe_allow_html=True)

# GIAO DIỆN TỔNG KẾT & TÍNH ĐIỂM
if st.session_state.show_summary:
  st.markdown(
      "<h2 style='text-align: center; color: #29b6f6;'>📊 Bảng Tổng Kết Kết"
      " Quả & Điểm Số</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      f"<p style='text-align: center; color: #aaa;'>Chế độ: <b>{selected_batch}</b></p>",
      unsafe_allow_html=True,
  )

  # Tự động gán nhãn "Bỏ qua" cho các từ chưa đánh giá
  for w, _ in vocab_list:
    if w not in st.session_state.history:
      st.session_state.history[w] = "Bỏ qua"

  # Tính điểm theo thang điểm 10
  score_map = {"Dễ": 10.0, "Ổn": 8.0, "Khó": 5.0, "Xem lại": 2.0, "Bỏ qua": 0.0}

  total_score = 0
  counts = {"Dễ": 0, "Ổn": 0, "Khó": 0, "Xem lại": 0, "Bỏ qua": 0}

  for w, _ in vocab_list:
    status = st.session_state.history.get(w, "Bỏ qua")
    total_score += score_map.get(status, 0.0)
    if status in counts:
      counts[status] += 1

  final_score = round(total_score / len(vocab_list), 1)

  st.markdown(
      f"""
      <div style="background-color: #1e1e2f; border: 2px solid #29b6f6; border-radius: 16px; padding: 25px; text-align: center; margin-bottom: 25px;">
          <div style="font-size: 16px; color: #aaa; text-transform: uppercase; letter-spacing: 1px;">Điểm số đánh giá năng lực</div>
          <div style="font-size: 54px; font-weight: bold; color: #29b6f6; margin: 10px 0;">{final_score} <span style="font-size: 24px; color: #888;">/ 10</span></div>
          <div style="font-size: 14px; color: #ddd;">
              🟢 Dễ: <b>{counts['Dễ']}</b> | 🔵 Ổn: <b>{counts['Ổn']}</b> | 🟠 Khó: <b>{counts['Khó']}</b> | 🔴 Xem lại: <b>{counts['Xem lại']}</b> | ⚫ Bỏ qua: <b>{counts['Bỏ qua']}</b>
          </div>
      </div>
  """,
      unsafe_allow_html=True,
  )

  st.markdown("### 📝 Chi tiết bài kiểm tra:")
  for idx, (w, d) in enumerate(vocab_list):
    status = st.session_state.history.get(w, "Bỏ qua")
    color_map = {
        "Xem lại": "#ff4d4d",
        "Khó": "#ffa500",
        "Ổn": "#29b6f6",
        "Dễ": "#4CAF50",
        "Bỏ qua": "#777777",
    }
    badge_color = color_map.get(status, "#777")
    st.markdown(
        f"""
        <div style="background-color: #1e1e2f; padding: 12px 18px; border-radius: 8px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center; border: 1px solid #2d2d44;">
            <div>
                <span style="font-size: 16px; font-weight: bold; color: #fff;">{idx + 1}. {w}</span>
                <div style="font-size: 13px; color: #888;">{d}</div>
            </div>
            <div>
                <span style="background-color: {badge_color}; color: #fff; padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: bold;">{status}</span>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

  st.markdown("<br>", unsafe_allow_html=True)
  col_sum1, col_sum2 = st.columns(2)
  with col_sum1:
    if st.button("🔄 Thi lại đề mới / Học lại", use_container_width=True):
      # Nếu đang ở chế độ thi thử, bấm học lại sẽ tạo bộ random 20 từ mới hoàn toàn
      if "Thi thử" in selected_batch and len(all_words) >= 20:
        batches["🎯 Thi thử Random 20 từ"] = random.sample(all_words, 20)
      st.session_state.current_idx = 0
      st.session_state.flipped = False
      st.session_state.history = {}
      st.session_state.show_summary = False
      st.rerun()
  with col_sum2:
    if st.button("🔙 Tiếp tục xem lại thẻ", use_container_width=True):
      st.session_state.show_summary = False
      st.rerun()

else:
  # GIAO DIỆN HỌC THÔNG THƯỜNG
  word, definition = vocab_list[st.session_state.current_idx]
  current_status = st.session_state.history.get(word, None)

  if not st.session_state.flipped:
    st.markdown(
        f"""
        <div class="desktop-card">
            <div class="badge">Từ kiểm tra</div>
            <div class="vocab-word">{word}</div>
            {f'<div style="margin-top: 15px; color: #29b6f6; font-size: 13px;">Đã đánh giá: <b>{current_status}</b></div>' if current_status else ''}
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
            <div style="margin-top: 15px; color: #777; font-size: 13px;">Từ vựng: <b style="color: #fff;">{word}</b> {f'| Đánh giá hiện tại: <b style="color: #29b6f6;">{current_status}</b>' if current_status else ''}</div>
        </div>
    """,
        unsafe_allow_html=True,
    )


  def go_next():
    if word not in st.session_state.history:
      st.session_state.history[word] = "Bỏ qua"

    if st.session_state.current_idx < total_num - 1:
      st.session_state.current_idx += 1
      st.session_state.flipped = False
    else:
      st.session_state.show_summary = True
    st.rerun()


  def go_prev():
    if st.session_state.current_idx > 0:
      st.session_state.current_idx -= 1
      st.session_state.flipped = False
      st.rerun()


  if not st.session_state.flipped:
    if st.button("LẬT XEM ĐỊNH NGHĨA", use_container_width=True, type="primary"):
      st.session_state.flipped = True
      st.rerun()

    nav_c1, nav_c2 = st.columns(2)
    with nav_c1:
      if st.button("⬅️ Từ trước", use_container_width=True):
        go_prev()
    with nav_c2:
      if st.button("Bỏ qua ➡️", use_container_width=True):
        st.session_state.history[word] = "Bỏ qua"
        go_next()
  else:
    st.markdown(
        "<p style='text-align: center; color: #aaa; font-size: 14px; margin-bottom:"
        " 5px;'>Đánh giá mức độ ghi nhớ của từ này (chọn xong có thể bấm nút"
        " 'Từ tiếp theo'):</p>",
        unsafe_allow_html=True,
    )


    def save_rating(level):
      st.session_state.history[word] = level
      st.rerun()


    c1, c2, c3, c4 = st.columns(4)
    with c1:
      if st.button("Xem lại", use_container_width=True):
        save_rating("Xem lại")
    with c2:
      if st.button("Khó", use_container_width=True):
        save_rating("Khó")
    with c3:
      if st.button("Ổn", use_container_width=True):
        save_rating("Ổn")
    with c4:
      if st.button("Dễ", use_container_width=True):
        save_rating("Dễ")

    st.markdown(
        """
        <style>
        .footer-table td { border: none !important; }
        </style>
        <table class="footer-table" style="width: 100%; text-align: center; color: #888; font-size: 11px; margin-top: 5px;">
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

    st.markdown("<br>", unsafe_allow_html=True)

    sub_c1, sub_c2, sub_c3 = st.columns(3)
    with sub_c1:
      if st.button("⬅️ Từ trước", use_container_width=True):
        go_prev()
    with sub_c2:
      if st.button("Từ tiếp theo ➡️", use_container_width=True, type="primary"):
        go_next()
    with sub_c3:
      if st.button("📊 Xem tổng kết", use_container_width=True):
        st.session_state.show_summary = True
        st.rerun()
