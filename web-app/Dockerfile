FROM node:alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json
COPY yarn.lock /usr/src/app/yarn.lock

COPY . ./
ENV PATH /usr/src/app/node_modules/.bin:$PATH

RUN yarn

CMD ["yarn", "start"]
