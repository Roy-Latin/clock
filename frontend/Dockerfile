# Use the official Nginx image as base
FROM nginx:alpine

# Copy the frontend code into the container
COPY index.html /usr/share/nginx/html/app1/index.html

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf