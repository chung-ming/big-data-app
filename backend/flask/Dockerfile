FROM python:3.9.2-alpine

# Upgrade pip
RUN pip install --upgrade pip

# Get curl for healthchecks
RUN apk add curl

# Create a non-root user
RUN adduser -D nonroot

# Create necessary directories and set permissions
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app


# Switch to the non-root user
USER nonroot

# Set the working directory
WORKDIR /home/app

# copy all the files to the container
COPY --chown=nonroot:nonroot . .

# Set up a virtual environment
ENV VIRTUAL_ENV=/home/app/venv
RUN python3.9 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py

# Install Python dependencies
RUN pip install -r requirements.txt

# Define the port number the container should expose
EXPOSE 8000

# Set the entry point to run the Flask app
CMD ["python", "app.py"]