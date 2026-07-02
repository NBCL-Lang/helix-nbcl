import requests
from pathlib import Path

print("What would you like to do?")
print()
print("[1] Copy queries over")
print("[2] Add nbcl to languages.toml")
print("[3] Both")
print()

method = 0
while method not in {1, 2, 3}:
    n_str = input("> ")
    try:
        n = int(n_str)
        method = n
    except ValueError:
        print("Please pass a valid number.")

def copy_queries():
    files = ["folds.scm", "highlights.scm", "indents.scm"]
    base = "https://raw.githubusercontent.com/NBCL-Lang/tree-sitter-nbcl/refs/heads/main/queries/"

    home_dir = Path.home()
    output_dir = home_dir / ".config/helix/runtime/queries/nbcl"
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Downloading queries...")
    for file in files:
        url = base + file
        response = requests.get(url)
        file_path = output_dir / file

        with open(file_path, "wb") as write_file:
            write_file.write(response.content)
            print(f"Wrote {file} to {file_path}")

def add_nbcl():
    local_langs = Path("languages.toml")
    output_file = Path.home() / ".config/helix/languages.toml"
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    content = local_langs.read_text(encoding="utf-8")
    
    with output_file.open("a", encoding="utf-8") as file:
        file.write(content)
        print(f"Appended nbcl language settings to {output_file}")

match method:
    case 1:
        copy_queries()
    case 2:
        add_nbcl()
    case 3:
        copy_queries()
        add_nbcl()

