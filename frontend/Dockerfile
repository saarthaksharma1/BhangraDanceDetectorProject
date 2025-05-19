# 1. Use official Node image
FROM node:18

# 2. Set working directory
WORKDIR /app

# 3. Copy dependencies and install
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# 4. Copy rest of the app
COPY . .

# 5. Expose dev server port
EXPOSE 3000

# 6. Start the React dev server
CMD ["npm", "start"]
