# The image you are going to inherit your Dockerfile from
FROM python:3.8
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1
# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /django_recipe_api
# Set the /django_recipe_api directory as the working directory
WORKDIR /django_recipe_api
# Copies from your local machine's current directory to the django_recipe_api folder 
# in the Docker image
COPY . /django_recipe_api
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
# Install the requirements.txt file in Docker image
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000"]


