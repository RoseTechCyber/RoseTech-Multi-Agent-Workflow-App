@echo off
REM ============================================================
REM RoseTech Multi-Agent-Workflow-app  Setup Script for Windows
REM ============================================================
echo Deleting old virtual environment...
rmdir /s /q venv

echo Creating  new virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing dependencies...
pip install -r requirements.txt

echo Launching Streamlit app...
streamlit run app.py

REM ============================================================
REM End of script
REM ============================================================
