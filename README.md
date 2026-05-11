# 📚 TestBase — Psixologiya & Falsafa

621 ta savol-javob | Offline | Screenshot himoyali | Android APK

## 🚀 GitHub ga push qilish

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/psixologiya-test.git
git push -u origin main
```

Push qilgandan so'ng GitHub Actions avtomatik:
1. ✅ GitHub Pages ga deploy qiladi (web versiya)
2. ✅ APK build qiladi
3. ✅ Releases ga APK joylashtiradi

## 📥 APK yuklab olish
`Releases` bo'limidan `app-debug.apk` ni yuklab oling.

## ⚙️ GitHub sozlamalari

### Pages yoqish:
`Settings → Pages → Source → GitHub Actions`

### Actions ruxsati:
`Settings → Actions → General → Workflow permissions → Read and write`

## 🔒 Xususiyatlar
- **Offline** — bir marta ochilsa internet kerak emas
- **Screenshot** — `FLAG_SECURE` (Android native) + CSS/JS himoya
- **Barcha Android** — minSdk 21 (Android 5+)
