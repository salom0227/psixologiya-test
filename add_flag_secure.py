import sys

path = sys.argv[1]
with open(path, "r") as f:
    c = f.read()

if "WindowManager" not in c:
    c = c.replace(
        "import com.getcapacitor.BridgeActivity;",
        "import com.getcapacitor.BridgeActivity;\nimport android.view.WindowManager;"
    )

if "FLAG_SECURE" not in c:
    c = c.replace(
        "super.onCreate(savedInstanceState);",
        "super.onCreate(savedInstanceState);\n        getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE);"
    )

with open(path, "w") as f:
    f.write(c)

print("Done:", path)
print("Check:")
for i, line in enumerate(c.split("\n")):
    if "FLAG_SECURE" in line or "WindowManager" in line:
        print(f"  {i+1}: {line}")
