<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, priorityConfig, getCleanArea, formatDate, titleFontSize, subtitleFontSize } from '../../src/templates/colors'

const { title = 'Project', area = 'Perso', status, priority, due_date, subtitle } = defineProps<{
  title?: string
  area?: string
  status?: string
  priority?: string
  due_date?: string
  subtitle?: string
}>()

const t = getTypeConfig('Project')
const areaInfo = getCleanArea(area)
const stColor = status ? statusColors[status] : null
const stLabel = status ? statusLabels[status] : null
const prio = priority ? priorityConfig[priority] : null
const dateStr = formatDate(due_date)
const titleSize = titleFontSize(title)
const subSize = subtitle ? subtitleFontSize(subtitle) : '0'
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-30"
      :style="{ background: `radial-gradient(ellipse 60% 50% at 20% 80%, ${t.from}33, transparent), radial-gradient(ellipse 40% 40% at 80% 20%, ${t.to}44, transparent), radial-gradient(ellipse 30% 30% at 50% 50%, ${t.accent}22, transparent)` }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-20">
      
      <!-- Top bar -->
      <div class="flex justify-between items-start w-full">
        <div class="flex flex-1 justify-start">
          <span
            class="inline-flex items-center gap-3 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
            :style="{ fontWeight: 700, background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/></svg>
            {{ t.label }}
          </span>
        </div>
        <div class="flex flex-1 justify-end">
          <span
            v-if="stColor && stLabel"
            class="inline-flex items-center gap-3 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
            :style="{ fontWeight: 700, background: `${stColor}15`, color: stColor, border: `1px solid ${stColor}30` }"
          >
            <div :style="{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: stColor }" />
            {{ stLabel }}
          </span>
        </div>
      </div>

      <!-- Center content -->
      <div class="flex flex-col items-center gap-8 w-full" style="max-width: 1040px; margin: 0 auto;">
        <h1
          class="text-white text-center"
          :style="{ fontWeight: 700, fontSize: titleSize, lineHeight: '1.2', maxWidth: '100%', overflow: 'hidden', lineClamp: '3', wordBreak: 'break-word' }"
        >
          {{ title }}
        </h1>
        <p
          v-if="subtitle"
          class="text-zinc-400 text-center"
          :style="{ fontWeight: 400, fontSize: subSize, lineHeight: '1.4', maxWidth: '900px', overflow: 'hidden', lineClamp: '2', wordBreak: 'break-word' }"
        >
          {{ subtitle }}
        </p>
      </div>

      <!-- Bottom bar: 3-col flex -->
      <div class="w-full flex justify-between items-end text-xl uppercase tracking-widest text-zinc-500" style="font-weight: 700;">
        <div class="flex-1 flex justify-start">
          <div v-if="prio" class="flex items-center gap-3" :style="{ color: prio.color }">
            <div class="flex gap-1">
              <div :style="{ width: '8px', height: '24px', backgroundColor: prio.color, opacity: prio.level >= 1 ? 1 : 0.3 }" />
              <div :style="{ width: '8px', height: '24px', backgroundColor: prio.color, opacity: prio.level >= 2 ? 1 : 0.3 }" />
              <div :style="{ width: '8px', height: '24px', backgroundColor: prio.color, opacity: prio.level >= 3 ? 1 : 0.3 }" />
            </div>
            {{ prio.label }}
          </div>
        </div>
        <div class="flex-1 flex justify-center items-center gap-3" :style="{ color: '#a1a1aa' }">
          <div v-html="areaInfo.svg" style="display: flex; align-items: center; justify-content: center; width: 24px; height: 24px;" />
          {{ areaInfo.label }}
        </div>
        <div class="flex-1 flex justify-end items-center gap-3">
          <span v-if="dateStr" style="display: flex; align-items: center; gap: 12px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>
            {{ dateStr }}
          </span>
        </div>
      </div>
      
    </div>
  </div>
</template>
