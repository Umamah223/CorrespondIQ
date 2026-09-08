# CorrespondIQ
AI-powered correspondence and calendar intelligence for extracting actionable insights from email communications and meeting context. It reads your emails and calendar to provide daily briefings.

[![Gemini](https://img.shields.io/badge/Gemini-3.6--Flash-orange.svg)](https://ai.google.dev/gemini-api)

## Overview

CorrespondIQ automatically connects to your Gmail and Google Calendar, analyzes your most important unread emails and upcoming meetings, and uses Google's Gemini AI to generate actionable briefings.

### Key Features

-  **Smart Email Fetching** – Retrieves your most important unread emails using Gmail's powerful search (`is:unread OR is:important`)
- **Calendar Awareness** – Pulls all meetings and events for the next 7 days
-  **Analysis** – Processes each email sender as a "client" and provides:
  - One‑sentence summary of the email thread
  - The single most important action item for you
  - Whether a meeting has been scheduled
-  **Daily Briefing** – Prints a clean, structured report directly in your terminal
- **Automation Ready** – Schedule it to run every morning (cron/Task Scheduler)


