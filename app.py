import time
import random

def magical_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)  # thoda delay for effect
    print()

def main():
    stars = "✨" * 20
    magical_print(stars)
    magical_print("🚀 Welcome to the world of GitHub Actions!")
    magical_print("🔮 Running Python script with a touch of magic...")
    magical_print("✅ Everything is working perfectly!")
    magical_print(stars)

    # Thoda extra magic: random fortune
    fortunes = [
        "🌟 Great things are coming your way!",
        "💡 Keep learning, success is near!",
        "🔥 Your DevOps + SRE journey will shine!",
        "🚀 Today is the best day to start something new!"
    ]
    magical_print(random.choice(fortunes))

if __name__ == "__main__":
    main()
