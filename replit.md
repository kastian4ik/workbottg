# Telegram Welcome Bot

## Overview
This is a Telegram bot that automatically welcomes new members when they join a Telegram group. The bot is written in Python using the pyTelegramBotAPI library and includes a Flask web server for health checks.

## Project Structure
- `bot.py` - Main bot script with welcome message logic and Flask health check server
- `requirements.txt` - Python dependencies (pyTelegramBotAPI, Flask)
- `Procfile` - Process configuration (for deployment)
- `.gitignore` - Git ignore file for Python projects
- `replit.md` - Project documentation

## Setup
The bot requires a Telegram Bot Token to function. This token should be stored in an environment variable called `TELEGRAM_BOT_TOKEN`.

### How to Get a Telegram Bot Token
1. Open Telegram and search for @BotFather
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the token provided by BotFather
5. Add it to the Secrets tab in Replit with the key `TELEGRAM_BOT_TOKEN`

## Features
- Welcomes new members to Telegram groups with a custom message in Ukrainian
- Tracks known members to avoid duplicate welcomes
- Automatic chat_id detection for supergroups
- Error handling with auto-restart on polling failures
- Flask health check endpoint for uptime monitoring (UptimeRobot compatible)

## Architecture
The bot runs two components in parallel:
1. **Telegram Bot** - Runs in a separate thread, polls for new messages
2. **Flask Web Server** - Runs on port 8080, provides health check endpoint at `/`

## Running the Bot
The bot runs continuously:
1. Flask server starts on 0.0.0.0:8080 (health checks)
2. Telegram polling runs in a background thread
3. Monitors for new chat members
4. Sends welcome messages to new members
5. Auto-restarts on errors

## Technical Details
- Language: Python 3.11
- Main Libraries: 
  - pyTelegramBotAPI 4.13.0
  - Flask 2.3.3
- Deployment: Runs as a worker process with embedded web server

## Recent Changes
- 2025-10-27: Initial setup in Replit environment
- Added Flask health check server on port 8080
- Implemented auto-restart mechanism for polling errors
- Added chat_id detection handler
- Configured workflow for continuous bot execution
- Installed all required dependencies
