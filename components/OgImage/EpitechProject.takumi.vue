<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, getCleanArea, formatDate, formatDateShort, titleFontSize, subtitleFontSize } from '../../src/templates/colors'

const { title = 'Epitech Project', area = 'Epitech', status, epitech_unit_code, epitech_kind, epitech_cursus, scheduled_date, due_date, subtitle } = defineProps<{
  title?: string
  area?: string
  status?: string
  epitech_unit_code?: string
  epitech_kind?: string
  epitech_cursus?: string
  scheduled_date?: string
  due_date?: string
  subtitle?: string
}>()

const t = getTypeConfig('EpitechProject')
const areaInfo = getCleanArea(area)
const stColor = status ? statusColors[status] : null
const stLabel = status ? statusLabels[status] : null
const dateStart = formatDateShort(scheduled_date)
const dateEnd = formatDateShort(due_date)
const titleSize = titleFontSize(title)
const subSize = subtitle ? subtitleFontSize(subtitle) : '0'

const metaParts: string[] = []
if (epitech_unit_code) metaParts.push(epitech_unit_code)
if (epitech_kind) metaParts.push(epitech_kind.toUpperCase())
if (epitech_cursus) metaParts.push(epitech_cursus)
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-35"
      :style="{ background: `radial-gradient(ellipse 60% 50% at 20% 80%, ${t.from}55, transparent), radial-gradient(ellipse 40% 40% at 80% 20%, ${t.to}55, transparent), radial-gradient(ellipse 30% 30% at 50% 50%, ${t.accent}22, transparent)` }"
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
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.42 10.922a2 2 0 0 0-.019-3.838L12.83 4.1a2 2 0 0 0-1.66 0L2.6 7.08a2 2 0 0 0 0 3.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/></svg>
            EPITECH PROJECT
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
      <div class="flex flex-col items-center gap-6 w-full" style="max-width: 1040px; margin: 0 auto;">

        <!-- Epitech header / eyebrow -->
        <div
          v-if="metaParts.length > 0"
          class="flex items-center gap-4 px-8 py-3 rounded-full text-2xl tracking-widest"
          :style="{ background: 'rgba(255,255,255,0.05)', color: t.accent, border: `1px solid ${t.accent}30`, fontWeight: 400 }"
        >
          <span v-for="(p, i) in metaParts" :key="p" style="display: flex; align-items: center; gap: 16px;">
            <span v-if="i > 0" :style="{ color: '#3f3f46' }">·</span>
            <span style="font-weight: 700;">{{ p }}</span>
          </span>
        </div>

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
      <div class="w-full flex justify-between items-end text-xl uppercase tracking-widest" style="font-weight: 700;">
        <div class="flex-1 flex justify-start">
          <!-- No priority for EpitechProject for now -->
        </div>
        <div class="flex-1 flex justify-center items-center gap-3" :style="{ color: '#a1a1aa' }">
          <div class="flex items-center gap-3">
            <div v-html="areaInfo.svg" style="display: flex; align-items: center; justify-content: center; width: 24px; height: 24px;" />
            {{ areaInfo.label }}
          </div>
        </div>
        <div class="flex-1 flex justify-end items-center gap-3 text-zinc-500">
          <span v-if="dateStart && dateEnd" style="display: flex; align-items: center; gap: 12px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>
            {{ dateStart }} → {{ dateEnd }}
          </span>
          <span v-else-if="dateEnd" style="display: flex; align-items: center; gap: 12px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>
            {{ dateEnd }}
          </span>
        </div>
      </div>

    </div>
  </div>
</template>
