FROM python:3.9

COPY . .
RUN pip install streamlit

CMD ["python3", "main.py"]
