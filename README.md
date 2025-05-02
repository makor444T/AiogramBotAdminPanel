# Telegram Bot Admin Panel

A Telegram bot built with `aiogram` and Finite State Machine (FSM) for managing posts and user roles through an admin panel.

## 📁 Project Structure

* `config/` — Environment variables and bot configuration
* `db_handlers/` — Database logic for posts and user roles
* `handlers/` — FSM logic and admin panel handlers
* `keyboards/` — Inline and reply keyboards
* `bot.py` — Entry point for bot startup

### Prerequisites

* Python 3.10+
* PostgreSQL
* A Telegram bot token from [BotFather](https://t.me/BotFather)

### 1. Clone the Repository

git clone https://github.com/makor444T/AiogramBotAdminPanel.git
cd your-repo-name

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Configure Environment Variables

Create a `.env` file in the `config/` directory using the provided `.env.example` as a template:

## 🛠 Tech Stack

* **Python**: 3.10+
* **aiogram**: 3.x
* **PostgreSQL**: Database for storing posts and roles

## ✨ Features

* Admin panel with role-based access control
* Create and delete posts via the bot
* FSM-based workflows for managing roles and content
