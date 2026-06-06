<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, limitTags, titleFontSize } from '../../src/templates/colors'

const { service = 'Service', host, domain, port_host, status, tags, exposure } = defineProps<{
  service?: string
  host?: string
  domain?: string
  port_host?: string | number
  status?: string
  tags?: string
  exposure?: string
}>()

const t = getTypeConfig('Task')
const stColor = status ? statusColors[status] : null
const stLabel = status ? statusLabels[status] : null
const tagList = limitTags(tags, 5)
const titleSizeVal = titleFontSize(service)

const identityInfo = [
  { label: domain, icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>' },
  { label: port_host ? `PORT ${port_host}` : '', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 3h5v5"/><path d="M4 20L21 3"/><path d="M21 16v5h-5"/><path d="M15 21l6-6"/><path d="M9 3L3 9"/></svg>' },
  { label: exposure ? exposure.toUpperCase() : '', icon: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>' },
].filter(i => i.label)
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-25"
      :style="{ background: `radial-gradient(ellipse 50% 50% at 40% 60%, ${t.from}33, transparent), radial-gradient(ellipse 40% 40% at 60% 30%, ${t.to}44, transparent), radial-gradient(ellipse 25% 25% at 50% 50%, ${t.accent}22, transparent)` }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full p-24 flex flex-col">

      <!-- Top Bar -->
      <div class="flex justify-between items-start w-full absolute top-24 left-24 right-24">
        <span
          class="inline-flex items-center gap-3 px-8 py-4 rounded-full text-xl uppercase tracking-widest font-bold"
          :style="{ background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
          SERVICE
        </span>
        <span
          v-if="stColor && stLabel"
          class="inline-flex items-center gap-3 px-8 py-4 rounded-full text-xl uppercase tracking-widest font-bold"
          :style="{ background: `${stColor}15`, color: stColor, border: `1px solid ${stColor}30` }"
        >
          <div :style="{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: stColor }" />
          {{ stLabel }}
        </span>
      </div>

      <!-- Main Identity Section -->
      <div class="flex-1 flex flex-col items-center justify-center gap-8">
        <h1
          class="text-white text-center font-bold"
          :style="{ fontSize: '100px', lineHeight: '1', maxWidth: '1040px', overflow: 'hidden', lineClamp: 2, wordBreak: 'break-word' }"
        >
          {{ service }}
        </h1>

        <!-- Primary Info Badges -->
        <div v-if="identityInfo.length > 0" class="flex flex-wrap justify-center items-center gap-6">
          <div
            v-for="info in identityInfo"
            :key="info.label"
            class="flex items-center gap-3 text-zinc-100"
            style="font-size: 32px; font-weight: 500;"
          >
            <div v-html="info.icon" class="text-zinc-500" />
            <span>{{ info.label }}</span>
          </div>
        </div>
      </div>

      <!-- Footer Context -->
      <div class="flex justify-between items-end w-full absolute bottom-24 left-24 right-24">
        <div class="flex items-center gap-4">
          <span
            v-if="host"
            class="inline-flex items-center gap-3 px-6 py-3 rounded-xl text-xl font-bold uppercase tracking-wider"
            :style="{ background: 'rgba(255,255,255,0.06)', color: '#d4d4d8', border: '1px solid rgba(255,255,255,0.12)' }"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="8" x="5" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><path d="M6 18h2"/><path d="M12 18h6"/></svg>
            {{ host }}
          </span>
        </div>

        <div class="flex gap-3">
          <span
            v-for="tag in tagList"
            :key="tag"
            class="px-5 py-2 rounded-lg text-lg font-bold uppercase tracking-widest text-zinc-500"
            :style="{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.06)' }"
          >
            #{{ tag }}
          </span>
        </div>
      </div>

    </div>
  </div>
</template>
