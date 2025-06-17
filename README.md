# ⏱️whatsapp-challenge-project
## 📌 Description

This was a challenge I had with my friends that was whoever wrote the first message in our groupchat at exactly 12:00 midnight, wins.
I used my coding skills to automate this process (That might have been cheating😂)

## 💡 What It Does

- Monitors the current time continuously.
- When the time reaches **00:00:00**, **00:00:01**, or **23:59:59**, it:
  - Types `"First"` automatically.
  - Presses the **Enter** key.
  - Prints `"Done"` in the terminal for confirmation.

---

## ▶️ How to Use
- Open the chat, post, or comment section where you want to type "First".
- Run the script: python challenge_crusher.py
- Do not move the mouse or type on the keyboard — pyautogui takes over at the scheduled time.
- Leave it running. When it's exactly midnight or one second after, it will type "First" and press Enter.
