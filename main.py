"""
GPA Calculator (Streamlit)
-----------------------------
Short, modular, and well-commented for workshop use.
Run: streamlit run main.py
"""

import streamlit as st
from typing import List, Dict, Tuple

# -----------------------------
# GPA Calculator (Streamlit)
# -----------------------------
# Short, modular, and well-commented for workshop use.
# Run: streamlit run main.py

# Letter grade to GPA points (4.0 scale)
GPA_MAP: Dict[str, float] = {
    "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "D-": 0.7,
    "F": 0.0,
}

def calculate_gpa(courses: List[Dict]) -> Tuple[float, float, float]:
    """Return (total_credits, total_points, gpa) for provided course rows.
    Each course dict: {name: str, credits: float, grade: str}
    """
    total_credits = 0.0
    total_points = 0.0
    for c in courses:
        try:
            credits = float(c.get("credits", 0) or 0)
        except ValueError:
            credits = 0.0
        grade = (c.get("grade") or "").strip()
        pts = GPA_MAP.get(grade, 0.0)
        total_credits += credits
        total_points += credits * pts
    gpa = (total_points / total_credits) if total_credits > 0 else 0.0
    return total_credits, total_points, gpa

def calculate_cumulative(current_gpa: float, current_credits: float,
                              prev_gpa: float, prev_credits: float) -> float:
    """Combine previous and current to get a cumulative GPA."""
    total_credits = max(current_credits, 0) + max(prev_credits, 0)
    if total_credits == 0:
        return 0.0
    total_points = current_gpa * max(current_credits, 0) + prev_gpa * max(prev_credits, 0)
    return total_points / total_credits

def init_state():
    """Initialize dynamic rows for courses in session_state."""
    if "courses" not in st.session_state:
        st.session_state.courses = [
            {"name": "Intro to CS", "credits": 3.0, "grade": "A"},
        ]
    if "recalc_trigger" not in st.session_state:
        st.session_state.recalc_trigger = 0

def add_course():
    st.session_state.courses.append({"name": "", "credits": 3.0, "grade": "B"})

def remove_course(index: int):
    if 0 <= index < len(st.session_state.courses):
        st.session_state.courses.pop(index)

def main():
    st.set_page_config(page_title="GPA Calculator", page_icon="📊", layout="centered")
    init_state()

    st.title("📊 GPA Calculator")
    st.caption("Quick prototype built with Streamlit · 4.0 scale")

    # --- Course Entry Table ---
    st.subheader("Courses")
    header_cols = st.columns([3, 1.2, 1.4, 0.9])
    header_cols[0].markdown("**Course Name**")
    header_cols[1].markdown("**Credits**")
    header_cols[2].markdown("**Letter Grade**")
    header_cols[3].markdown("**Remove**")

    grade_options = list(GPA_MAP.keys())

    for i, course in enumerate(st.session_state.courses):
        c1, c2, c3, c4 = st.columns([3, 1.2, 1.4, 0.9])
        course["name"] = c1.text_input("Course Name", value=course.get("name", ""), key=f"name_{i}")
        course["credits"] = c2.number_input("Credits", min_value=0.0, step=0.5, value=float(course.get("credits", 0) or 0), key=f"credits_{i}")
        course["grade"] = c3.selectbox("Grade", options=grade_options, index=max(0, grade_options.index(course.get("grade", grade_options[0])) if course.get("grade") in grade_options else 0), key=f"grade_{i}")
        c4.button("🗑️", key=f"remove_{i}", use_container_width=True, on_click=remove_course, args=(i,))

    bcols = st.columns([1, 1, 6])
    bcols[0].button("➕ Add Course", on_click=add_course, use_container_width=True)
    bcols[1].button("🔄 Recalculate", on_click=lambda: st.session_state.__setitem__("recalc_trigger", st.session_state.recalc_trigger + 1), use_container_width=True)

    # --- Calculations ---
    total_credits, total_points, gpa = calculate_gpa(st.session_state.courses)

    st.subheader("Results")
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Credits", f"{total_credits:.1f}")
    m2.metric("Total Grade Points", f"{total_points:.2f}")
    m3.metric("GPA", f"{gpa:.3f}")

    with st.expander("Optional: Add previous GPA to compute cumulative"):
        prev_c1, prev_c2 = st.columns(2)
        prev_gpa = prev_c1.number_input("Previous GPA", min_value=0.0, max_value=4.0, step=0.01, value=0.0)
        prev_credits = prev_c2.number_input("Previous Credits", min_value=0.0, step=0.5, value=0.0)
        if prev_gpa > 0 and prev_credits > 0:
            cumulative = calculate_cumulative(gpa, total_credits, prev_gpa, prev_credits)
            st.metric("Cumulative GPA", f"{cumulative:.3f}")

    st.markdown("---")
    st.markdown(
        """
        ### How GPA is computed
        - **Per-course points** = credits × grade points (A=4.0, A-=3.7, B+=3.3, ..., F=0.0).
        - **Total grade points** = sum of per-course points.
        - **GPA** = total grade points ÷ total credits.
        - **Cumulative GPA (optional)** combines your current term with a previous GPA and credits.
        """
    )

if __name__ == "__main__":
    main()
