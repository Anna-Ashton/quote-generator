import pandas as pd
import random

# Load quotes
df = pd.read_csv("quotes.csv")

def get_quote(mood):
    mood = mood.strip().lower()
    matches = df[df['mood'].str.lower() == mood]
    
    if not matches.empty:
        return random.choice(matches['quote'].tolist())
    else:
        return "Sorry, I don't have a quote for that mood yet. But you're still awesome!"

if __name__ == "__main__":
    mood = input("How are you feeling? ")
    quote = get_quote(mood)
    print("\nHere's your quote:")
    print(f"💬 {quote}")
