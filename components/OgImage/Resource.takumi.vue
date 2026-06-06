<script setup lang="ts">
import { getTypeConfig, cleanArea } from '../../src/templates/colors'

const { title = 'Resource', area = 'Perso', subtitle } = defineProps<{
  title?: string
  area?: string
  subtitle?: string
}>()

const t = getTypeConfig('Resource')
const areaClean = cleanArea(area)
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: Inter, sans-serif;">
    <div
      class="absolute inset-0 opacity-30"
      :style="{
        background: `radial-gradient(ellipse 50% 60% at 30% 50%, ${t.from}33, transparent), radial-gradient(ellipse 50% 30% at 70% 70%, ${t.to}44, transparent), radial-gradient(ellipse 20% 20% at 50% 30%, ${t.accent}22, transparent)`,
      }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-20">
      <div class="flex justify-between items-start">
        <span
          class="inline-flex items-center gap-3 px-6 py-3 rounded-full text-2xl font-semibold"
          :style="{ background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
        >
          {{ t.emoji }} {{ t.label }}
        </span>
      </div>

      <div class="flex flex-col items-center gap-6" style="max-width: 1040px; margin: 0 auto;">
        <h1 class="text-white text-[72px] font-extrabold leading-tight text-center" style="letter-spacing: -0.02em;">
          {{ title }}
        </h1>
        <p
          v-if="subtitle"
          class="text-zinc-400 text-[32px] text-center"
          style="line-height: 1.4; letter-spacing: -0.01em;"
        >
          {{ subtitle }}
        </p>
      </div>

      <div class="flex justify-end text-zinc-500 text-[24px] font-medium">
        <span>{{ areaClean }}</span>
      </div>
    </div>
  </div>
</template>
