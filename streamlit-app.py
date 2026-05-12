import streamlit as st
from orchestrator import run_workflow

st.title("🧩 RoseTech-Multi-Agent AI Workflow App (Windows Local)")

user_request = st.text_input("Enter a task for the agents:")

if st.button("Run Agents"):
    if user_request.strip():
        st.write("Running workflow...")
        results = run_workflow(user_request)
        st.success("Workflow complete!")

        st.subheader("Planner Output")
        st.write(results["Plan"])

        st.subheader("Coder Output")
        st.code(results["Code"], language="python")

        st.subheader("Critic Output")
        st.write(results["Review"])
    else:
        st.warning("Please enter a task first.")
