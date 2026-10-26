FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends texlive-xetex texlive-latex-extra texlive-pictures texlive-fonts-recommended lmodern && rm -rf /var/lib/apt/lists/*
