from pathlib import Path

required = [
    "README.md", "src", "tests",
    "results", "figures", "requirements.txt",
]
missing = [name for name in required
           if not Path(name).exists()]
print("ready" if not missing else missing)
