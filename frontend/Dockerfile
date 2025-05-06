# Etapa base para instalar dependencias
FROM node:18-alpine AS base
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install

# Etapa de desarrollo
FROM base AS dev
COPY . .
CMD ["npm", "run", "dev"]

# Etapa de construcción para producción
FROM base AS builder
COPY . .
RUN npm run build

# Etapa final para producción con nginx
FROM nginx:alpine AS prod
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]