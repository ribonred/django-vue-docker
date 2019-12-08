FROM nikolaik/python-nodejs:python3.7-nodejs10
ENV PYTHONUNBUFFERED 1
WORKDIR /laundry
COPY ./laundry /laundry
RUN pip install -r requirements.txt
RUN npm install
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# RUN python manage.py collectstatic