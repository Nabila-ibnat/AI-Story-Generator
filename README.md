# AI Story Generator API

A FastAPI service that takes a one-line prompt and returns a complete, AI-generated short story using an OpenAI model. Fully containerized with Docker.

## Project Overview

This API accepts a short text prompt (e.g. *"A lonely robot discovers a hidden forest."*), sends it to an OpenAI model wrapped in a story-writing instruction, and returns a structured JSON response containing the generated story.

**Tech stack:**
- Python 3.11
- FastAPI
- OpenAI API
- Docker / Docker Compose
- Pydantic (request/response validation)

## Project Structure

```text
ai-story-generator/
│
├── app/
│   ├── main.py
│   ├── Story/
│   │   ├── story.py
│   │   ├── openai_service.py
│   │   └── story_schema.py
│   ├── core/
│   │   └── config.py
│   └── utils/
│       └── prompt_template.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Installation Guide (Local, without Docker)

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-story-generator.git
   cd ai-story-generator
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** (see below)

5. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

6. Visit:
   - API root: http://127.0.0.1:8000
   - Swagger docs: http://127.0.0.1:8000/docs

## Environment Setup

Copy `.env.example` to `.env` and fill in your OpenAI API key:

```bash
cp .env.example .env
```

```env
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-5-mini
```

> Get your API key from the [OpenAI Platform](https://platform.openai.com/) under **Dashboard → API Keys**.

## Docker Setup

1. Make sure Docker Desktop is running.
2. Make sure your `.env` file is created (see above).
3. Build and start the container:
   ```bash
   docker compose up --build
   ```
4. Visit http://localhost:8000/docs

To stop the container:
```bash
docker compose down
```

## API Usage

### Endpoint

```
POST /api/v1/story/generate
```

### Example Request

```json
{
  "prompt": "A lonely robot discovers a hidden forest."
}
```

### Example Response

```json
{
  "success": true,
  "story": "Once upon a time, in a distant future, a lonely robot wandered across abandoned cities..."
}
```

### Example with curl

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/story/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A dragon becomes best friends with a village child."}'
```

## Notes

- The `MODEL_NAME` environment variable controls which OpenAI model is used (e.g. `gpt-5` or `gpt-5-mini`).
- `.env` is excluded from version control via `.gitignore` — never commit real API keys. Use `.env.example` as the template.
