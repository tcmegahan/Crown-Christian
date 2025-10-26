/* eslint-disable no-unused-vars */
import React, { useEffect, useState } from 'react';
import { getLessonPlans } from '../lib/api';
import { getProfile } from '../lib/auth';

type Props = { onOpen: (id: string) => void };

export default function LessonPlanList({ onOpen }: Props) {
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [profile, setProfile] = useState<any>({ authenticated: false, roles: [], permissions: [] });

  useEffect(() => {
    getProfile()
      .then((p) => setProfile(p))
      .catch(() => {});
    getLessonPlans()
      .then((data) => {
        setItems(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const canEdit =
    profile.authenticated && profile.permissions && profile.permissions.includes('edit_curriculum');

  if (loading) return <div>Loading lesson plans...</div>;
  return (
    <div>
      <h3>Lesson Plans</h3>
      <ul>
        {items.map((lp) => (
          <li key={lp.lesson_id}>
            <strong>{lp.title}</strong> {lp.curriculum ? `(${lp.curriculum.name})` : ''}
            {canEdit && (
              <button
                aria-label={`Edit ${lp.title}`}
                onClick={() => onOpen(lp.lesson_id)}
                style={{ marginLeft: 8 }}
              >
                Edit
              </button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
