




Documentation
1. Virtual Environment
The script creates a local Python environment (venv) so dependencies don’t interfere with your global Python install.

2. Dependencies
Installs everything listed in requirements.txt:

streamlit → UI

transformers + torch → Local AI models

3. Activation
Activates the virtual environment before installing packages.

4. Launch
Runs streamlit run app.py to open the demo in your browser.



🚀 How to Use
Place setup.bat in your project folder.

Double‑click setup.bat.

The script will:

Create a virtual environment.

Install dependencies.

Launch the Streamlit app.

Your browser will open with the Multi‑Agent Demo UI.





✅ Result
No manual typing needed.

Works entirely on Windows, locally.

Agents (Planner, Coder, Critic) collaborate via the Streamlit interface.