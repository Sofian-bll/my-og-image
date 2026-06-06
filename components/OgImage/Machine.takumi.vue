<script setup lang="ts">
import { getTypeConfig, statusColors, statusLabels, getCleanArea, titleFontSize, subtitleFontSize } from '../../src/templates/colors'

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
const titleSize = titleFontSize(hostname)

const specBadges = [
  { label: os, icon: '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="12" x="2" y="9" rx="2" ry="2"/><path d="M12 9V2"/><path d="M6 13h12"/></svg>' },
  { label: cpu, icon: '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>' },
  { label: ram, icon: '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 19v-3"/><path d="M10 19v-3"/><path d="M14 19v-3"/><path d="M18 19v-3"/><rect width="18" height="7" x="3" y="12" rx="1"/><path d="M11 5h2"/><path d="M11 8h2"/><path d="M11 2h2"/></svg>' },
  { label: disk, icon: '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12s-1-7-10-7-10 7-10 7 1-7 10-7 10 7 10 7Z"/><circle cx="12" cy="12" r="3"/></svg>' },
].filter(b => b.label)

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

      <!-- Top Bar -->
      <div class="flex justify-between items-start w-full">
        <span
          class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest font-bold"
          :style="{ background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="8" x="5" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><path d="M6 18h2"/><path d="M12 18h6"/></svg>
          MACHINE
        </span>
        <span
          v-if="stColor && stLabel"
          class="inline-flex items-center gap-2 px-8 py-4 rounded-full text-xl uppercase tracking-widest font-bold"
          :style="{ background: `${stColor}15`, color: stColor, border: `1px solid ${stColor}30` }"
        >
          <div :style="{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: stColor }" />
          {{ stLabel }}
        </span>
      </div>

      <!-- Center: Titre auto-resize -->
      <div class="flex flex-col items-center justify-center flex-1">
        <h1
          class="text-white text-center font-bold"
          :style="{ fontSize: titleSize, lineHeight: '1.1', maxWidth: '1040px', overflow: 'hidden', lineClamp: 2, wordBreak: 'break-word', textTransform: 'uppercase', letterSpacing: '0.05em' }"
        >
          {{ hostname }}
        </h1>
      </div>

      <!-- Bottom Layout: Specs (Left) + IP/Roles (Right) -->
      <div class="flex justify-between items-end w-full">
        <!-- Specs Pile (Left) -->
        <div class="flex flex-col items-start gap-2">
          <div
            v-for="b in specBadges"
            :key="b.label"
            class="flex items-center gap-2 px-4 py-1.5 rounded-lg whitespace-nowrap"
            :style="{ background: 'rgba(255,255,255,0.04)', border: '1px solid rgba(255,255,255,0.08)' }"
          >
            <div v-html="b.icon" class="text-zinc-500" />
            <span class="text-base font-bold text-zinc-300 uppercase">{{ b.label }}</span>
          </div>
        </div>

        <!-- Metadata (Right) -->
        <div class="flex flex-col items-end gap-4">
          <div v-if="ip_tailscale" class="flex items-center gap-2 text-zinc-500 font-bold tracking-widest text-lg uppercase">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            {{ ip_tailscale }}
          </div>

          <div class="flex gap-2 flex-wrap justify-end max-w-[500px]">
            <span
              v-for="r in roleList"
              :key="r"
              class="px-4 py-1.5 rounded-md text-xs font-bold uppercase tracking-widest whitespace-nowrap"
              :style="{ background: `${t.accent}15`, color: t.accent, border: `1px solid ${t.accent}30` }"
            >
              {{ r }}
            </span>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
