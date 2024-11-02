FROM python:3.9

COPY . .
RUN pip install streamlit pandas

CMD ["python3", "main.py"]
