FROM python:3.9-slim
WORKDIR /app

COPY cloud1.py  /app/
COPY random_paragraphs.txt /app/

RUN pip install nltk
ENV NLTK_DATA /usr/local/share/nltk_data

RUN python -c "import nltk; nltk.download('stopwords')"
EXPOSE 80

ENV NAME dockerfile
CMD ["python", "cloud1.py"]