<script setup lang="ts">
import { getTypeConfig, getCleanArea, limitTags, titleFontSize, subtitleFontSize } from '../../src/templates/colors'

const { title = 'Resource', area = 'Perso', subtitle, tags } = defineProps<{
  title?: string
  area?: string
  subtitle?: string
  tags?: string
}>()

const t = getTypeConfig('Resource')
const areaInfo = getCleanArea(area)
const titleSize = titleFontSize(title)
const subSize = subtitle ? subtitleFontSize(subtitle) : '0'
const tagList = limitTags(tags, 2)
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-30"
      :style="{ background: `radial-gradient(ellipse 50% 60% at 30% 50%, ${t.from}33, transparent), radial-gradient(ellipse 50% 30% at 70% 70%, ${t.to}44, transparent), radial-gradient(ellipse 20% 20% at 50% 30%, ${t.accent}22, transparent)` }"
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
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>
            {{ t.label }}
          </span>
        </div>
        <div class="flex flex-1 justify-end">
          <!-- No status for resources -->
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
      <div class="w-full flex justify-between items-end text-xl uppercase tracking-widest" style="font-weight: 700;">
        <div class="flex-1 flex justify-start">
          <!-- No priority for resources -->
        </div>
        <div class="flex-1 flex justify-center items-center gap-3" :style="{ color: '#a1a1aa' }">
          <div v-if="areaInfo.label !== 'Unknown'" class="flex items-center gap-3">
            <div v-html="areaInfo.svg" style="display: flex; align-items: center; justify-content: center; width: 24px; height: 24px;" />
            {{ areaInfo.label }}
          </div>
        </div>
        <div class="flex-1 flex justify-end items-center gap-3 text-zinc-400">
          <span v-for="t in tagList" :key="t" style="display: flex; align-items: center; gap: 8px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" x2="7.01" y1="7" y2="7"/></svg>
            {{ t }}
          </span>
        </div>
      </div>

    </div>
  </div>
</template>
