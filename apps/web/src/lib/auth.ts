export type Profile = {
  authenticated: boolean;
  username?: string;
  roles: string[];
  permissions: string[];
};

const CACHE_KEY = 'crown_profile';
const CACHE_TTL_MS = 5 * 60 * 1000; // 5 minutes

export async function fetchProfileFromServer(): Promise<Profile> {
  const res = await fetch('/api/profile/');
  if (!res.ok) return { authenticated: false, roles: [], permissions: [] };
  return (await res.json()) as Profile;
}

export async function getProfile(): Promise<Profile> {
  try {
    const raw = sessionStorage.getItem(CACHE_KEY);
    if (raw) {
      const parsed = JSON.parse(raw);
      const age = Date.now() - (parsed._ts || 0);
      if (age < CACHE_TTL_MS) {
        return parsed.data as Profile;
      }
    }
    const data = await fetchProfileFromServer();
    sessionStorage.setItem(CACHE_KEY, JSON.stringify({ _ts: Date.now(), data }));
    return data;
  } catch (e) {
    return { authenticated: false, roles: [], permissions: [] };
  }
}

export function clearProfileCache() {
  sessionStorage.removeItem(CACHE_KEY);
}
