
import streamlit as st
import pandas as pd

# Initialize session state to store assignments
if "assignments" not in st.session_state:
    st.session_state.assignments = []

# Sample lists (replace with your real data)
tasks = ["Fix login bug", "Update homepage UI", "Write blog post", "Database backup"]
users = ["Alice", "Bob", "Charlie", "Dana"]

st.set_page_config(page_title="Task Assignment Dashboard")
st.title("📋 Task Assignment Dashboard")

# Dropdown for task and user
selected_task = st.selectbox("Select a Task", tasks)
selected_user = st.selectbox("Assign to User", users)

# Assign button
if st.button("Assign Task"):
    st.session_state.assignments.append({"Task": selected_task, "Assigned To": selected_user})
    st.success(f"✅ Task '{selected_task}' assigned to {selected_user}.")

# Display assigned tasks
if st.session_state.assignments:
    st.subheader("📌 Assigned Tasks")
    df = pd.DataFrame(st.session_state.assignments)
    st.dataframe(df, use_container_width=True)
