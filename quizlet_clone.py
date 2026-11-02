import math
import pandas as pd
import streamlit as st

# Cấu hình trang web giao diện Dark Mode
st.set_page_config(
    page_title="IELTS Flashcard Pro", page_icon="📚", layout="centered"
)

# Custom CSS ép giao diện tối màu, bo góc chuẩn app mobile/flashcard cao cấp
st.markdown(
    """
    <style>
    /* Tổng thể nền tối */
    .stApp {
        background-color: #12121f;
        color: #ffffff;
    }
    
    /* Ẩn bớt các thanh header mặc định của streamlit cho gọn */
    header {visibility: hidden;}
    
    /* Khung thẻ Flashcard */
    .flashcard {
        background-color: #1e1e2f;
        border: 1px solid #2d2d44;
        border-radius: 20px;
        padding: 40px 20px;
        text-align: center;
        min-height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }
    
    .vocab-text {
        font-size: 36px;
        font-weight: bold;
        color: #ffffff;
        word-break: break-word;
    }
    
    .def-text {
        font-size: 22px;
        color: #e0e0e0;
        line-height: 1.5;
        word-break: break-word;
    }
    
    /* Nhãn trạng thái nhỏ trên thẻ */
    .badge {
        background-color: #2b2b40;
        color: #a0a0c0;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Đọc dữ liệu từ file vocabulary.csv trên GitHub
@st.cache_data
def load_vocab():
  try:
    df = pd.read_csv(
        "vocabulary.csv", header=None, names=["Word", "Definition"]
    )
    df = df.dropna()
    return df.values.tolist()
  except Exception:
    return []


all_words = load_vocab()

if not all_words:
  st.error(
      "⚠️ Không tìm thấy file `vocabulary.csv` trên GitHub! T hãy kiểm tra lại"
      " nhé."
  )
else:
  # Tự động chia Set (mỗi Set 20 từ)
  chunk_size = 20
  batches = {}
  total_sets = math.ceil(len(all_words) / chunk_size)

  for i in range(total_sets):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, len(all_words))
    set_name = f"Set {i + 1} ({start_idx + 1} - {end_idx})"
    batches[set_name] = all_words[start_idx:end_idx]

  # Thanh chọn Set ở trên cùng
  selected_batch = st.selectbox(
      "📂 Chọn Flashcard Set:",
      list(batches.keys()),
      help="Chọn nhóm từ muốn ôn",
  )
  vocab_list = batches[selected_batch]

  # Khởi tạo session state
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

  word, definition = vocab_list[st.session_state.current_idx]
  current_num = st.session_state.current_idx + 1
  total_num = len(vocab_list)

  # Top bar: Tiến trình (Progress bar & số đếm)
  col_top1, col_top2, col_top3 = st.columns([1, 6, 1])
  with col_top1:
    if st.button("✕", use_container_width=True):
      st.session_state.current_idx = 0
      st.rerun()
  with col_top2:
    st.markdown(
        f"<p style='text-align: center; font-weight: bold; color: #ccc;"
        f" margin-top: 5px;'>{current_num} / {total_num}</p>",
        unsafe_allow_html=True,
    )
  with col_top3:
    st.markdown(
        "<p style='text-align: center; color: #ccc; cursor: pointer;'>⚙️</p>",
        unsafe_allow_html=True,
    )

  # Thanh progress ngang
  st.progress(current_num / total_num)
  st.markdown("<br>", unsafe_allow_html=True)

  # Giao diện thẻ Flashcard (Bấm vào thẻ hoặc nút để lật)
  card_container = st.container()
  with card_container:
    if not st.session_state.flipped:
      # Mặt trước: Hiện từ vựng
      st.markdown(
          f"""
            <div class="flashcard">
                <div class="badge">Từ mới</div>
                <div class="vocab-text">{word}</div>
                <div style="margin-top: 30px; color: #666; font-size: 14px;">(Chạm / Bấm nút bên dưới để lật nghĩa)</div>
            </div>
        """,
          unsafe_allow_html=True,
      )
    else:
      # Mặt sau: Hiện định nghĩa Anh - Anh
      st.markdown(
          f"""
            <div class="flashcard" style="background-color: #1a1a2e; border: 1px solid #3d3d66;">
                <div class="badge" style="background-color: #0f3460; color: #e94560;">Định nghĩa Anh - Anh</div>
                <div class="def-text">{definition}</div>
                <div style="margin-top: 20px; color: #888; font-size: 14px;">Từ: <b style="color: #fff;">{word}</b></div>
            </div>
        """,
          unsafe_allow_html=True,
      )

  # Nút lật thẻ trung gian nếu chưa lật
  if not st.session_state.flipped:
    if st.button("🔄 Lật xem nghĩa", use_container_width=True, type="primary"):
      st.session_state.flipped = True
      st.rerun()
  else:
    # 4 nút đánh giá chuẩn phong cách Anki / Quizlet y hệt ảnh mẫu
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

    # Dòng chữ nhỏ mô tả thời gian hẹn ôn tập ở dưới mỗi nút (giống hệt ảnh)
    st.markdown(
        """
        <table style="width: 100%; text-align: center; color: #888; font-size: 11px; margin-top: -10px;">
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
