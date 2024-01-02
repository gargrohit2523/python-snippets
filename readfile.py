from pathlib import Path

def CountWords():
    path = Path("c:\\txt\\brotherkarams.txt")
    contents = path.read_text(encoding='utf-8')
    print(len(contents))
    words = contents.split()
    print(len(words))

try:
    CountWords()
except FileNotFoundError:
    print("File Not Found")