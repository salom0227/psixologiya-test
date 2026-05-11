import os

def patch_main_activity():
    target_file = None
    # Android loyihasidan MainActivity faylini qidirish (Java yoki Kotlin)
    for root, dirs, files in os.walk("android"):
        for file in files:
            if file in ["MainActivity.java", "MainActivity.kt"]:
                target_file = os.path.join(root, file)
                break
        if target_file: break

    if not target_file:
        print("XATO: MainActivity fayli topilmadi!")
        return False

    with open(target_file, "r") as f:
        content = f.read()

    # Agar allaqachon himoya qo'shilgan bo'lsa, to'xtatamiz
    if "FLAG_SECURE" in content:
        print("HIMOYA: Skrinshot himoyasi allaqachon mavjud.")
        return True

    is_kotlin = target_file.endswith(".kt")
    
    print(f"Himoya qo'shilmoqda: {target_file}")

    if is_kotlin:
        # Kotlin uchun himoya kodi
        if "android.view.WindowManager" not in content:
            content = content.replace("import com.getcapacitor.BridgeActivity", 
                                    "import android.view.WindowManager\nimport com.getcapacitor.BridgeActivity")
        
        if "override fun onCreate" in content:
            content = content.replace("super.onCreate(savedInstanceState)", 
                                    "super.onCreate(savedInstanceState)\n        window.setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE)")
        else:
            content = content.replace("class MainActivity : BridgeActivity() {", 
                                    "class MainActivity : BridgeActivity() {\n    override fun onCreate(savedInstanceState: android.os.Bundle?) {\n        super.onCreate(savedInstanceState)\n        window.setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE)\n    }")
    else:
        # Java uchun himoya kodi
        if "import android.view.WindowManager;" not in content:
            content = content.replace("import com.getcapacitor.BridgeActivity;", 
                                    "import android.view.WindowManager;\nimport com.getcapacitor.BridgeActivity;")
        
        if "onCreate" in content:
            content = content.replace("super.onCreate(savedInstanceState);", 
                                    "super.onCreate(savedInstanceState);\n        getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE);")
        else:
            content = content.replace("public class MainActivity extends BridgeActivity {", 
                                    "public class MainActivity extends BridgeActivity {\n    @Override\n    public void onCreate(android.os.Bundle savedInstanceState) {\n        super.onCreate(savedInstanceState);\n        getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE);\n    }")

    with open(target_file, "w") as f:
        f.write(content)
    
    print("MUVAFFAQIYATLI: Skrinshot himoyasi o'rnatildi!")
    return True

if __name__ == "__main__":
    patch_main_activity()
