<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, getCleanArea, formatDateShort, titleFontSize, subtitleFontSize } from '../../src/templates/colors'

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

const metaParts: { label: string; weight: 'bold' | 'normal' }[] = []
if (epitech_unit_code) metaParts.push({ label: epitech_unit_code, weight: 'bold' })
if (epitech_kind) metaParts.push({ label: epitech_kind.toUpperCase(), weight: 'normal' })
if (epitech_cursus) metaParts.push({ label: epitech_cursus, weight: 'normal' })
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
            class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
            :style="{ fontWeight: 700, background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.42 10.922a2 2 0 0 0-.019-3.838L12.83 4.1a2 2 0 0 0-1.66 0L2.6 7.08a2 2 0 0 0 0 3.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/></svg>
            EPITECH PROJECT
          </span>
        </div>
        <div class="flex flex-1 justify-end">
          <span
            v-if="stColor && stLabel"
            class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
            :style="{ fontWeight: 700, background: `${stColor}15`, color: stColor, border: `1px solid ${stColor}30` }"
          >
            <div :style="{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: stColor }" />
            {{ stLabel }}
          </span>
        </div>
      </div>

      <!-- Center: eyebrow + title + subtitle -->
      <div class="flex flex-col items-center gap-6">
        <!-- Epitech header / eyebrow - only show if at least one part -->
        <div
          v-if="metaParts.length > 0"
          class="flex items-center gap-6"
          :style="{ background: 'rgba(255,255,255,0.05)', color: t.accent, border: `1px solid ${t.accent}30`, padding: '12px 32px', borderRadius: '9999px' }"
        >
          <span
            v-for="(p, i) in metaParts"
            :key="p.label"
            :style="{ fontWeight: p.weight === 'bold' ? 700 : 400, fontSize: '24px', letterSpacing: '0.1em', textTransform: 'uppercase' }"
          >
            <span v-if="i > 0" style="color: #3f3f46; margin-right: 24px;">·</span>
            {{ p.label }}
          </span>
        </div>

        <h1
          class="text-white text-center"
          style="font-weight: 700; font-size: 72px; line-height: 1.2; max-width: 1040px; word-break: break-word;"
        >
          {{ title }}
        </h1>
        <p
          v-if="subtitle"
          class="text-zinc-400 text-center"
          style="font-weight: 400; font-size: 28px; line-height: 1.4; max-width: 900px; word-break: break-word;"
        >
          {{ subtitle }}
        </p>
      </div>

      <!-- Bottom bar: 3-col -->
      <div class="w-full flex items-end" style="font-weight: 700; font-size: 22px;">
        <div class="flex flex-1 justify-start"></div>

        <div class="flex flex-1 justify-center">
          <div class="flex items-center gap-2 text-zinc-500">
            <div v-html="areaInfo.svg" style="display: flex; align-items: center; justify-content: center; width: 22px; height: 22px;" />
            <span class="uppercase tracking-widest">{{ areaInfo.label }}</span>
          </div>
        </div>

        <div class="flex flex-1 justify-end">
          <div v-if="dateStart && dateEnd" class="flex items-center gap-2 text-zinc-500">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>
            <span style="font-weight: 400;">{{ dateStart }} → {{ dateEnd }}</span>
          </div>
          <div v-else-if="dateEnd" class="flex items-center gap-2 text-zinc-500">
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>
            <span style="font-weight: 400;">{{ dateEnd }}</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
