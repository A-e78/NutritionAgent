# Nutrition AI Agent - Replit Environment Setup

## Overview
This is a full-stack nutrition recommendation application that uses evolutionary algorithms (Genetic Algorithm and Simulated Annealing) to generate personalized nutritional recommendations.

**Tech Stack:**
- Backend: Python FastAPI (port 8000)
- Frontend: React (port 5000)
- Algorithms: Genetic Algorithm, Simulated Annealing

## Project Structure
```
nutrition-ai-agent/
├── backend/                 # Python FastAPI backend
│   ├── algorithms/          # GA and Simulated Annealing implementations
│   ├── api/                 # API routes
│   ├── models/              # Pydantic data models
│   ├── services/            # Business logic
│   └── main.py              # FastAPI application entry point
├── frontend/                # React frontend
│   ├── src/                 # React components and logic
│   ├── public/              # Static assets
│   └── .env                 # Frontend environment config (port 5000)
└── replit.md                # This file
```

## Current Setup Status

### Installed Dependencies
- **Python 3.11** with packages:
  - fastapi
  - uvicorn
  - pandas
  - numpy
  - pydantic

- **Node.js 20** with packages:
  - react
  - react-dom
  - react-scripts
  - web-vitals
  - @testing-library packages

### Configuration
- Frontend configured to run on **port 5000** with host **0.0.0.0**
- Backend configured to run on **port 8000** with host **0.0.0.0** (required for Replit proxy)
- CORS enabled on backend to allow frontend requests
- React development server configured to bypass host header verification (required for Replit proxy)

### Active Workflows
- **frontend**: Runs `cd frontend && npm start` on port 5000 (webview)
  - This is the main user-facing application
  - Accessible through Replit's webview
- **backend**: Runs `cd backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000` (console)
  - FastAPI backend server
  - Both workflows start automatically when the Repl runs

## API Endpoints
Base URL (development): The backend is available on port 8000

Available endpoints:
- `GET /diet/foods` - List all foods
- `GET /diet/foods/filter` - Filter foods
- `POST /diet/requirements` - Submit user requirements
- `POST /diet/generate` - Generate personalized nutrition plan

## Recent Changes (Nov 1, 2025)
- Initialized project from GitHub import
- Created missing frontend package.json
- Installed all Python and Node.js dependencies
- Configured React to run on port 5000 with proper host settings
- Set up frontend workflow for Replit environment
- Configured backend for port 8000

## Development Notes
- The frontend is served through Replit's proxy in an iframe, so host verification bypass is essential
- Frontend automatically restarts when code changes are detected
- Backend needs manual restart when code changes are made
- Python virtual environment is managed by Replit's `.pythonlibs/` directory
