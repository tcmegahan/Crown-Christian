export type Profile = {
  authenticated: boolean;
  username?: string;
  roles: string[];
  permissions: string[];
};

export async function getProfile(): Promise<Profile> {
  const res = await fetch('/api/profile/');
  if (!res.ok) return { authenticated: false, roles: [], permissions: [] };
  return (await res.json()) as Profile;
}
