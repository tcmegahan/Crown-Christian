import React, { useEffect, useState } from 'react';
import { getCurriculums, createLessonPlanAPI, Curriculum } from '../lib/api';

export default function LessonPlanEditor() {
  const [curriculums, setCurriculums] = useState<Curriculum[]>([]);
  const [title, setTitle] = useState('');
  const [curriculumId, setCurriculumId] = useState<string | undefined>(undefined);
  const [objectives, setObjectives] = useState('');
  const [activities, setActivities] = useState('');
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    getCurriculums()
      .then(setCurriculums)
      .catch(() => {});
  }, []);

  async function save() {
    setSaving(true);
    try {
      const payload = { title, curriculum_id: curriculumId, objectives, activities };
      await createLessonPlanAPI(payload);
      alert('Lesson plan created');
      setTitle('');
      setObjectives('');
      setActivities('');
    } catch (e) {
      alert(String(e));
    }
    setSaving(false);
  }

  return (
    <div>
      <h3>Create Lesson Plan</h3>
      <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" />
      <select value={curriculumId} onChange={(e) => setCurriculumId(e.target.value || undefined)}>
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
        Save
      </button>
    </div>
  );
}
