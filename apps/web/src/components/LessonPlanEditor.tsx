/* eslint-disable no-unused-vars */
import React, { useEffect, useState } from 'react';
import {
  getCurriculums,
  createLessonPlanAPI,
  getLessonPlanById,
  updateLessonPlan,
  Curriculum,
} from '../lib/api';
import { useProfile } from '../lib/ProfileContext';

export default function LessonPlanEditor({
  id,
  onSaved,
}: {
  id?: string;
  onSaved?: (lp: any) => void;
}) {
  const { profile } = useProfile();
  const canEdit =
    profile.authenticated && profile.permissions && profile.permissions.includes('edit_curriculum');
  const [curriculums, setCurriculums] = useState<Curriculum[]>([]);
  const [title, setTitle] = useState('');
  const [curriculumId, setCurriculumId] = useState<string | undefined>(undefined);
  const [objectives, setObjectives] = useState('');
  const [activities, setActivities] = useState('');
  const [saving, setSaving] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    getCurriculums()
      .then(setCurriculums)
      .catch(() => {});
  }, []);

  useEffect(() => {
    if (id) {
      setLoading(true);
      getLessonPlanById(id)
        .then((lp) => {
          setTitle(lp.title || '');
          setObjectives(lp.objectives || '');
          setActivities(lp.activities || '');
          setCurriculumId(lp.curriculum?.curriculum_id);
        })
        .catch(() => {})
        .finally(() => setLoading(false));
    }
  }, [id]);

  async function save() {
    if (!canEdit) {
      alert('You do not have permission to perform this action.');
      return;
    }
    setSaving(true);
    try {
      if (id) {
        const updated = await updateLessonPlan(id, {
          title,
          curriculum_id: curriculumId || null,
          objectives,
          activities,
        });
        onSaved && onSaved(updated);
      } else {
        const payload = { title, curriculum_id: curriculumId, objectives, activities };
        const created = await createLessonPlanAPI(payload);
        onSaved && onSaved(created);
      }
    } catch (e) {
      alert(String(e));
    }
    setSaving(false);
  }

  if (!canEdit) return <div>You do not have permission to create or edit lesson plans.</div>;

  if (loading) return <div>Loading...</div>;
  return (
    <div>
      <h3>{id ? 'Edit Lesson Plan' : 'Create Lesson Plan'}</h3>
      <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" />
      <select
        value={curriculumId || ''}
        onChange={(e) => setCurriculumId(e.target.value || undefined)}
      >
        <option value="">(No curriculum)</option>
        {curriculums.map((c) => (
          <option key={c.curriculum_id} value={c.curriculum_id}>
            {c.name}
          </option>
        ))}
      </select>
      <textarea
        value={objectives}
        onChange={(e) => setObjectives(e.target.value)}
        placeholder="Objectives"
      />
      <textarea
        value={activities}
        onChange={(e) => setActivities(e.target.value)}
        placeholder="Activities"
      />
      <button onClick={save} disabled={saving || !title}>
        {id ? 'Save' : 'Create'}
      </button>
    </div>
  );
}
