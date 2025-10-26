import React, { createContext, useContext, useEffect, useState } from 'react';
import { getProfile as fetchProfile } from './auth';

type Profile = {
  authenticated: boolean;
  username?: string;
  roles: string[];
  permissions: string[];
};

type ProfileContextValue = {
  profile: Profile;
  refresh: () => Promise<void>;
};

const defaultValue: ProfileContextValue = {
  profile: { authenticated: false, roles: [], permissions: [] },
  refresh: async () => {},
};

const ProfileContext = createContext<ProfileContextValue>(defaultValue);

export const ProfileProvider: React.FC<React.PropsWithChildren<Record<string, unknown>>> = ({
  children,
}) => {
  const [profile, setProfile] = useState<Profile>(defaultValue.profile);

  const refresh = async () => {
    try {
      const p = await fetchProfile();
      setProfile(p);
    } catch (e) {
      setProfile(defaultValue.profile);
    }
  };

  useEffect(() => {
    refresh();
  }, []);

  return <ProfileContext.Provider value={{ profile, refresh }}>{children}</ProfileContext.Provider>;
};

export function useProfile() {
  return useContext(ProfileContext);
}
