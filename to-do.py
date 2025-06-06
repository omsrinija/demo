import streamlit as st

# Set page configuration
st.set_page_config(page_title="📝 To-Do App", layout="centered")

# Title
st.title("✅ To-Do List App")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add new task
new_task = st.text_input("➕ Add a new task:")
if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Please enter a task.")

# Display and manage tasks
st.subheader("📋 Your Tasks:")

# Display current tasks
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
        with col1:
            checked = st.checkbox("", value=task["done"], key=f"check_{i}")
            st.session_state.tasks[i]["done"] = checked
        with col2:
            task_text = task["task"]
            if task["done"]:
                st.markdown(f"~~{task_text}~~", unsafe_allow_html=True)
            else:
                st.write(task_text)
        with col3:
            if st.button("🗑️", key=f"del_{i}"):
                removed_task = st.session_state.tasks.pop(i)
                st.success(f"Deleted task: '{removed_task['task']}'")
                st.rerun()

else:
    st.info("You have no tasks yet. Add some!")

# Footer
st.markdown("---")
st.caption("Built by Om Srinija💙")
