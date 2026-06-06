export default defineEventHandler(async (event) => {
  const template = getRouterParam(event, 'template') || 'default'
  const PascalCase = template.charAt(0).toUpperCase() + template.slice(1)
  const query = getQuery(event)

  const props: Record<string, string> = {}
  for (const [key, value] of Object.entries(query)) {
    if (value) props[key] = String(value)
  }

  const propPairs = Object.entries(props).map(
    ([k, v]) => `${k}_${encodeURIComponent(v)}`,
  )

  const encodedProps = btoa(JSON.stringify(props))
  const encodedPath = btoa(`__og-image__/image/${template}/og.png`)

  const url = [
    `c_${PascalCase}`,
    ...propPairs,
    `q_${encodedProps}`,
    `p_${encodedPath}`,
  ].join(',') + '.png'

  return $fetch(`/_og/d/${url}`)
})
