# Backlogz
Backlog application for games! 

# Developer Setup

How to get Backlogz (backend + frontend) running on your machine.

## Prerequisites

- **Git**
- **Python 3.12 or newer** (check with `python --version`)
- **Setup nvm. Use this link - https://www.nvmnode.com/guide/download.html. nvm version, nvm install lts, nvm use lts, node -v, npm -v. If all that works, great!** (check with `node --version`) 
- **Poetry 2.x** (installed in step 1)

## 1. Install Poetry

We use [pipx](https://pipx.pypa.io/) to install Poetry. It keeps Poetry in its own isolated environment and sets up your PATH.

**Windows (PowerShell):**

```powershell
python -m pip install --user pipx
python -m pipx ensurepath
```

**macOS / Linux:**

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

**Close and reopen your terminal** (PATH changes only apply to new sessions), then:

```bash
pipx install poetry
poetry --version    # should print 2.x
```

If `poetry` or `pipx` is "not recognized" after reopening the terminal, the `ensurepath` step didn't take effect. Re-run it and restart your terminal again.

## 2. Clone the repo

```bash
git clone <repo-url>
cd <repo-folder>
```

## 3. Backend

```bash
cd backend
poetry config virtualenvs.in-project true   # keeps the .venv folder inside backend/
poetry install
```

`poetry install` reads `poetry.lock`, so everyone gets the exact same dependency versions. Never edit `poetry.lock` by hand.

Verify:

```bash
poetry run pytest                              # should show 1 passed
poetry run uvicorn app.main:app --reload       # starts the API
```

- http://localhost:8000/health returns `{"status": "ok"}`
- http://localhost:8000/docs is the auto-generated API explorer (Swagger UI)

## 4. Frontend

In a second terminal, from the repo root:

```bash
cd frontend
npm ci
npm run dev
```

Open http://localhost:5173. You should see the app load.

`npm ci` installs exactly what `package-lock.json` says (the npm equivalent of `poetry install` with a lock file). Use `npm install <package>` only when you are deliberately adding a new dependency.

## Everyday commands

**Backend** (run from `backend/`):

| Task | Command |
|------|---------|
| Run tests | `poetry run pytest` |
| Start dev server | `poetry run uvicorn app.main:app --reload` |
| Lint | `poetry run ruff check .` |
| Add a dependency | `poetry add <package>` |
| Add a dev-only dependency | `poetry add --group dev <package>` |

**Frontend** (run from `frontend/`):

| Task | Command |
|------|---------|
| Start dev server | `npm run dev` |
| Type-check and build | `npm run build` |
| Add a UI component | `npx shadcn@latest add <component>` |
| Add a dependency | `npm install <package>` |

After pulling changes that touch `poetry.lock` or `package-lock.json`, run `poetry install` or `npm ci` again.

shadcn is already configured (`components.json` is committed), so you do **not** need to run `shadcn init`.

## Git workflow

- Never push directly to `main`.
- Work on your own branch, for example `feature/game-model`.
- Open a pull request into `main` and get one approval from the other person before merging.
- Commit lock files (`poetry.lock`, `package-lock.json`). Never commit `.env` files or AWS credentials.

## Troubleshooting

- **`poetry: command not found`**: see step 1, then restart your terminal.
- **Build or wheel errors during `poetry install` on Python 3.14**: some packages lag behind new Python releases. Try Python 3.13 and tell the team.
- **`Attribute "app" not found in module "app.main"`**: you are running the command from the wrong folder (it must be run from `backend/`), or `app/main.py` is empty or unsaved.
- **Red squiggle on `@/components/...` imports in VS Code but the app runs**: restart the TypeScript server (Ctrl+Shift+P, then "TypeScript: Restart TS Server").