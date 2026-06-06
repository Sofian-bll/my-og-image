<script setup lang="ts">
import { getTypeConfig, cleanArea } from '../../src/templates/colors'

const { title = 'Aspiration', area = 'Perso', description } = defineProps<{
  title?: string
  area?: string
  description?: string
}>()

const t = getTypeConfig('Aspiration')
const areaClean = cleanArea(area)
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: Inter, sans-serif;">
    <div
      class="absolute inset-0 opacity-20"
      :style="{
        background: `radial-gradient(ellipse 60% 50% at 50% 50%, ${t.from}22, transparent), radial-gradient(ellipse 40% 30% at 70% 40%, ${t.to}33, transparent), radial-gradient(ellipse 30% 40% at 30% 60%, ${t.accent}18, transparent)`,
      }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-20">
      <span
        class="inline-flex items-center gap-3 px-6 py-3 rounded-full text-2xl font-semibold self-start"
        :style="{ background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
      >
        {{ t.emoji }} {{ t.label }}
      </span>

      <div class="flex flex-col items-center gap-8" style="max-width: 1040px; margin: 0 auto;">
        <h1 class="text-white text-[64px] font-extrabold leading-tight text-center" style="letter-spacing: -0.02em;">
          {{ title }}
        </h1>
        <p
          v-if="description"
          class="text-[28px] text-center"
          style="line-height: 1.5; max-width: 900px;"
          :style="{ color: t.accent, opacity: 0.7 }"
        >
          {{ description }}
        </p>
      </div>

      <div class="flex justify-end text-zinc-500 text-[24px] font-medium">
        <span>{{ areaClean }}</span>
      </div>
    </div>
  </div>
</template>
