<script setup lang="ts">
import { getTypeConfig, getCleanArea, splitTitle, titleFontSize, subtitleFontSize } from '../../src/templates/colors'

const { title = 'Aspiration', area = 'Perso', description } = defineProps<{
  title?: string
  area?: string
  description?: string
}>()

const t = getTypeConfig('Aspiration')
const areaInfo = getCleanArea(area)
const split = splitTitle(title, 'Aspiration')
const titleSize = titleFontSize(split.main || title)
const descSize = description ? subtitleFontSize(description) : '0'
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-20"
      :style="{ background: `radial-gradient(ellipse 60% 50% at 50% 50%, ${t.from}22, transparent), radial-gradient(ellipse 40% 30% at 70% 40%, ${t.to}33, transparent), radial-gradient(ellipse 30% 40% at 30% 60%, ${t.accent}18, transparent)` }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-20">

      <div class="flex justify-between items-start w-full">
        <div class="flex flex-1 justify-start">
          <span
            class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
            :style="{ fontWeight: 700, background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m11 20 5-5-5-5"/><path d="M18 20V10a4 4 0 0 0-4-4H5"/></svg>
            {{ t.label }}
          </span>
        </div>
        <div class="flex flex-1 justify-end"></div>
      </div>

      <div class="flex flex-col items-center gap-6">
        <div
          v-if="split.eyebrow"
          class="text-zinc-500"
          style="font-weight: 400; font-size: 36px; letter-spacing: 0.02em; max-width: 1000px; word-break: break-word;"
        >
          {{ split.eyebrow }}
        </div>
        <h1
          class="text-white text-center"
          :style="{ fontWeight: 700, fontSize: titleSize, lineHeight: '1.1', maxWidth: '1040px', overflow: 'hidden', lineClamp: '3', wordBreak: 'break-word' }"
        >
          {{ split.main || title }}
        </h1>
        <p
          v-if="description"
          class="text-center"
          :style="{ fontWeight: 400, fontSize: descSize, lineHeight: '1.4', maxWidth: '900px', overflow: 'hidden', lineClamp: '3', wordBreak: 'break-word', color: '#fb7185', opacity: 0.8 }"
        >
          {{ description }}
        </p>
      </div>

      <div class="w-full flex items-end" style="font-weight: 700; font-size: 22px;">
        <div class="flex flex-1 justify-start"></div>
        <div class="flex flex-1 justify-center">
          <div v-if="areaInfo.label !== 'Unknown'" class="flex items-center gap-2 text-zinc-500">
            <div v-html="areaInfo.svg" style="display: flex; align-items: center; justify-content: center; width: 22px; height: 22px;" />
            <span class="uppercase tracking-widest">{{ areaInfo.label }}</span>
          </div>
        </div>
        <div class="flex flex-1 justify-end"></div>
      </div>

    </div>
  </div>
</template>
