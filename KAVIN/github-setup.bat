@echo off
REM WiFi Security Analyzer - GitHub Push Script

echo.
echo ============================================
echo WiFi Security Analyzer - Deploy to GitHub
echo ============================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [1/4] Initializing Git repository...
git init

echo [2/4] Configuring Git user...
git config user.name "WiFi Analyzer Developer"
git config user.email "developer@wifisecurity.local"

echo [3/4] Adding all files...
git add .

echo [4/4] Creating initial commit...
git commit -m "WiFi Security Analyzer - Ready for Render deployment"

echo.
echo ============================================
echo NEXT STEPS:
echo ============================================
echo.
echo 1. Go to GitHub: https://github.com/new
echo 2. Create a new repository named: WiFi-Security-Analyzer
echo 3. Copy the HTTPS URL (looks like: https://github.com/YOUR_USERNAME/WiFi-Security-Analyzer.git)
echo 4. Run this command:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/WiFi-Security-Analyzer.git
echo    git push -u origin main
echo.
echo 5. Then go to Render.com and connect your GitHub repo
echo.
pause
