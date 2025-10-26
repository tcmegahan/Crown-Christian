import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import { ProfileProvider } from './lib/ProfileContext';

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ProfileProvider>
      <App />
    </ProfileProvider>
  </React.StrictMode>,
);
