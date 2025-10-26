import React, { useEffect, useState } from 'react';
import { getCurriculums, Curriculum } from '../lib/api';
import { getProfile } from '../lib/auth';

export default function CurriculumList() {
  const [items, setItems] = useState<Curriculum[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [profile, setProfile] = useState<any>({
    authenticated: false,
    roles: [],
    permissions: [],
  });

  useEffect(() => {
    getProfile()
      .then((p) => setProfile(p))
      .catch(() => {});
    getCurriculums()
      .then((data) => {
        setItems(data);
        setLoading(false);
      })
      .catch((e) => {
        setError(String(e));
        setLoading(false);
      });
  }, []);

  const canEdit =
    profile.authenticated && profile.permissions && profile.permissions.includes('edit_curriculum');

  async function createCurriculum() {
    const name = prompt('Name for new curriculum');
    if (!name) return;
    const res = await fetch('/api/academics/curriculums/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name }),
    });
    if (res.ok) {
      const data = await res.json();
      setItems([data, ...items]);
    }
  }

  if (loading) return <div>Loading curriculums...</div>;
  if (error) return <div>Error: {error}</div>;
  return (
    <div>
      <h3>Curriculums</h3>
      {canEdit && <button onClick={createCurriculum}>New Curriculum</button>}
      <ul>
        {items.map((c) => (
          <li key={c.curriculum_id}>
            {c.name} - {c.description}
          </li>
        ))}
      </ul>
    </div>
  );
}
