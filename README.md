# CI Sample Python Repository

This repository demonstrates a CI pipeline with GitHub Actions including:
- triggers: `push`, `pull_request`, and `workflow_dispatch`
- linting (flake8)
- static analysis (mypy)
- unit, integration, and acceptance tests (pytest markers)
- Docker image build and push to GitHub Container Registry (GHCR)
- Slack notifications
- creating a GitHub Issue on failure (example of bug-tracker integration)

Secrets expected (set in GitHub repo settings):
- `GHCR_PAT` - token with write:packages (or use GITHUB_TOKEN for public repos)
- `SLACK_WEBHOOK` - Slack Incoming Webhook URL
- `BUGTRACKER_TOKEN` - optional token for external bug tracker (demo uses GitHub Issues via GITHUB_TOKEN)

Repository layout:
```
├─ .github/workflows/ci.yml
├─ app/
│  └─ main.py
├─ tests/
│  ├─ test_unit.py
│  ├─ test_integration.py
│  └─ test_acceptance.py
├─ Dockerfile
├─ requirements.txt
├─ setup.cfg
└─ pyproject.toml
```
