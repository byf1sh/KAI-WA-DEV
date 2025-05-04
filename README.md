# 📥 WhatsApp Fetcher

**WhatsApp Fetcher** is an application that automatically fetches new messages from WhatsApp and stores them in an Excel file on OneDrive using the Microsoft Graph API. It allows users to select which chat rooms to monitor, and every new incoming message in the selected chat will be fetched and saved in real-time.

## ✨ Features

- ✅ Automatically detects and fetches new WhatsApp messages.
- ✅ Users can select which chat rooms to monitor.
- ✅ Fetched messages are stored directly into an Excel file on OneDrive.
- ✅ Seamless integration with Microsoft Graph API.
- ✅ Ideal for conversation documentation, monitoring, and data backup.

## 🚀 How It Works

1. The app logs in to WhatsApp Web.
2. The user selects the desired chat room(s) to monitor.
3. The app listens for new incoming messages.
4. New messages are automatically fetched and formatted.
5. The message data is pushed to an Excel file on OneDrive via the Graph API.

## 🧩 Requirements

- A Microsoft account with Graph API access.
- A valid Microsoft Graph API access token.
- An active WhatsApp account that can log in via WhatsApp Web.

## 🔧 Installation

```bash
git clone https://github.com/byf1sh/KAI-WA-DEV.git
cd whatsapp-fetcher
pip install -r requirements.txt
