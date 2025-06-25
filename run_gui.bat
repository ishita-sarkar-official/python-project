@echo off
echo.
echo Starting Binance Trading Bot GUI...

:: Activate the virtual environment
call venv\Scripts\activate

:: Run the GUI app
python gui\app.py

:: Pause after script ends
pause
