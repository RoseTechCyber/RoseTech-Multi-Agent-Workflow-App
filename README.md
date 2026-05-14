# RoseTech-Multi-Agent-Workflow-App
A Windows‑native, locally designed **Multi‑Agent AI App** that demonstrates how multiple agents (Planner, Coder, Critic) can collaborate to handle tasks such as planning, coding, and reviewing.  
Built with **Streamlit** for an intuitive user interface and deployed publicly via Streamlit Community Cloud.

---

## 🚀 Live Demo
Try the app instantly:  
👉 [Rosetech Multi‑Agent Workflow App](https://rosetech-multi-agent-workflow-app-xxg638xxqdmqwd3yf3doj6.streamlit.app/)

---

## ✨ Features
- **Planner Agent**: Breaks down tasks into actionable steps.  
- **Coder Agent**: Generates Python code or workflow scripts.  
- **Critic Agent**: Reviews outputs for clarity, correctness, and improvements.  
- **Streamlit UI**: Simple text input and interactive results display.  
- **Windows‑friendly setup**: No need for Azure, Linux images, or Copilot Studio. Runs locally with CPU‑friendly models.

---

## 📂 Project Structure

multi_agent_demo/
│
├── app.py                # Streamlit UI
├── agents.py             # Agent definitions (Planner, Coder, Critic)
├── orchestrator.py       # Orchestrates agent workflow
├── requirements.txt      # Python dependencies
├── setup.bat             # One‑click  reset and setup script



---

## 🛠️ Installation (Local Setup)
1. Clone the repository:
   ```bash
   git clone https://github.com/RoseTechCyber/multi-agent-workflow-app.git
   cd multi-agent-workflow-app


2. Install dependencies:
  pip install -r requirements.txt

3. Run the app:
   streamlit run app.py
   
4.  Open your browser at http://localhost:8501.

5. Usage Examples
   -Run a calculator program → Agents collaborate to plan, code, and review.

   -Plan a weekend hackathon schedule → Planner outlines agenda, Coder suggests automation, Critic reviews feasibility.

   -Generate a recipe workflow → Planner structures steps, Coder drafts code, Critic checks clarity.


📸 Screenshots

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/97f5371d-944e-4d15-931b-68352dfc1e56" />


🛡️ Maintenance
Update requirements.txt when adding new libraries.

Push changes to GitHub → Streamlit Cloud redeploys automatically.

Use setup.bat to wipe and rebuild your environment if dependencies break.


👤 Author
Chinatu Uzuegbu  
GitHub: RoseTechCyber (github.com in Bing)  

✅ Conclusion
The RoseTech Multi‑Agent Workflow App showcases how organizations can leverage AI agents for varied business processes, all within a Windows‑friendly Streamlit interface.
Accessible locally (http://localhost:8501) or via the public Streamlit Cloud URL.
