@echo off
REM WiFi Security Analyzer - Launch Script for Windows
REM This script installs dependencies and runs the application

echo.
echo ================================
echo WiFi Security Analyzer
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [OK] Python is installed
echo.

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not installed
    pause
    exit /b 1
)

echo [OK] pip is installed
echo.

REM Install requirements if not already installed
echo Checking dependencies...
pip list | find /I "Flask" >nul
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install packages
        pause
        exit /b 1
    )
    echo [OK] Packages installed successfully
) else (
    echo [OK] All packages are already installed
)

echo.
echo ================================
echo Starting WiFi Security Analyzer
echo ================================
echo.
echo Access the application at:
echo http://127.0.0.1:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
