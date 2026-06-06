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
            class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
            :style="{ fontWeight: 700, background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>
            {{ t.label }}
          </span>
        </div>
        <div class="flex flex-1 justify-end"></div>
      </div>

      <!-- Center: title + subtitle -->
      <div class="flex flex-col items-center gap-6">
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
          <div
            v-if="areaInfo.label !== 'Unknown'"
            class="flex items-center gap-2 text-zinc-500"
          >
            <div v-html="areaInfo.svg" style="display: flex; align-items: center; justify-content: center; width: 22px; height: 22px;" />
            <span class="uppercase tracking-widest">{{ areaInfo.label }}</span>
          </div>
        </div>

        <div class="flex flex-1 justify-end">
          <div
            v-if="tagList.length > 0"
            class="flex items-center gap-4 text-zinc-400"
            style="font-weight: 400;"
          >
            <span
              v-for="(t, i) in tagList"
              :key="t"
              class="flex items-center gap-2"
            >
              <span v-if="i > 0" style="color: #3f3f46;">·</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" x2="7.01" y1="7" y2="7"/></svg>
              <span style="text-transform: none;">{{ t }}</span>
            </span>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
