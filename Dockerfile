 FROM python:3.9
 LABEL maintainer="Faith Kovi"
 RUN mkdir -p /app
 WORKDIR /app
 COPY ./ /app
 RUN pip -r requirements.txt
 EXPOSE 5000
 CMD [ "python", "app,py" ]
