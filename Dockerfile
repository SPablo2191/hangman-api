# 
FROM python:3.9

# 
WORKDIR /

# 
COPY ./dev.txt /requirements/dev.txt

# 
RUN pip install --no-cache-dir --upgrade -r /requirements/dev.txt

# 
COPY ./app /src/app

# 
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
