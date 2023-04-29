FROM node:9-slim
WORKDIR /main

COPY package*.json ./

RUN npm install

COPY . /main

EXPOSE 8080

CMD ["npm", "start"]