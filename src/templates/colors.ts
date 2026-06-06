export const typeGradients: Record<string, { from: string; to: string; accent: string; emoji: string; label: string }> = {
  Project: { from: '#4f46e5', to: '#6d28d9', accent: '#818cf8', emoji: '📂', label: 'Project' },
  Resource: { from: '#0f766e', to: '#047857', accent: '#2dd4bf', emoji: '📚', label: 'Resource' },
  Task: { from: '#b45309', to: '#c2410c', accent: '#fbbf24', emoji: '✏️', label: 'Task' },
  Aspiration: { from: '#e11d48', to: '#be185d', accent: '#fb7185', emoji: '🌱', label: 'Aspiration' },
  SystemConfig: { from: '#334155', to: '#27272a', accent: '#94a3b8', emoji: '⚙️', label: 'System' },
}

export const statusColors: Record<string, string> = {
  todo: '#6b7280',
  in_progress: '#3b82f6',
  paused: '#f59e0b',
  done: '#10b981',
  dropped: '#ef4444',
}

export const statusLabels: Record<string, string> = {
  todo: 'todo',
  in_progress: 'in progress',
  paused: 'paused',
  done: 'done',
  dropped: 'dropped',
}

export const prioritySymbols: Record<string, string> = {
  low: '◉',
  medium: '◉◉',
  high: '◉◉◉',
}

export function getTypeConfig(type: string) {
  return typeGradients[type] ?? typeGradients.SystemConfig
}

export function cleanArea(area: string): string {
  return area.replace(/[[\]]/g, '').trim()
}

export function formatDate(date: string | undefined): string {
  if (!date) return ''
  const d = new Date(date)
  if (isNaN(d.getTime())) return date
  return d.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short', year: 'numeric' })
}
