<script setup lang="ts">
import { getTypeConfig, cleanArea } from '../../src/templates/colors'

const { title = 'Sofian OS', area, subtitle } = defineProps<{
  title?: string
  area?: string
  subtitle?: string
}>()

const t = getTypeConfig('SystemConfig')
const areaClean = area ? cleanArea(area) : ''
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: Inter, sans-serif;">
    <div
      class="absolute inset-0 opacity-20"
      :style="{
        background: `radial-gradient(ellipse 50% 50% at 50% 50%, ${t.from}33, transparent), radial-gradient(ellipse 40% 40% at 70% 30%, ${t.to}44, transparent), radial-gradient(ellipse 30% 30% at 30% 70%, ${t.accent}22, transparent)`,
      }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-center items-center p-20 gap-8">
      <span
        class="inline-flex items-center gap-3 px-6 py-3 rounded-full text-2xl font-semibold"
        :style="{ background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
      >
        {{ t.emoji }} {{ t.label }}
      </span>
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
      <p v-if="areaClean" class="text-zinc-500 text-[24px] font-medium absolute bottom-10 right-10">
        {{ areaClean }}
      </p>
    </div>
  </div>
</template>
