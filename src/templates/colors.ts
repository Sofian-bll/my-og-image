export const typeGradients: Record<string, { from: string; to: string; accent: string; label: string }> = {
  Project: { from: '#4f46e5', to: '#6d28d9', accent: '#818cf8', label: 'Project' },
  Resource: { from: '#0f766e', to: '#047857', accent: '#2dd4bf', label: 'Resource' },
  Task: { from: '#b45309', to: '#c2410c', accent: '#fbbf24', label: 'Task' },
  Aspiration: { from: '#e11d48', to: '#be185d', accent: '#fb7185', label: 'Aspiration' },
  SystemConfig: { from: '#334155', to: '#27272a', accent: '#94a3b8', label: 'System' },
  EpitechProject: { from: '#1e3a8a', to: '#4f46e5', accent: '#60a5fa', label: 'Epitech Project' },
}

export const statusColors: Record<string, string> = {
  todo: '#6b7280',
  in_progress: '#3b82f6',
  paused: '#f59e0b',
  done: '#10b981',
  dropped: '#ef4444',
}

export const statusLabels: Record<string, string> = {
  todo: 'TODO',
  in_progress: 'IN PROGRESS',
  paused: 'PAUSED',
  done: 'DONE',
  dropped: 'DROPPED',
}

export const priorityConfig: Record<string, { label: string; color: string; level: number }> = {
  low:    { label: 'LOW',    color: '#3b82f6', level: 1 },
  medium: { label: 'MEDIUM', color: '#f59e0b', level: 2 },
  high:   { label: 'HIGH',   color: '#ef4444', level: 3 },
}

export function getTypeConfig(type: string) {
  return typeGradients[type] ?? typeGradients.SystemConfig
}

export function getCleanArea(area: string): { label: string, svg: string } {
  const clean = area.replace(/[[\]]/g, '').replace(/[^\w\s]/gi, '').trim()

  const icons: Record<string, string> = {
    Perso: `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>`,
    Epitech: `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.42 10.922a2 2 0 0 0-.019-3.838L12.83 4.1a2 2 0 0 0-1.66 0L2.6 7.08a2 2 0 0 0 0 3.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/></svg>`,
  }

  const fallbackIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/></svg>`

  return {
    label: clean || 'Unknown',
    svg: icons[clean] || fallbackIcon
  }
}

export function formatDate(date: string | undefined): string {
  if (!date) return ''
  const d = new Date(date)
  if (isNaN(d.getTime())) return date
  return d.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short', year: 'numeric' })
}

export function formatDateShort(date: string | undefined): string {
  if (!date) return ''
  const d = new Date(date)
  if (isNaN(d.getTime())) return date
  return d.toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit' })
}

export function titleFontSize(title: string): string {
  const len = title.length
  if (len < 30) return '72px'
  if (len < 60) return '56px'
  if (len < 90) return '44px'
  return '36px'
}

export function subtitleFontSize(sub: string): string {
  const len = sub.length
  if (len < 60) return '32px'
  if (len < 120) return '26px'
  return '22px'
}

export function limitTags(tagsString: string | undefined, max: number = 2): string[] {
  if (!tagsString) return []
  return tagsString.split(',').map(t => t.trim()).filter(Boolean).slice(0, max)
}

import { getEyebrowConfig } from './eyebrow-config'

export function splitTitle(title: string, type: string = 'Resource'): { eyebrow: string; main: string } {
  if (!title) return { eyebrow: '', main: '' }

  const config = getEyebrowConfig(type)
  if (!config.enabled) return { eyebrow: '', main: title }

  for (const sep of config.separators) {
    const idx = title.indexOf(sep)
    if (idx !== -1) {
      const eyebrow = title.slice(0, idx).trim()
      const main = title.slice(idx + sep.length).trim()

      if (main.length < config.minMainLength) {
        return { eyebrow: '', main: title }
      }

      return { eyebrow, main }
    }
  }

  return { eyebrow: '', main: title }
}
