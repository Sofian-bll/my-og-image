export default defineNuxtConfig({
  compatibilityDate: '2026-06-06',

  modules: ['nuxt-og-image'],

  site: {
    url: 'https://og.sofian.lab',
  },

  ogImage: {
    renderer: 'takumi',
    fonts: [
      { name: 'Syne', weights: [400, 700, 800], provider: 'google' },
    ],
    defaults: {
      width: 1200,
      height: 630,
    },
  },
})
