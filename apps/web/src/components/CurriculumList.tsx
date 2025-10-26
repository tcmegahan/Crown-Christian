import React, { useEffect, useState } from 'react';
import { getCurriculums, Curriculum, createCurriculumAPI } from '../lib/api';
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
  const [creating, setCreating] = useState(false);
  const [newName, setNewName] = useState('');

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
    if (!newName) return;
    setCreating(true);
    try {
      const data = await createCurriculumAPI(newName);
      setItems([data, ...items]);
      setNewName('');
    } catch (e) {
      alert(String(e));
    }
    setCreating(false);
  }

  if (loading) return <div>Loading curriculums...</div>;
  if (error) return <div>Error: {error}</div>;
  return (
    <div>
      <h3>Curriculums</h3>
      {canEdit && (
        <div>
          <input
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
            placeholder="New curriculum name"
          />
          <button onClick={createCurriculum} disabled={creating || !newName}>
            Create
          </button>
        </div>
      )}
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
