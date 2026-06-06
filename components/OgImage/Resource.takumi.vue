<script setup lang="ts">
import { getTypeConfig, cleanArea, titleFontSize, subtitleFontSize } from '../../src/templates/colors'

const { title = 'Resource', area = 'Perso', subtitle } = defineProps<{
  title?: string
  area?: string
  subtitle?: string
}>()

const t = getTypeConfig('Resource')
const areaClean = cleanArea(area)
const titleSize = titleFontSize(title)
const subSize = subtitle ? subtitleFontSize(subtitle) : '0'
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-30"
      :style="{ background: `radial-gradient(ellipse 50% 60% at 30% 50%, ${t.from}33, transparent), radial-gradient(ellipse 50% 30% at 70% 70%, ${t.to}44, transparent), radial-gradient(ellipse 20% 20% at 50% 30%, ${t.accent}22, transparent)` }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-20">
      <div class="flex justify-start">
        <span
          class="inline-flex items-center gap-3 px-8 py-4 rounded-full text-xl font-bold uppercase tracking-widest"
          :style="{ background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
        >
          {{ t.emoji }} {{ t.label }}
        </span>
      </div>

      <div class="flex flex-col items-center gap-8" :style="{ maxWidth: '1040px', margin: '0 auto', width: '100%' }">
        <h1
          class="text-white font-extrabold text-center"
          :style="{ fontSize: titleSize, lineHeight: '1.15', maxWidth: '100%', overflow: 'hidden', lineClamp: '3', wordBreak: 'break-word' }"
        >
          {{ title }}
        </h1>
        <p
          v-if="subtitle"
          class="text-zinc-400 text-center"
          :style="{ fontSize: subSize, lineHeight: '1.3', maxWidth: '900px', overflow: 'hidden', lineClamp: '2', wordBreak: 'break-word' }"
        >
          {{ subtitle }}
        </p>
      </div>

      <div class="grid grid-cols-3 items-end text-xl font-bold uppercase tracking-widest">
        <div />
        <div class="flex justify-center text-zinc-500">
          {{ areaClean }}
        </div>
        <div />
      </div>
    </div>
  </div>
</template>
