FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 先複製 requirements 並安裝依賴（此時還是 root）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# 建立非 root user
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# 複製專案程式碼
COPY --chown=appuser:appuser . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
