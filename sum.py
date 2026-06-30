from transformers import pipeline

# Load summarization model (downloads on first run)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

print("=" * 50)
print("TEXT SUMMARIZATION TOOL")
print("=" * 50)

print("1. Enter text manually")
print("2. Read from a TXT file")

choice = input("\nChoose an option (1/2): ")

# ---------------------------
# Manual Text Input
# ---------------------------
if choice == "1":
    text = input("\nEnter your text:\n")

# ---------------------------
# TXT File Input
# ---------------------------
elif choice == "2":
    path = input("Enter TXT file path: ")

    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
    except Exception as e:
        print("Error:", e)
        exit()

else:
    print("Invalid choice!")
    exit()

# ---------------------------
# Check text length
# ---------------------------
if len(text.strip()) < 50:
    print("\nText is too short to summarize.")
    exit()

# ---------------------------
# Generate Summary
# ---------------------------
summary = summarizer(
    text,
    max_length=100,
    min_length=30,
    do_sample=False
)

print("\n" + "=" * 50)
print("ORIGINAL TEXT")
print("=" * 50)
print(text)

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print(summary[0]["summary_text"])
