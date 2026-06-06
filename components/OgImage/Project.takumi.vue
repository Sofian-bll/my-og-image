<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, prioritySymbols, cleanArea, formatDate } from '../../src/templates/colors'

const { title = 'Project', area = 'Perso', status, priority, due_date, subtitle } = defineProps<{
  title?: string
  area?: string
  status?: string
  priority?: string
  due_date?: string
  subtitle?: string
}>()

const t = getTypeConfig('Project')
const areaClean = cleanArea(area)
const statusColor = status ? statusColors[status] ?? '#6b7280' : null
const statusLabel = status ? statusLabels[status] ?? status : null
const prioritySymbol = priority ? prioritySymbols[priority] ?? '' : null
const dateStr = formatDate(due_date)
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: Inter, sans-serif;">
    <div
      class="absolute inset-0 opacity-30"
      :style="{
        background: `radial-gradient(ellipse 60% 50% at 20% 80%, ${t.from}33, transparent), radial-gradient(ellipse 40% 40% at 80% 20%, ${t.to}44, transparent), radial-gradient(ellipse 30% 30% at 50% 50%, ${t.accent}22, transparent)`,
      }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10 rounded-none" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-20">
      <div class="flex justify-between items-start">
        <span
          class="inline-flex items-center gap-3 px-6 py-3 rounded-full text-2xl font-semibold"
          :style="{ background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
        >
          {{ t.emoji }} {{ t.label }}
        </span>
        <span
          v-if="statusColor && statusLabel"
          class="inline-flex items-center gap-2 px-5 py-3 rounded-full text-2xl font-semibold"
          :style="{ background: `${statusColor}15`, color: statusColor, border: `1px solid ${statusColor}30` }"
        >
          <span :style="{ fontSize: '16px' }">●</span> {{ statusLabel }}
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

      <div class="flex justify-center items-center gap-8 text-zinc-500 text-[24px] font-medium">
        <span v-if="prioritySymbol" class="flex items-center gap-2" :style="{ color: t.accent }">
          {{ prioritySymbol }} {{ priority }}
        </span>
        <span v-if="priority && areaClean" class="text-zinc-600">—</span>
        <span>{{ areaClean }}</span>
        <span v-if="dateStr" class="text-zinc-600">—</span>
        <span v-if="dateStr">📅 {{ dateStr }}</span>
      </div>
    </div>
  </div>
</template>
