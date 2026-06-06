const pascalMap: Record<string, string> = {
  project: 'Project',
  resource: 'Resource',
  task: 'Task',
  aspiration: 'Aspiration',
  systemconfig: 'SystemConfig',
  epitechproject: 'EpitechProject',
  service: 'Service',
  machine: 'Machine',
}

export default defineEventHandler(async (event) => {
  const template = getRouterParam(event, 'template') || 'project'
  const PascalCase = pascalMap[template] ?? (template.charAt(0).toUpperCase() + template.slice(1))
  const query = getQuery(event)

  const props: Record<string, string> = {}
  for (const [key, value] of Object.entries(query)) {
    if (value) props[key] = String(value)
  }

  const propPairs = Object.entries(props).map(
    ([k, v]) => `${k}_${encodeURIComponent(v)}`,
  )

  const toBase64 = (str: string) => Buffer.from(str, 'utf-8').toString('base64')
  const encodedProps = toBase64(JSON.stringify(props))
  const encodedPath = toBase64(`__og-image__/image/${template}/og.png`)

  const url = [
    `c_${PascalCase}`,
    ...propPairs,
    `q_${encodedProps}`,
    `p_${encodedPath}`,
  ].join(',') + '.png'

  return $fetch(`/_og/d/${url}`)
})
