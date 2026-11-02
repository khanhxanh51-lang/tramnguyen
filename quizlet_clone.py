import random
import streamlit as st

# Cấu hình trang web giao diện Dark Mode
st.set_page_config(
    page_title="IELTS Flashcard Pro", page_icon="📚", layout="centered"
)

# Custom CSS ép giao diện tối màu, bo góc chuẩn app mobile/flashcard cao cấp
st.markdown(
    """
    <style>
    .stApp {
        background-color: #12121f;
        color: #ffffff;
    }
    header {visibility: hidden;}
    
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

# Danh sách toàn bộ từ vựng tích hợp trực tiếp, chia theo Set chuẩn 20 từ
batches = {
    "Set 1 (Lô 18 - G, H, I, J, K...)": [
        ("gainsay", "(v.) deny or contradict a fact or statement."),
        ("galvanize", "(v.) shock or excite someone into taking action."),
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
        ("goad", "(v.) provoke or annoy someone to stimulate some action."),
        ("gouge", "(v.) make a groove, hole, or scuff with a sharp tool."),
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
    "Set 2 (Lô 19 - I, J, K, L, M...)": [
        (
            "idiosyncrasy",
            "(n.) a mode of behaviour or way of thought peculiar to an individual.",
        ),
        (
            "ignominious",
            "(adj.) deserving or causing public disgrace or shame.",
        ),
        ("immutable", "(adj.) unchanging over time or unable to be changed."),
        ("impartial", "(adj.) treating all rivals or disputants equally; fair."),
        (
            "impasse",
            (
                "(n.) a situation in which no progress is possible, especially"
                " because of disagreement."
            ),
        ),
        ("impecunious", "(adj.) having little or no money."),
        ("impediment", "(n.) a hindrance or obstruction in doing something."),
        (
            "imperious",
            "(adj.) assuming power or authority without justification; arrogant.",
        ),
        ("impetuous", "(adj.) acting or done quickly and without thought."),
        ("impudent", "(adj.) not showing due respect for another person."),
        (
            "inchoate",
            "(adj.) just begun and so not fully formed or developed.",
        ),
        (
            "incongruous",
            "(adj.) not in harmony or keeping with the surroundings.",
        ),
        ("indefatigable", "(adj.) persisting tirelessly."),
        ("indolent", "(adj.) wanting to avoid activity or exertion; lazy."),
        ("ineffable", "(adj.) too great or extreme to be expressed in words."),
        ("inert", "(adj.) lacking the ability or strength to move."),
        ("ingenuous", "(adj.) innocent and unsuspecting."),
        ("inimical", "(adj.) tending to obstruct or harm."),
        ("innocuous", "(adj.) not harmful or offensive."),
        ("insipid", "(adj.) lacking flavor; lacking vigor or interest."),
    ],
    "Set 3 (Lô 20 - M, N, O, P)": [
        (
            "malediction",
            (
                "(n.) a magical word or phrase uttered with the intention of"
                " bringing about evil; a curse."
            ),
        ),
        (
            "malleable",
            (
                "(adj.) able to be hammered or pressed out of shape without"
                " breaking."
            ),
        ),
        ("maverick", "(n.) an unorthodox or independent-minded person."),
        ("mendacious", "(adj.) not telling the truth; lying."),
        (
            "mercurial",
            "(adj.) subject to sudden or unpredictable changes of mood.",
        ),
        ("meticulous", "(adj.) showing great attention to detail; very careful."),
        (
            "misanthrope",
            "(n.) a person who dislikes humankind and avoids human society.",
        ),
        ("mitigate", "(v.) make less severe, serious, or painful."),
        ("mollify", "(v.) appease the anger or anxiety of someone."),
        ("mundane", "(adj.) lacking interest or excitement; dull."),
        ("nadir", "(n.) the lowest point in the fortunes of a person/org."),
        (
            "nascent",
            "(adj.) just coming into existence and beginning to display potential.",
        ),
        ("nefarious", "(adj.) wicked or criminal."),
        (
            "obdurate",
            "(adj.) stubbornly refusing to change one's opinion or course.",
        ),
        (
            "obsequious",
            "(adj.) obedient or attentive to an excessive or servile degree.",
        ),
        (
            "officious",
            (
                "(adj.) assertive of authority in a domineering way about"
                " trivial matters."
            ),
        ),
        (
            "onerous",
            "(adj.) involving an amount of effort that is oppressively burdensome.",
        ),
        (
            "ossify",
            "(v.) turn into bone; cease to develop and become rigid/fixed.",
        ),
        (
            "palliate",
            "(v.) make a disease or its symptoms less severe without removing cause.",
        ),
        (
            "paragon",
            "(n.) a person or thing regarded as a perfect example of quality.",
        ),
    ],
}

# Chọn Set từ vựng ở giao diện trên cùng
selected_batch = st.selectbox("📂 Chọn Flashcard Set:", list(batches.keys()))
vocab_list = batches[selected_batch]

# Khởi tạo session state cho từng Set
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

# Top bar: Nút đóng/reset, hiển thị số thứ tự từ
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
      "<p style='text-align: center; color: #ccc;'>⚙️</p>",
      unsafe_allow_html=True,
  )

# Thanh tiến trình ngang (Progress Bar)
st.progress(current_num / total_num)
st.markdown("<br>", unsafe_allow_html=True)

# Khung thẻ Flashcard Dark Mode
if not st.session_state.flipped:
  st.markdown(
      f"""
        <div class="flashcard">
            <div class="badge">Từ mới</div>
            <div class="vocab-text">{word}</div>
            <div style="margin-top: 30px; color: #666; font-size: 14px;">(Bấm nút bên dưới để lật nghĩa)</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
else:
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

# Nút lật thẻ hoặc 4 nút đánh giá thời gian
if not st.session_state.flipped:
  if st.button("🔄 Lật xem nghĩa", use_container_width=True, type="primary"):
    st.session_state.flipped = True
    st.rerun()
else:
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
