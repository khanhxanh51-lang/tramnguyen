import streamlit as st

# Cấu hình trang web
st.set_page_config(
    page_title="IELTS Vocabulary - Flashcard Sets",
    page_icon="📚",
    layout="centered",
)

# Custom CSS giao diện Flashcard
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
        font-size: 38px;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 10px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("📚 Ôn Tập Từ Vựng IELTS - Flashcard Sets")
st.markdown(
    "Hệ thống flashcard chia thành các Set 20 từ chuẩn Anh - Anh, ôn tập trực"
    " quan."
)
st.markdown("---")

# Danh sách phân chia theo các Set bắt đầu từ Set 1
batches = {
    "Set 1 (G, H, I, J, K...)": [
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
            "(adj.) denoting a period of time in the past that was idyllically"
            " happy.",
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
    "Set 2 (I, J, K, L, M...)": [
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
    "Set 3 (M, N, O, P)": [
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
    "Set 4 (P, Q, R, S)": [
        (
            "parsimonious",
            "(adj.) unwilling to spend money or use resources; stingy.",
        ),
        (
            "pedantic",
            (
                "(adj.) excessively concerned with minor details and rules or"
                " displaying learning."
            ),
        ),
        ("penury", "(n.) extreme poverty; destitution."),
        ("perfidious", "(adj.) deceitful and untrustworthy."),
        (
            "perfunctory",
            "(adj.) carried out with a minimum of effort or reflection.",
        ),
        ("permeate", "(v.) spread throughout something; pervade."),
        (
            "perspicacious",
            "(adj.) having a ready insight into and understanding of things.",
        ),
        (
            "phlegmatic",
            "(adj.) having an unemotional and stolidly calm disposition.",
        ),
        ("placate", "(v.) make someone less angry or hostile."),
        (
            "plasticity",
            "(n.) adaptability of an organism to changes in environment.",
        ),
        ("polemic", "(n.) a strong verbal or written attack on someone."),
        (
            "pragmatic",
            "(adj.) dealing with things sensibly based on practical considerations.",
        ),
        (
            "precipitate",
            "(v.) cause a bad situation to happen suddenly or unexpectedly.",
        ),
        ("prevaricate", "(v.) speak or act in an evasive way."),
        (
            "prodigal",
            "(adj.) spending money or resources freely and recklessly.",
        ),
        ("proliferate", "(v.) increase rapidly in numbers; multiply."),
        ("propitiate", "(v.) win or regain the favor of a god/person by pleasing."),
        (
            "propriety",
            "(n.) state of conforming to conventionally accepted standards.",
        ),
        ("pugnacious", "(adj.) eager or quick to argue, quarrel, or fight."),
        (
            "quell",
            "(v.) put an end to a rebellion or disorder, typically by force.",
        ),
    ],
    "Set 5 (R, S, T, U, V)": [
        (
            "recalcitrant",
            "(adj.) having an uncooperative attitude toward authority.",
        ),
        ("recondite", "(adj.) little known; abstruse (of a subject)."),
        ("redoubtable", "(adj.) formidable, especially as an opponent."),
        ("refractory", "(adj.) stubborn or unmanageable."),
        ("reprobate", "(n.) an unprincipled person."),
        ("repudiate", "(v.) refuse to accept or be associated with."),
        ("rescind", "(v.) revoke, cancel, or repeal a law, order, agreement."),
        ("reticent", "(adj.) not revealing one's thoughts or feelings readily."),
        ("rife", "(adj.) of common occurrence; widespread."),
        (
            "sagacious",
            "(adj.) having keen mental discernment and good judgment; wise.",
        ),
        ("salubrious", "(adj.) health-giving; healthy."),
        (
            "sanguine",
            "(adj.) optimistic or positive, especially in a difficult situation.",
        ),
        ("sardonic", "(adj.) grimly mocking or cynical."),
        ("scathing", "(adj.) witheringly scornful; severely critical."),
        ("solicitous", "(adj.) characterized by or showing interest or concern."),
        ("soporific", "(adj.) inducing drowsiness or sleep."),
        ("specious", "(adj.) superficially plausible, but actually wrong."),
        (
            "stolid",
            "(adj.) calm, dependable, and showing little emotion or animation.",
        ),
        (
            "surreptitious",
            "(adj.) kept secret, especially because it would not be approved.",
        ),
        ("sycophant", "(n.) a person acting obsequiously to gain advantage."),
    ],
    "Set 6 (T, U, V, W, Z)": [
        (
            "taciturn",
            "(adj.) reserved or uncommunicative in speech; saying little.",
        ),
        ("tantamount", "(adj.) equivalent in seriousness to; virtually the same."),
        ("temerity", "(n.) excessive confidence or boldness; audacity."),
        ("tirade", "(n.) a long, angry speech of criticism or accusation."),
        ("torpor", "(n.) a state of physical or mental inactivity; lethargy."),
        ("tractable", "(adj.) easy to control or influence."),
        (
            "truculent",
            "(adj.) eager or quick to argue or fight; aggressively defiant.",
        ),
        ("ubiquitous", "(adj.) present, appearing, or found everywhere."),
        ("umbrage", "(n.) offense or annoyance."),
        (
            "unctuous",
            "(adj.) excessively or ingratiatingly flattering; oily.",
        ),
        (
            "uxorious",
            "(adj.) having or showing excessive fondness for one's wife.",
        ),
        (
            "vacillate",
            "(v.) alternate or waver between opinions; be indecisive.",
        ),
        ("venerate", "(v.) regard with great respect; revere."),
        ("veracity", "(n.) conformity to facts; accuracy."),
        ("verbose", "(adj.) using or expressed in more words than needed."),
        ("vilify", "(v.) speak or write about in an abusively disparaging manner."),
        ("virulent", "(adj.) extremely severe or harmful in its effects."),
        ("vociferous", "(adj.) vehement or clamorous."),
        ("wanton", "(adj.) deliberate and unprovoked (of cruel action)."),
        ("zealot", "(n.) a person fanatical and uncompromising in ideals."),
    ],
    "Set 7 (Tổng hợp A-Z - Lần 1)": [
        ("alacrity", "(n.) brisk and cheerful readiness."),
        ("cacophony", "(n.) a harsh, discordant mixture of sounds."),
        (
            "debacle",
            "(n.) a sudden and ignominious failure; a fiasco / (adj.) fearless.",
        ),
        ("ebullient", "(adj.) cheerful and full of energy."),
        (
            "facetious",
            "(adj.) treating serious issues with deliberately inappropriate humor.",
        ),
        ("gainsay", "(v.) deny or contradict a fact or statement."),
        ("hackneyed", "(adj.) lacking significance through having been overused."),
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
            "(adj.) stubbornly refusing to change one's opinion or course.",
        ),
        ("palliate", "(v.) make a disease or its symptoms less severe."),
        ("quixotic", "(adj.) exceedingly idealistic; unrealistic and impractical."),
        (
            "recalcitrant",
            "(adj.) having an uncooperative attitude toward authority.",
        ),
        (
            "sagacious",
            "(adj.) having or showing keen mental discernment and good judgment.",
        ),
        ("taciturn", "(adj.) reserved or uncommunicative in speech."),
        ("ubiquitous", "(adj.) present, appearing, or found everywhere."),
    ],
    "Set 8 (Tổng hợp A-Z - Lần 2)": [
        (
            "acerbic",
            "(adj.) sharp and forthright; expressing harsh or sharp criticism.",
        ),
        ("bellicose", "(adj.) demonstrating aggression and willingness to fight."),
        (
            "capricious",
            "(adj.) given to sudden and unaccountable changes of mood.",
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
        ("kinetic", "(adj.) relating to or resulting from motion."),
        (
            "labyrinthine",
            "(adj.) like a labyrinth; irregular and twisting (of a network).",
        ),
        ("mendacious", "(adj.) not telling the truth; lying."),
        ("nadir", "(n.) the lowest point in the fortunes of a person/org."),
        (
            "obsequious",
            "(adj.) obedient or attentive to an excessive or servile degree.",
        ),
        ("paradigm", "(n.) a typical example or pattern of something; a model."),
        ("querulous", "(adj.) complaining in a petulant or whining manner."),
        (
            "recalcitrant",
            "(adj.) having an uncooperative attitude toward authority.",
        ),
        ("sycophant", "(n.) a person acting obsequiously to gain advantage."),
        (
            "truculent",
            "(adj.) eager or quick to argue or fight; aggressively defiant.",
        ),
    ],
}

# Chọn Set từ vựng
selected_batch = st.selectbox(
    "📂 Chọn Flashcard Set muốn ôn tập:", list(batches.keys())
)
vocab_list = batches[selected_batch]

# Khởi tạo trạng thái phiên làm việc theo từng Set
if (
    "current_idx" not in st.session_state
    or "last_batch" not in st.session_state
    or st.session_state.last_batch != selected_batch
):
  st.session_state.current_idx = 0
  st.session_state.last_batch = selected_batch
  st.session_state.show_def = False

if st.session_state.current_idx >= len(vocab_list):
  st.session_state.current_idx = 0

word, definition = vocab_list[st.session_state.current_idx]

# Hiển thị vị trí từ trong Set
st.caption(
    f"Đang học: **{selected_batch}** | Thẻ từ số:"
    f" **{st.session_state.current_idx + 1} / {len(vocab_list)}**"
)

# Khung thẻ từ vựng lớn
st.markdown(
    f"""
    <div class="vocab-card">
        <div style="font-size: 13px; color: #888; margin-bottom: 5px; text-transform: uppercase;">IELTS Flashcard</div>
        <div class="vocab-word">{word}</div>
    </div>
""",
    unsafe_allow_html=True,
)

# Hiển thị định nghĩa khi lật
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

# Hàng nút điều hướng (Trước / Lật nghĩa / Tiếp theo)
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

# Nút đánh giá mức độ (Chưa thuộc / Đã thuộc)
if st.session_state.show_def:
  st.markdown("---")
  st.markdown(
      "<p style='text-align: center; font-weight: bold; color: #555;'>Đánh giá"
      " từ này của tớ:</p>",
      unsafe_allow_html=True,
  )
  d_col1, d_col2 = st.columns(2)
  with d_col1:
    if st.button("🔴 Chưa thuộc (Khó)", use_container_width=True):
      st.session_state.current_idx = (
          st.session_state.current_idx + 1
      ) % len(vocab_list)
      st.session_state.show_def = False
      st.rerun()
  with d_col2:
    if st.button("🟢 Đã thuộc (Dễ)", use_container_width=True):
      st.session_state.current_idx = (
          st.session_state.current_idx + 1
      ) % len(vocab_list)
      st.session_state.show_def = False
      st.rerun()
