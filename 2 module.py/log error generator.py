from pathlib import Path

print("\nTry This: Log ERROR generator")
print("=" * 50)

def error_lines(path: str):
    # Using a generator (yield) is much better for large logs than loading the whole file
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if "ERROR" in line:
                yield line.rstrip("\n")

# Setup the demo file if it doesn't exist
demo = Path("./demo.log")
if not demo.exists():
    demo.write_text("""INFO start
WARNING low disk
ERROR failed to open file
INFO done
""")

# Iterate through the generator
for e in error_lines(str(demo)):
    print(e)