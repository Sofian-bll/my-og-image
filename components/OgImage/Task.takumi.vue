<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, cleanArea, formatDate } from '../../src/templates/colors'

const { title = 'Task', area = 'Perso', status, due_date } = defineProps<{
  title?: string
  area?: string
  status?: string
  due_date?: string
}>()

const t = getTypeConfig('Task')
const areaClean = cleanArea(area)
const statusColor = status ? statusColors[status] ?? '#6b7280' : null
const statusLabel = status ? statusLabels[status] ?? status : null
const dateStr = formatDate(due_date)
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: Inter, sans-serif;">
    <div
      class="absolute inset-0 opacity-25"
      :style="{
        background: `radial-gradient(ellipse 50% 50% at 40% 60%, ${t.from}33, transparent), radial-gradient(ellipse 40% 40% at 60% 30%, ${t.to}44, transparent), radial-gradient(ellipse 25% 25% at 50% 50%, ${t.accent}22, transparent)`,
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
        <span
          v-if="statusColor && statusLabel"
          class="inline-flex items-center gap-2 px-5 py-3 rounded-full text-2xl font-semibold"
          :style="{ background: `${statusColor}15`, color: statusColor, border: `1px solid ${statusColor}30` }"
        >
          <span :style="{ fontSize: '16px' }">●</span> {{ statusLabel }}
        </span>
      </div>

      <div class="flex flex-col items-center" style="max-width: 1040px; margin: 0 auto;">
        <h1 class="text-white text-[72px] font-extrabold leading-tight text-center" style="letter-spacing: -0.02em;">
          {{ title }}
        </h1>
      </div>

      <div class="flex justify-center items-center gap-8 text-zinc-500 text-[24px] font-medium">
        <span>{{ areaClean }}</span>
        <span v-if="dateStr" class="text-zinc-600">—</span>
        <span v-if="dateStr">📅 {{ dateStr }}</span>
      </div>
    </div>
  </div>
</template>
