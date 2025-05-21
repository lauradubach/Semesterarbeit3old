import os
import json

# Die Ordner mit Markdown-Dateien
CONTENT_DIRS = ["Sites", "Sprints"]
INDEX = []

for dir_name in CONTENT_DIRS:
    for filename in os.listdir(dir_name):
        if filename.endswith(".md"):
            filepath = os.path.join(dir_name, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Erste Zeile als Titel, sonst Dateiname
            title = filename.replace(".md", "")
            lines = content.strip().splitlines()
            if lines and lines[0].startswith("#"):
                title = lines[0].lstrip("#").strip()

            INDEX.append({
                "title": title,
                "url": f"{dir_name}/{filename.replace('.md', '.html')}",
                "content": content.replace("\n", " ")[:1000]  # Optional kürzen
            })

# Speichern als JSON
with open("search-index.json", "w", encoding="utf-8") as f:
    json.dump(INDEX, f, indent=2, ensure_ascii=False)

print("✅ search-index.json wurde erstellt.")