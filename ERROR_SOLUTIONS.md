# 🔴 Error Messages & Solutions

Quick reference guide for common Render deployment errors.

---

## Build Phase Errors (During `pip install`)

### Error: `ERROR: Could not find a version that satisfies the requirement`

**Cause:** Wrong package name or version

**Fix:**
1. Check `requirements.txt` for typos
2. Remove problematic line
3. Run locally: `pip install -r requirements.txt`
4. If error, remove that line from requirements.txt
5. Push to GitHub
6. Render will retry automatically

**Example fix:**
```
❌ gunicorn==21.2.0.0  (too many digits)
✅ gunicorn==21.2.0    (correct)
```

---

### Error: `No module named 'flask'`

**Cause:** `requirements.txt` is missing or empty

**Fix:**
1. Verify `requirements.txt` exists in root folder
2. Should contain at minimum:
   ```
   Flask==3.0.0
   Flask-CORS==4.0.0
   gunicorn==21.2.0
   ```
3. Push to GitHub
4. Redeploy

---

### Error: `Python version X not available`

**Cause:** Requested Python version not supported

**Fix:**
1. Use Python 3.10 or 3.11 (latest supported)
2. In Render settings, select `Python 3` (auto-selects latest)
3. If manual needed: `python-3.11.0`
4. Restart deployment

---

## Deployment Phase Errors (During `gunicorn app:app`)

### Error: `ModuleNotFoundError: No module named 'app'`

**Cause:** `app.py` not in root directory

**Fix:**
1. Verify file structure:
   ```
   c:\Users\kavin\OneDrive\Documents\KAVIN\
   ├── app.py          ← Should be here
   └── templates\
   ```
2. If in subfolder, move to root
3. Procfile should say: `web: gunicorn app:app`
4. Push and retry

---

### Error: `TemplateNotFound: portal.html`

**Cause:** `templates/` folder not found or portal.html missing

**Fix:**
1. Check folder structure:
   ```
   ├── app.py
   ├── templates/         ← Must exist
   │   ├── portal.html    ← Must exist
   │   ├── admin_login.html
   │   └── admin_dashboard.html
   ```
2. Make sure folder is lowercase: `templates` (not Templates)
3. Make sure files are in the folder
4. Push to GitHub (all files)
5. Verify with: `git status`

---

### Error: `Address already in use: ('0.0.0.0', 5000)`

**Cause:** Port configuration issue

**Fix:**
- Already fixed in current `app.py`
- Check line: `port = int(os.environ.get('PORT', 5000))`
- Should use environment PORT variable ✅

---

### Error: `502 Bad Gateway` (Site loads then crashes)

**Cause:** App crashes after starting

**Fix:**
1. Check Render logs for actual error
2. Common causes:
   - Missing import in app.py
   - File write error (already fixed)
   - Database connection failed
3. Fix code locally first: `python app.py`
4. Test thoroughly before pushing
5. Check logs: Render Dashboard → Logs

---

## Runtime Errors (Site loads but features fail)

### Error: `CORS error: No 'Access-Control-Allow-Origin'`

**Cause:** Cross-origin request blocked

**Fix:**
- Already enabled: `CORS(app)` in app.py ✅
- Hard refresh browser: `Ctrl+Shift+R`
- Clear browser cache: Ctrl+Shift+Delete

---

### Error: `404 Not Found` on API call

**Cause:** Endpoint doesn't exist

**Fix:**
1. Check endpoint is defined in app.py
2. URL must match exactly
3. Method must match (GET vs POST)
4. Examples:
   ```
   @app.route('/api/analyze-wifi', methods=['GET'])
   @app.route('/api/admin-login', methods=['POST'])
   ```

---

### Error: `TypeError: can only concatenate str (not "NoneType") to str`

**Cause:** Null/None value being used

**Fix:**
1. Add None checks in code
2. Example fix:
   ```python
   # ❌ Bad
   name = data['name'] + " Smith"
   
   # ✅ Good
   name = (data.get('name') or '') + " Smith"
   ```
3. Test locally before pushing

---

### Error: `IOError: [Errno 2] No such file or directory`

**Cause:** File not found (static files, templates)

**Fix:**
1. Verify file paths are correct
2. Use absolute paths if needed
3. Check file exists on GitHub
4. Examples:
   ```
   ✅ /static/videos/file.mp4  (absolute)
   ❌ static/videos/file.mp4   (relative - may not work)
   ❌ ./static/videos/file.mp4 (relative - may not work)
   ```

---

## Service Issues (Won't Start or Stops)

### Error: `Service crashed` or `Failed to start service`

**Cause:** Multiple possibilities

**Fix:**
1. Check Render logs for exact error
2. Restart service: Dashboard → Restart button
3. Redeploy:
   - Make code change (add comment)
   - Commit: `git commit -m "Redeploy"`
   - Push: `git push`
4. Wait 2-3 minutes for redeployment

---

### Error: `Deployment timed out`

**Cause:** Build taking too long

**Fix:**
1. Check for large files slowing build
2. Remove unnecessary dependencies
3. Limit video file sizes
4. Try deploy again - may be temporary

---

## GitHub-Related Errors

### Error: `Authentication failed when pushing`

**Cause:** GitHub credentials not set

**Fix:**
```powershell
git config user.name "Your Name"
git config user.email "your@email.com"
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Then try push again:
```powershell
git push -u origin main
```

---

### Error: `fatal: 'origin' does not appear to be a 'git' repository`

**Cause:** Remote not configured

**Fix:**
```powershell
git remote add origin https://github.com/YOUR_USERNAME/WiFi-Security-Analyzer.git
git push -u origin main
```

---

### Error: `Permission denied (publickey)`

**Cause:** SSH key not set up

**Fix:**
Use HTTPS instead of SSH:
```powershell
git remote set-url origin https://github.com/YOUR_USERNAME/WiFi-Security-Analyzer.git
git push -u origin main
```

---

## Debugging Commands

### Check app locally
```powershell
cd c:\Users\kavin\OneDrive\Documents\KAVIN
python app.py
# Should show: Running on http://127.0.0.1:5000
```

### Check requirements
```powershell
cat requirements.txt
# Should show Flask, CORS, gunicorn
```

### Check file structure
```powershell
dir /s templates
dir /s static
# Should show template files and videos
```

### Check git status
```powershell
git status
# Should show: On branch main, nothing to commit
```

### Check latest commit
```powershell
git log --oneline -3
# Should show recent commits
```

---

## Quick Fix Checklist

If deployment fails:

1. [ ] Read error message carefully
2. [ ] Check Render logs for details
3. [ ] Run app locally: `python app.py`
4. [ ] Verify all files in GitHub: `git status`
5. [ ] Check `requirements.txt` has all dependencies
6. [ ] Verify folder structure is correct
7. [ ] Hard refresh browser (Ctrl+Shift+R)
8. [ ] Restart Render service (Dashboard → Restart)
9. [ ] Wait 5 minutes and try again
10. [ ] Check Render logs again

---

## When to Restart vs Redeploy

### Restart (Fast - 30 seconds)
```
Dashboard → Restart
```
Use when: Site is slow, or you want to restart process

### Redeploy (Slow - 2-3 minutes)
```
Make code change → git add . → git commit -m "msg" → git push
```
Use when: Changed code, dependencies, or configuration

---

## Getting Help

1. **Read the error message carefully** - Most are self-explanatory
2. **Check Render logs** - Real time error messages
3. **Test locally first** - `python app.py`
4. **Compare with working code** - Check GitHub for correct version
5. **Try restarting** - Often fixes temporary issues
6. **Contact Render support** - support@render.com

---

**Most errors have simple solutions. Check the logs and follow the fixes above! 🔧**
