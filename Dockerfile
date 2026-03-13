# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all repo files into container
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 7860

# Run Streamlit app
CMD streamlit run app.py --server.port $PORT --server.enableCORS false
