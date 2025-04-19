FROM python:3.12.10-slim@sha256:82c07f2f6e35255b92eb16f38dbd22679d5e8fb523064138d7c6468e7bf0c15b

RUN useradd -m user

WORKDIR /app

COPY src/ src/
COPY app.py requirements.txt ./

RUN chown -R user:user /app

RUN apt-get update && apt-get install -y  --no-install-recommends curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip==25.0.1 \
    && pip install --no-cache-dir -r requirements.txt

USER user

EXPOSE 8888

ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:8888", "src:application"]

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8888/healthz || exit 1
