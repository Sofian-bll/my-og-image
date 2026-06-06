<script setup lang="ts">
import { getTypeConfig, getCleanArea, titleFontSize, subtitleFontSize } from '../../src/templates/colors'

const { title = 'System', area, subtitle } = defineProps<{
  title?: string
  area?: string
  subtitle?: string
}>()

const t = getTypeConfig('SystemConfig')
const areaInfo = area ? getCleanArea(area) : { label: '', svg: '' }
const titleSize = titleFontSize(title)
const subSize = subtitle ? subtitleFontSize(subtitle) : '0'
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-20"
      :style="{ background: `radial-gradient(ellipse 50% 50% at 50% 50%, ${t.from}33, transparent), radial-gradient(ellipse 40% 40% at 70% 30%, ${t.to}44, transparent), radial-gradient(ellipse 30% 30% at 30% 70%, ${t.accent}22, transparent)` }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-20">

      <div class="flex justify-between items-start w-full">
        <div class="flex flex-1 justify-start">
          <span
            class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
            :style="{ fontWeight: 700, background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/></svg>
            {{ t.label }}
          </span>
        </div>
        <div class="flex flex-1 justify-end"></div>
      </div>

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

      <div class="w-full flex items-end" style="font-weight: 700; font-size: 22px;">
        <div class="flex flex-1 justify-start"></div>
        <div class="flex flex-1 justify-center">
          <div v-if="areaInfo.label" class="flex items-center gap-2 text-zinc-500">
            <div v-html="areaInfo.svg" style="display: flex; align-items: center; justify-content: center; width: 22px; height: 22px;" />
            <span class="uppercase tracking-widest">{{ areaInfo.label }}</span>
          </div>
        </div>
        <div class="flex flex-1 justify-end"></div>
      </div>

    </div>
  </div>
</template>
