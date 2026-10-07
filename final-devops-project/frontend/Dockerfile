# Production Dockerfile for Frontend Node.js Service
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies (zero-dependency or express)
RUN npm install --production

# Copy application source
COPY . .

# Expose frontend port
EXPOSE 3000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/ || exit 1

# Start the Node server
CMD ["node", "server.js"]
