<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, titleFontSize } from '../../src/templates/colors'

const { hostname = 'Machine', os, cpu, ram, disk, ip_tailscale, role, status } = defineProps<{
  hostname?: string
  os?: string
  cpu?: string
  ram?: string
  disk?: string
  ip_tailscale?: string
  role?: string
  status?: string
}>()

const t = getTypeConfig('SystemConfig')
const stColor = status ? statusColors[status] : null
const stLabel = status ? statusLabels[status] : null
const titleSizeVal = titleFontSize(hostname || 'Machine')

const specs: string[] = []
if (os) specs.push(os)
if (cpu) specs.push(cpu)
if (ram) specs.push(ram)
if (disk) specs.push(disk)

const roleList = role ? role.split(',').map(r => r.trim()).filter(Boolean) : []
</script>

<template>
  <div class="w-full h-full flex bg-zinc-950 relative overflow-hidden" style="font-family: 'Syne', sans-serif;">
    <div
      class="absolute inset-0 opacity-20"
      :style="{ background: `radial-gradient(ellipse 50% 50% at 50% 50%, ${t.from}33, transparent), radial-gradient(ellipse 40% 40% at 70% 30%, ${t.to}44, transparent)` }"
    />
    <div class="absolute inset-0 ring-1 ring-white/10 z-10" />
    <div class="relative z-20 w-full h-full flex flex-col justify-between p-24">

      <div class="flex justify-between items-start w-full">
        <span
          class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest"
          :style="{ fontWeight: 700, background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="8" x="5" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><path d="M6 18h2"/><path d="M12 18h6"/></svg>
          MACHINE
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

      <div class="flex flex-col items-center gap-6">
        <h1
          class="text-white text-center"
          :style="{ fontWeight: 700, fontSize: titleSizeVal, lineHeight: '1.1', maxWidth: '1040px', overflow: 'hidden', wordBreak: 'break-word' }"
        >
          {{ hostname }}
        </h1>
        <div
          v-if="specs.length > 0"
          class="flex flex-wrap justify-center items-center gap-4 text-zinc-400"
          style="font-weight: 400; font-size: 26px; max-width: 1000px;"
        >
          <span v-for="(s, i) in specs" :key="s" style="display: flex; align-items: center; gap: 16px;">
            <span v-if="i > 0" style="color: #3f3f46;">·</span>
            {{ s }}
          </span>
        </div>
      </div>

      <div class="w-full flex justify-center items-center gap-4 text-zinc-500" style="font-weight: 400; font-size: 22px;">
        <span v-for="(r, i) in roleList" :key="r" style="display: flex; align-items: center; gap: 12px;">
          <span v-if="i > 0" style="color: #3f3f46;">·</span>
          {{ r }}
        </span>
        <span v-if="ip_tailscale" style="display: flex; align-items: center; gap: 12px;">
          <span v-if="roleList.length > 0" style="color: #3f3f46;">·</span>
          {{ ip_tailscale }}
        </span>
      </div>

    </div>
  </div>
</template>
