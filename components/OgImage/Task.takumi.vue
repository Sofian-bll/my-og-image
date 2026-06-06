<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, cleanArea, formatDate, titleFontSize } from '../../src/templates/colors'

const { title = 'Task', area = 'Perso', status, due_date } = defineProps<{
  title?: string
  area?: string
  status?: string
  due_date?: string
}>()

const t = getTypeConfig('Task')
const areaClean = cleanArea(area)
const stColor = status ? statusColors[status] : null
const stLabel = status ? statusLabels[status] : null
const dateStr = formatDate(due_date)
const titleSize = titleFontSize(title)
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-25"
      :style="{ background: `radial-gradient(ellipse 50% 50% at 40% 60%, ${t.from}33, transparent), radial-gradient(ellipse 40% 40% at 60% 30%, ${t.to}44, transparent), radial-gradient(ellipse 25% 25% at 50% 50%, ${t.accent}22, transparent)` }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-20">
      <div class="flex justify-between items-start">
        <span
          class="inline-flex items-center gap-3 px-8 py-4 rounded-full text-xl font-bold uppercase tracking-widest"
          :style="{ background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
        >
          {{ t.emoji }} {{ t.label }}
        </span>
        <span
          v-if="stColor && stLabel"
          class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl font-bold uppercase tracking-widest"
          :style="{ background: `${stColor}15`, color: stColor, border: `1px solid ${stColor}30` }"
        >
          ● {{ stLabel }}
        </span>
      </div>

      <div class="flex flex-col items-center" :style="{ maxWidth: '1040px', margin: '0 auto', width: '100%' }">
        <h1
          class="text-white font-extrabold text-center"
          :style="{ fontSize: titleSize, lineHeight: '1.15', maxWidth: '100%', overflow: 'hidden', lineClamp: '3', wordBreak: 'break-word' }"
        >
          {{ title }}
        </h1>
      </div>

      <div class="grid grid-cols-3 items-end text-xl font-bold uppercase tracking-widest">
        <div />
        <div class="flex justify-center text-zinc-500">
          {{ areaClean }}
        </div>
        <div class="flex justify-end text-zinc-500">
          <span v-if="dateStr">📅 {{ dateStr }}</span>
        </div>
      </div>
    </div>
  </div>
</template>
