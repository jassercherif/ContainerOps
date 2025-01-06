FROM node:22

WORKDIR /app

COPY package*.json ./
RUN npm install 

COPY . .

# Change ownership to node user
RUN chown -R node:node /app

# Build the React app (if needed)
# RUN npm run build 

ENV PORT=3000

EXPOSE ${PORT}

USER node

ENV NODE_OPTIONS=--openssl-legacy-provider


CMD ["npm", "start"]