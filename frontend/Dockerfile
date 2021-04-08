FROM node:12.18.0-alpine as build 
#also say 
WORKDIR /app
#copy the react app to the container
COPY . /app/ 

# #prepare the container for building react 
RUN npm install --silent
RUN npm run build 

#prepare nginx
FROM nginx:1.17.2-alpine

COPY --from=build /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

#fire up nginx
# EXPOSE 80 # uncomment in development 
CMD ["nginx","-g","daemon off;"]