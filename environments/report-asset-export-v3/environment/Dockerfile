# Pinned base image. For the final submission, pin by digest as well, e.g.
#   FROM python:3.12.7-slim-bookworm@sha256:<digest>
FROM python:3.12.7-slim-bookworm

# tmux + procps are required by the terminus-2 agent, which drives the
# container through a tmux session.
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates tmux procps \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 agent

# Install the CLI (editable, so the agent's edits take effect immediately).
WORKDIR /app
COPY repo/ /app/
RUN pip install --no-cache-dir -e .
RUN chown -R agent:agent /app

# Asset store the service serves, plus a secret that lives OUTSIDE the store.
# /data/reports        <- the storage root the service is meant to expose
# /data/secret         <- must never be reachable through an export path
RUN set -eux; \
    mkdir -p /data/reports/2024/q3 /data/secret; \
    echo "Company overview" > /data/reports/overview.txt; \
    echo "Q3 revenue up 12%" > /data/reports/2024/q3/summary.txt; \
    echo "SOLUMN_SECRET_TOKEN_do_not_leak" > /data/secret/api_key.txt; \
    chown -R agent:agent /data/reports; \
    chmod 0644 /data/secret/api_key.txt

USER agent
