@echo off
echo ==========================================
echo Starting Elite Upwork Proposal Assistant
echo ==========================================

:: Start Backend
start cmd /k "python main.py"
echo Backend starting on http://localhost:8000...

:: Start Frontend
cd dashboard
start cmd /k "npm run dev"
echo Frontend starting on http://localhost:3000...

echo.
echo Please wait for Ollama to finish downloading models.
echo Access the dashboard at http://localhost:3000
echo.
pause
