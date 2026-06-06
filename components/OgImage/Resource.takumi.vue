<script setup lang="ts">
const props = defineProps<{
  title?: string
  area?: string
  subtitle?: string
  bg?: string
}>()

const title = props.title || 'Sofian OS'
const area = props.area || 'Resource'
const bg = props.bg || '#0d1117'
</script>

<template>
  <div
    :style="{ backgroundColor: bg }"
    class="h-full w-full flex flex-col justify-center items-center p-20"
  >
    <span class="text-[#58a6ff] text-3xl font-medium tracking-wide uppercase">
      {{ area }}
    </span>
    <h1
      class="text-white text-7xl font-bold mt-6 text-center leading-tight"
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
  </div>
</template>
