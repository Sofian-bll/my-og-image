<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, limitTags } from '../../src/templates/colors'

const { service = 'Service', host, domain, port_host, status, tags, exposure } = defineProps<{
  service?: string
  host?: string
  domain?: string
  port_host?: string
  status?: string
  tags?: string
  exposure?: string
}>()

const t = getTypeConfig('Task') // amber/orange gradient
const stColor = status ? statusColors[status] : null
const stLabel = status ? statusLabels[status] : null
const tagList = limitTags(tags, 3)

// Build metadata line
const metaParts: string[] = []
if (domain) metaParts.push(domain)
if (port_host) metaParts.push(`port:${port_host}`)
if (host) metaParts.push(host)
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-25"
      :style="{ background: `radial-gradient(ellipse 50% 50% at 40% 60%, ${t.from}33, transparent), radial-gradient(ellipse 40% 40% at 60% 30%, ${t.to}44, transparent), radial-gradient(ellipse 25% 25% at 50% 50%, ${t.accent}22, transparent)` }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-24">

      <div class="flex justify-between items-start w-full">
        <span
          class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
          :style="{ fontWeight: 700, background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
          SERVICE
        </span>
        <span
          v-if="stColor && stLabel"
          class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
          :style="{ fontWeight: 700, background: `${stColor}15`, color: stColor, border: `1px solid ${stColor}30` }"
        >
          <div :style="{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: stColor }" />
          {{ stLabel }}
        </span>
      </div>

      <div class="flex flex-col items-center gap-4">
        <h1
          class="text-white text-center"
          style="font-weight: 700; font-size: 80px; line-height: 1.1; max-width: 1040px; overflow: hidden; line-clamp: 2; word-break: break-word;"
        >
          {{ service }}
        </h1>
      </div>

      <div class="w-full flex flex-col gap-4">
        <div
          v-if="metaParts.length > 0"
          class="flex justify-center items-center gap-5 text-zinc-400"
          style="font-weight: 400; font-size: 28px;"
        >
          <span v-for="(p, i) in metaParts" :key="p" style="display: flex; align-items: center; gap: 20px;">
            <span v-if="i > 0" style="color: #3f3f46;">·</span>
            {{ p }}
          </span>
        </div>
        <div v-if="tagList.length > 0" class="flex justify-center items-center gap-3 text-zinc-500" style="font-weight: 400; font-size: 22px;">
          <span v-for="(t, i) in tagList" :key="t" style="display: flex; align-items: center; gap: 12px;">
            <span v-if="i > 0" style="color: #3f3f46;">·</span>
            <span style="color: #52525b;">#</span>{{ t }}
          </span>
        </div>
      </div>

    </div>
  </div>
</template>
