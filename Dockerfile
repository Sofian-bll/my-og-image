FROM node:22-alpine AS build

WORKDIR /app

COPY package.json bun.lock ./

RUN apk add --no-cache bash curl unzip && curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:$PATH"

RUN bun install --frozen-lockfile

COPY . .

RUN npx nuxi build

FROM node:22-alpine AS runtime

WORKDIR /app

COPY --from=build /app/.output .output

EXPOSE 3000

ENV NITRO_HOST=0.0.0.0
ENV NITRO_PORT=3000
ENV NODE_ENV=production

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget -qO- http://localhost:3000/api/og/default?title=health || exit 1

CMD ["node", ".output/server/index.mjs"]
