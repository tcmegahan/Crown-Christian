import React, { useEffect, useState } from 'react';
import { getCurriculums, Curriculum } from '../lib/api';

export default function CurriculumList() {
  const [items, setItems] = useState<Curriculum[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
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

  if (loading) return <div>Loading curriculums...</div>;
  if (error) return <div>Error: {error}</div>;
  return (
    <div>
      <h3>Curriculums</h3>
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
