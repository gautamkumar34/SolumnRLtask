# Pinned base image. For the final submission, pin by digest as well, e.g.
#   FROM python:3.12.7-slim-bookworm@sha256:<digest>
FROM python:3.12.7-slim-bookworm

# git for the tool/sample repo; tmux + procps are required by the terminus-2
# agent, which drives the container through a tmux session.
RUN apt-get update \
    && apt-get install -y --no-install-recommends git ca-certificates tmux procps \
    && rm -rf /var/lib/apt/lists/*

# Avoid "dubious ownership" warnings when the verifier (root) inspects a repo
# created at build time.
RUN git config --system --add safe.directory '*'

# Unprivileged user the agent runs as (matches [agent].user in task.toml).
RUN useradd -m -u 1000 agent

# Install the CLI (editable, so the agent's edits take effect immediately).
WORKDIR /app
COPY repo/ /app/
RUN pip install --no-cache-dir -e .
RUN chown -R agent:agent /app

# A deterministic sample repository the grader analyses. main has three
# commits; the newest is "Add login form". A feature/login branch exists too.
RUN set -eux; \
    mkdir -p /data/sample-repo; \
    cd /data/sample-repo; \
    git init -q -b main; \
    git config user.name "Ada Lovelace"; \
    git config user.email "ada@example.com"; \
    export GIT_AUTHOR_DATE="2024-01-01T10:00:00" GIT_COMMITTER_DATE="2024-01-01T10:00:00"; \
    echo "# project" > README.md; git add .; git commit -q -m "Initial commit"; \
    export GIT_AUTHOR_DATE="2024-01-02T10:00:00" GIT_COMMITTER_DATE="2024-01-02T10:00:00"; \
    echo "config" > config.txt; git add .; git commit -q -m "Add config"; \
    export GIT_AUTHOR_DATE="2024-01-03T10:00:00" GIT_COMMITTER_DATE="2024-01-03T10:00:00"; \
    echo "login" > login.py; git add .; git commit -q -m "Add login form"; \
    git branch feature/login

USER agent
