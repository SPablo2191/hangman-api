# Use the official Python image as a parent image
FROM python:3.9

# Set the working directory to /
WORKDIR /

# Copy the requirements file into the container at /requirements/
COPY ./dev.txt /requirements/dev.txt

# Install any needed packages specified in requirements/dev.txt
RUN pip install --no-cache-dir --upgrade -r /requirements/dev.txt

# Copy the contents of the local src directory to the working directory in the container
COPY ./src /src

# Set the default command to run when the container starts
CMD ["uvicorn", "src.app.app:app", "--host", "0.0.0.0", "--port", "80"]
