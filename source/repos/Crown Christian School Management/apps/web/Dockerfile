FROM node:20-alpine AS build
WORKDIR /app
COPY package.json pnpm-lock.yaml* ./
RUN corepack enable && corepack prepare pnpm@9.0.0 --activate && pnpm install --frozen-lockfile
COPY . .
RUN pnpm build

FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE80
CMD ["nginx", "-g", "daemon off;"]
