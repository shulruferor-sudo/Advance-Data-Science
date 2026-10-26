FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm
# The inherited Yarn apt source is unused and has an unavailable signing key.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends texlive-xetex texlive-latex-extra texlive-pictures texlive-fonts-recommended lmodern \
    && rm -rf /var/lib/apt/lists/*
