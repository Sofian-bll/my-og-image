<script setup lang="ts">
const props = defineProps<{
  title?: string
  subtitle?: string
}>()

const title = props.title || 'Sofian OS'
</script>

<template>
  <div class="h-full w-full flex flex-col justify-center items-center p-20 bg-gradient-to-br from-[#0d1117] to-[#161b22]">
    <div class="w-24 h-1 bg-[#58a6ff] rounded-full mb-8" />
    <h1
      class="text-white text-7xl font-bold text-center leading-tight"
      style="max-width: 1000px; word-break: break-word"
    >
      {{ title }}
    </h1>
    <p
      v-if="subtitle"
      class="text-[#8b949e] text-4xl mt-6 text-center"
      style="max-width: 900px; word-break: break-word"
    >
      {{ subtitle }}
    </p>
    <div class="absolute bottom-10 right-10 text-[#8b949e] text-2xl">
      sofian.lab
    </div>
  </div>
</template>
