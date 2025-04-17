import re
import getpass  # To hide the password input

# 🔁 Extended Common Passwords List (Top 1000+ commonly used passwords for simplicity)
common_passwords = [
    "123456", "password", "123456789", "qwerty", "abc123", "football", "123123", "admin",
    "welcome", "monkey", "login", "passw0rd", "1234", "111111", "1q2w3e4r", "123qwe", "dragon",
    "sunshine", "letmein", "batman", "trustno1", "hello", "freedom", "whatever", "qazwsx",
    "mustang", "baseball", "superman", "iloveyou", "starwars", "shadow", "cheese", "696969",
    "snoopy", "flower", "matrix", "michelle", "ashley", "jordan", "pepper", "access",
    "donald", "pokemon", "winter2024", "hunter2", "tigger", "naruto", "cookie", "master",
    "12345", "letmein123", "123qwe", "qwertyuiop", "admin123", "1qaz2wsx", "football123",
    "sunshine123", "hello123", "superman123", "password1", "abc12345", "1qazxsw2", "letmein1",
    # Add other common passwords (or load from an external file for a bigger list)
]

# 🔍 Password Strength Logic
def check_strength(password, purpose, common_passwords):
    score = 0
    suggestions = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Digit
    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("Include numbers (0-9).")

    # Symbol
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        suggestions.append("Add special characters like @, #, $, etc.")

    # Repetition
    if not re.search(r'(.)\1\1', password):
        score += 1
    else:
        suggestions.append("Avoid repeated characters like 'aaa'.")

    # Common Password Check
    if password.lower() not in common_passwords:
        score += 2
    else:
        suggestions.append("Avoid common or leaked passwords.")

    # Purpose-sensitive bonus (for each platform)
    if purpose.lower() in ["banking", "finance", "email"]:
        if len(password) >= 16 and re.search(r'[A-Z]', password) and re.search(r'[^a-zA-Z0-9]', password):
            score += 1
        else:
            suggestions.append("Use at least 16 characters with special chars for critical accounts.")

    # Platform-Specific Suggestions
    platform_specific_suggestions(purpose, password, suggestions)

    # Final Decision
    complexity_score = score
    if complexity_score >= 8:
        strength = "🔒 Strong"
    elif complexity_score >= 5:
        strength = "🟡 Moderate"
    else:
        strength = "🔓 Weak"

    return strength, suggestions, complexity_score

def platform_specific_suggestions(purpose, password, suggestions):
    """ Add suggestions based on the platform """
    if purpose.lower() == "instagram":
        if len(password) < 12:
            suggestions.append("For Instagram, it's better to have at least 12 characters.")
        if not re.search(r'[A-Z]', password):
            suggestions.append("Instagram accounts benefit from having uppercase letters in the password.")

    if purpose.lower() == "youtube":
        if len(password) < 12:
            suggestions.append("YouTube accounts should have a minimum of 12 characters.")
        if not re.search(r'[^a-zA-Z0-9]', password):
            suggestions.append("Add a special character for YouTube to enhance security.")

    if purpose.lower() == "whatsapp":
        if len(password) < 10:
            suggestions.append("For WhatsApp, use at least 10 characters for better security.")
        if not re.search(r'[A-Z]', password):
            suggestions.append("Include at least one uppercase letter for WhatsApp.")

    if purpose.lower() == "snapchat":
        if len(password) < 12:
            suggestions.append("Snapchat accounts should have at least 12 characters.")
        if re.search(r'\s', password):
            suggestions.append("Avoid spaces in your Snapchat password.")

    if purpose.lower() == "social media":
        if len(password) < 10:
            suggestions.append("For general social media accounts, use at least 10 characters.")

# 🏁 Start Here
def main():
    print("\n🔐 Welcome to Advanced Password Strength Checker\n")

    print("🧭 What are you setting the password for?")
    print("1. Instagram")
    print("2. YouTube")
    print("3. WhatsApp")
    print("4. Snapchat")
    print("5. Social Media (General)")
    print("6. Email")
    print("7. Banking / Finance")
    print("8. Other")

    option = input("Enter choice (1-8): ").strip()

    purposes = {
        "1": "Instagram",
        "2": "YouTube",
        "3": "WhatsApp",
        "4": "Snapchat",
        "5": "Social Media",
        "6": "Email",
        "7": "Banking",
        "8": "Other"
    }

    purpose = purposes.get(option, "Other")

    # Ask user if they want to see the password
    show_password = input("\nDo you want to see the password as you type? (y/n): ").strip().lower()

    # Password input based on user preference
    if show_password == 'y':
        password = input(f"🔑 Enter the password for {purpose}: ").strip()
    else:
        password = getpass.getpass(f"🔑 Enter the password for {purpose}: ").strip()

    strength, suggestions, complexity_score = check_strength(password, purpose, common_passwords)

    print(f"\n🔎 Password Strength for {purpose}: {strength}\n")
    print(f"Complexity Score: {complexity_score}/10")
    if suggestions:
        print("💡 Suggestions to improve:")
        for tip in suggestions:
            print(f" - {tip}")
    else:
        print("✅ Your password looks great and secure!")

if __name__ == "__main__":
    main()
