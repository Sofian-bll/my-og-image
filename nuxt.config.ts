export default defineNuxtConfig({
  compatibilityDate: '2026-06-06',

  modules: ['nuxt-og-image', '@nuxt/fonts'],

  site: {
    url: 'https://og.sofian.lab',
  },

  fonts: {
    families: [
      { name: 'Syne', weights: [400, 700], provider: 'google' },
    ],
  },

  ogImage: {
    renderer: 'takumi',
    defaults: {
      width: 1200,
      height: 630,
    },
  },
})
