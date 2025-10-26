/* eslint-disable no-unused-vars */
import React, { useEffect, useState } from 'react';
import { getLessonPlanById, updateLessonPlan } from '../lib/api';

export default function LessonPlanDetail({
  id,
  onSaved,
}: {
  id: string;
  onSaved?: (lp: any) => void;
}) {
  const [lp, setLp] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    getLessonPlanById(id)
      .then((data) => setLp(data))
      .finally(() => setLoading(false));
  }, [id]);

  async function save() {
    try {
      const updated = await updateLessonPlan(id, {
        title: lp.title,
        objectives: lp.objectives,
        activities: lp.activities,
        curriculum_id: lp.curriculum?.curriculum_id || null,
      });
      setLp(updated);
      onSaved && onSaved(updated);
    } catch (e) {
      alert(String(e));
    }
  }

  if (loading) return <div>Loading...</div>;
  return (
    <div>
      <h3>Lesson Plan: {lp?.title}</h3>
      <input value={lp?.title || ''} onChange={(e) => setLp({ ...lp, title: e.target.value })} />
      <textarea
        value={lp?.objectives || ''}
        onChange={(e) => setLp({ ...lp, objectives: e.target.value })}
      />
      <textarea
        value={lp?.activities || ''}
        onChange={(e) => setLp({ ...lp, activities: e.target.value })}
      />
      <button onClick={save}>Save</button>
    </div>
  );
}
