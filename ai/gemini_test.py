import google.generativeai as genai

# === 1️⃣ SETUP ===
API_KEY = "AIzaSyC0PyYOfJLpGyMNQEzmjNKiLiPybhfUpBg"  # <-- Replace with your Gemini API key
genai.configure(api_key=API_KEY)

# === 2️⃣ CREATE MODEL ===
model = genai.GenerativeModel("gemini-2.5-flash")


# === 3️⃣ USER INPUT ===
prompt = input("Enter your prompt: ")

# === 4️⃣ GENERATE RESPONSE ===
response = model.generate_content(prompt)

# === 5️⃣ OUTPUT ===
print("\n🤖 Gemini's Response:")
print(response.text)
