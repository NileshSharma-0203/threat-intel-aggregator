#!/bin/bash
source venv/bin/activate
echo "🕷️  Starting crawler..."
python -m scrapers.tor_browser_selenium &
sleep 5
echo "📊  Launching dashboard at http://localhost:5000"
python dashboard/app.py
