FROM python:3.8.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

# RUN sh -c "$(curl -sSfL https://release.solana.com/v1.10.23/install)"
# RUN export PATH="/root/.local/share/solana/install/active_release/bin:$PATH"
# RUN ln ~/.local/share/solana/install/active_release/bin/spl-token /bin

# COPY requirements.txt .
# RUN pip install -r requirements.txt

COPY . .