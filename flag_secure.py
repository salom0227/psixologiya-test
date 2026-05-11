import sys, os
path = next((os.path.join(r,f) for r,d,fs in os.walk("android") for f in fs if f=="MainActivity.java"), None)
if not path: print("MainActivity topilmadi!"); exit(1)
with open(path) as f: c = f.read()
if "WindowManager" not in c:
    c = c.replace("import com.getcapacitor.BridgeActivity;", "import com.getcapacitor.BridgeActivity;\nimport android.view.WindowManager;")
if "FLAG_SECURE" not in c:
    c = c.replace("super.onCreate(savedInstanceState);", "super.onCreate(savedInstanceState);\n        getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE);")
with open(path, "w") as f: f.write(c)
print("FLAG_SECURE qoshildi:", path)
