# 🔧 Troubleshooting Render Deployment Issues

## Common Problems & Solutions

### ❌ Problem 1: "Build Failed" Error

**Symptoms:** Deployment stops at build stage with red error message

**Solutions:**

1. **Check Render Logs:**
   - Go to your Render dashboard
   - Click on your service
   - Open "Logs" tab
   - Look for error messages

2. **Common Build Errors:**

   **Error:** `ImportError: No module named 'flask'`
   - **Cause:** Missing `requirements.txt`
   - **Fix:** Make sure `requirements.txt` exists in root folder
   - **Check:** Run `pip freeze > requirements.txt` locally

   **Error:** `ModuleNotFoundError`
   - **Cause:** Missing dependency
   - **Fix:** Add to `requirements.txt` and push

   **Error:** `Python version mismatch`
   - **Cause:** Wrong Python version specified
   - **Fix:** Use Python 3.11 (default on Render)

---

### ❌ Problem 2: "Build Successful but Site Won't Load"

**Symptoms:** Deploy succeeds, but site returns error or blank page

**Solutions:**

1. **Check Render Logs:**
   ```
   Dashboard → Logs → Filter by "error"
   ```

2. **Common Runtime Errors:**

   **Error:** `TemplateNotFound: portal.html`
   - **Cause:** Templates folder not found
   - **Fix:** Ensure `templates/` folder exists with `portal.html`
   - **Verify:** All template files in correct location

   **Error:** `StaticFileNotFound`
   - **Cause:** Static files not in right place
   - **Fix:** Ensure `static/` folder exists with videos
   - **Check:** Path should be `/static/videos/...`

   **Error:** `Address already in use`
   - **Cause:** Port configuration issue
   - **Fix:** Already fixed in app.py (uses PORT env var)

---

### ❌ Problem 3: "Site Loads but Nothing Works"

**Symptoms:** Page loads but buttons, forms, or features don't work

**Solutions:**

1. **Check Browser Console:**
   - Open your site
   - Press `F12` (Developer Tools)
   - Go to "Console" tab
   - Look for red error messages

2. **Common JavaScript Errors:**

   **Error:** `CORS error`
   - **Cause:** Cross-origin request blocked
   - **Fix:** Already enabled in app.py with Flask-CORS
   - **Check:** Reload page (Ctrl+Shift+R)

   **Error:** `404 on /api/...`
   - **Cause:** API endpoint not found
   - **Fix:** Check endpoint is properly defined in app.py
   - **Solution:** Make sure latest code was pushed to GitHub

   **Error:** `Cannot read property of undefined`
   - **Cause:** JavaScript error in portal.html
   - **Fix:** Check for syntax errors in code

---

### ❌ Problem 4: "Videos Not Loading"

**Symptoms:** Video section shows but videos don't play

**Solutions:**

1. **Check Video Files:**
   ```
   static/videos/ should contain:
   - how-to-use.mp4
   - wifi-security.mp4
   - threat-detection.mp4
   - domain-safety.mp4
   ```

2. **Fix Video Paths:**
   - Use absolute paths: `/static/videos/filename.mp4`
   - Not relative paths: `static/videos/...`
   - Already correct in current code ✅

3. **If Videos Still Don't Load:**
   - Check Render Logs for file errors
   - Verify video files are in GitHub repo
   - Ensure files committed (not ignored)

---

### ❌ Problem 5: "Admin Login Not Working"

**Symptoms:** Admin login page loads but credentials fail

**Solutions:**

1. **Check Credentials:**
   - Username: `admin`
   - Password: `admin123`
   - Both are case-sensitive

2. **Debug in Console (F12):**
   - Go to Network tab
   - Click login button
   - Check if `/api/admin-login` returns 200
   - Look for response data

3. **If Endpoint Not Found:**
   - Make sure admin login route is in app.py
   - Check: `@app.route('/api/admin-login', methods=['POST'])`

---

## 🔍 Step-by-Step Debugging

### 1. **Check Render Dashboard:**
   - Is service "Active" (green)?
   - Are there error logs?
   - Is the URL accessible?

### 2. **Check GitHub:**
   - Are all files pushed?
   - Run: `git status` (should show clean)
   - Try: `git log` (see recent commits)

### 3. **Test Locally First:**
   ```powershell
   cd c:\Users\kavin\OneDrive\Documents\KAVIN
   python app.py
   # Visit http://localhost:5000
   ```
   - Does it work locally?
   - If yes: Deploy issue
   - If no: Code issue

### 4. **Check App Configuration:**
   - `app.py` uses `host='0.0.0.0'` ✅
   - `app.py` uses PORT env var ✅
   - `Procfile` has correct start command ✅
   - `requirements.txt` has all dependencies ✅

---

## 🚀 Fixed Version Checklist

Your app should now have:

- ✅ Error handling for file operations
- ✅ Correct port configuration (0.0.0.0)
- ✅ Environment variable support for PORT
- ✅ Debug mode disabled (debug=False)
- ✅ CORS enabled for all routes
- ✅ Proper static file paths
- ✅ Template directory configured

---

## 📝 Redeployment Steps

If you made changes:

1. **Commit changes locally:**
   ```powershell
   git add .
   git commit -m "Fix: Render deployment issues"
   ```

2. **Push to GitHub:**
   ```powershell
   git push origin main
   ```

3. **Render auto-deploys:**
   - Goes to dashboard
   - Shows "Deploy in progress"
   - Waits 2-3 minutes
   - Shows "Deploy succeeded"

---

## 💡 Pro Tips

### Tip 1: Enable Render Logs Monitoring
- Dashboard → Logs
- Auto-refresh every 5 seconds
- Watch as app deploys

### Tip 2: Hard Refresh in Browser
- Chrome: `Ctrl+Shift+R`
- Firefox: `Ctrl+Shift+R`
- Safari: `Cmd+Shift+R`
- Clears cache and reloads fresh

### Tip 3: Check Build Command
- Render dashboard → Settings
- Verify Build Command: `pip install -r requirements.txt`
- Verify Start Command: `gunicorn app:app`

### Tip 4: Use Render's Log Viewer
- Real-time error messages
- Shows exact line causing issue
- Super helpful for debugging

---

## 🆘 If Still Not Working

### Option A: Check GitHub Repo
```powershell
# Make sure you're in the right folder
cd c:\Users\kavin\OneDrive\Documents\KAVIN

# Verify files exist
ls -la templates/
ls -la static/
ls -la

# Check if pushed to GitHub
git log --oneline -5
```

### Option B: Test Locally
```powershell
# Run app locally to ensure code works
python app.py

# Visit http://localhost:5000
# Test all features
# Check browser console for errors
```

### Option C: Manual Redeploy on Render
1. Go to Render Dashboard
2. Click your service
3. Click "Restart" button
4. Wait for redeployment

### Option D: Check Environment
- Make sure Python 3.11 selected
- Make sure Region is correct
- Make sure Branch is "main"
- Make sure Plan is "Free"

---

## 📊 Health Check

Your deployment is working if:

| Feature | Check | Status |
|---------|-------|--------|
| **Home Page Loads** | Visit URL, see WiFi analyzer | ✅ Should work |
| **Network Analysis** | Click "Analyze WiFi" button | ✅ Shows demo data |
| **Domain Checker** | Enter a domain, check safety | ✅ Should work |
| **Admin Login** | Use admin/admin123 | ✅ Should work |
| **Videos** | Click video tutorial | ✅ Should play |
| **Nearby Networks** | View networks list | ✅ Shows demo networks |
| **Security Modal** | Click security button | ✅ Should show modal |

---

## 📞 Getting More Help

1. **Render Support:**
   - https://render.com/docs
   - Contact: support@render.com

2. **Check These Docs:**
   - Flask: https://flask.palletsprojects.com
   - Gunicorn: https://docs.gunicorn.org
   - Render: https://render.com/docs/getting-started

3. **Verify Your Files:**
   - All files in GitHub repo
   - Run: `git push` to update
   - Check Render logs after push

---

## ✅ Quick Fixes Checklist

- [ ] Checked Render logs for errors
- [ ] Verified all files in GitHub
- [ ] Hard refreshed browser (Ctrl+Shift+R)
- [ ] Tested app locally
- [ ] Confirmed credentials (admin/admin123)
- [ ] Checked portal.html in templates/
- [ ] Verified static/videos/ exists
- [ ] Confirmed requirements.txt has dependencies
- [ ] Made sure Procfile is correct
- [ ] Restarted service from Render dashboard

---

**Your app should now work on Render! 🎉**

If issues persist, check the logs section above with specific error messages.
