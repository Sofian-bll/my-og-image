export default defineNuxtConfig({
  compatibilityDate: '2026-06-06',

  modules: ['nuxt-og-image'],

  site: {
    url: 'https://og.sofian.lab',
  },

  ogImage: {
    renderer: 'takumi',
    defaults: {
      width: 1200,
      height: 630,
    },
  },
})
