/* eslint-disable no-unused-vars */
import React, { useEffect, useState } from 'react';
import { getCurriculumById, updateCurriculum, createCurriculumAPI } from '../lib/api';

export default function CurriculumEditor({
  id,
  onSaved,
}: {
  id?: string;
  onSaved?: (c: any) => void;
}) {
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
