/**
 * Eyebrow configuration for OG image title splitting.
 *
 * Splits the title on the first matching separator and uses the
 * left part as a discreet eyebrow (zinc-500) above the main title.
 *
 * If disabled, the full title goes into the main title.
 */

export const EYEBROW_SEPARATORS: string[] = [
  ' - ',
  ' : ',
  ' — ',
  ' | ',
]

export interface EyebrowConfig {
  enabled: boolean
  separators: string[]
  minMainLength: number
}

export const EYEBROW_DEFAULT_RULES: EyebrowConfig = {
  enabled: false,
  separators: EYEBROW_SEPARATORS,
  minMainLength: 4,
}

export const EYEBROW_CONFIG_BY_TYPE: Record<string, EyebrowConfig> = {
  // Resource: "ParentProject - SubResource" → eyebrow = project context
  Resource: { enabled: true, separators: [' - ', ' : '], minMainLength: 4 },

  // Project: "Project - XXX" → eyebrow would be "Project" (too generic)
  // Already has epitech_unit_code in EpitechProject; classic Project uses no split
  Project: { enabled: false, separators: [], minMainLength: 0 },

  // Task: "Domaine - Action" or "Context - Action"
  Task: { enabled: true, separators: [' - ', ' : '], minMainLength: 3 },

  // Aspiration: titles usually don't have a prefix
  Aspiration: { enabled: false, separators: [], minMainLength: 0 },

  // EpitechProject: already uses epitech_unit_code in its own eyebrow
  EpitechProject: { enabled: false, separators: [], minMainLength: 0 },

  // SystemConfig: titles usually don't have a prefix
  SystemConfig: { enabled: false, separators: [], minMainLength: 0 },
}

export function getEyebrowConfig(type: string): EyebrowConfig {
  return EYEBROW_CONFIG_BY_TYPE[type] ?? EYEBROW_DEFAULT_RULES
}
