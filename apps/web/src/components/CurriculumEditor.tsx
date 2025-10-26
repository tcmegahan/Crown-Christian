/* eslint-disable no-unused-vars */
import React, { useEffect, useState } from 'react';
import { getCurriculumById, updateCurriculum, createCurriculumAPI } from '../lib/api';
import { useProfile } from '../lib/ProfileContext';

export default function CurriculumEditor({
  id,
  onSaved,
}: {
  id?: string;
  onSaved?: (c: any) => void;
}) {
  const { profile } = useProfile();
  const canEdit =
    profile.authenticated && profile.permissions && profile.permissions.includes('edit_curriculum');
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (id) {
      setLoading(true);
      getCurriculumById(id)
        .then((curr) => {
          setName(curr.name);
          setDescription(curr.description || '');
        })
        .finally(() => setLoading(false));
    }
  }, [id]);

  async function save() {
    if (!canEdit) {
      alert('You do not have permission to perform this action.');
      return;
    }
    setLoading(true);
    try {
      if (id) {
        const updated = await updateCurriculum(id, { name, description });
        onSaved && onSaved(updated);
      } else {
        const created = await createCurriculumAPI(name, description);
        onSaved && onSaved(created);
      }
    } catch (e) {
      alert(String(e));
    }
    setLoading(false);
  }

  if (!canEdit) return <div>You do not have permission to create or edit curriculums.</div>;

  return (
    <div>
      <h3>{id ? 'Edit Curriculum' : 'New Curriculum'}</h3>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Description"
      />
      <button onClick={save} disabled={loading || !name}>
        {id ? 'Save' : 'Create'}
      </button>
    </div>
  );
}
