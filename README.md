# AetherOS – Living AI Startup Ecosystem

## Tech Stack
- **Frontend**: Next.js 15 (App Router), Tailwind, shadcn/ui, Vercel AI SDK (optional)
- **Backend**: Python 3.12+, FastAPI, LangGraph (or CrewAI/AutoGen), SQLModel/Supabase
- **Agents**: LangGraph graphs + custom prompts
- **Database/Memory**: Supabase (Postgres + pgvector) or Pinecone
- **Payments**: PayFast/PayShap + Stripe
- **Deployment**: User-owned Netlify/Render/Vercel free tier (autonomous via API)
- **Hosting this repo**: Vercel (frontend), Railway/Fly.io/Render (backend)

## Quick Start (Local Dev)
1. Clone repo
2. `cd frontend && pnpm install && pnpm dev`
3. `cd ../backend && poetry install && poetry run uvicorn app.main:app --reload`
4. Visit http://localhost:3000
