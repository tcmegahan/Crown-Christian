import React, { useState } from 'react';
import CurriculumList from './CurriculumList';
import LessonPlanEditor from './LessonPlanEditor';
import CurriculumEditor from './CurriculumEditor';
import LessonPlanDetail from './LessonPlanDetail';
import LessonPlanList from './LessonPlanList';

export default function Dashboard() {
  const [view, setView] = useState<{ name: string; id?: string }>({ name: 'home' });

  function openCurriculumEditor(id?: string) {
    setView({ name: 'curriculum-editor', id });
  }
  function openLessonDetail(id: string) {
    setView({ name: 'lesson-detail', id });
  }

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Welcome to the Crown Christian School Management Dashboard.</p>
      {view.name === 'home' && (
        <div>
          <CurriculumList />
          <button onClick={() => openCurriculumEditor()}>New Curriculum</button>
          <LessonPlanEditor />
          <LessonPlanList onOpen={(id) => openLessonDetail(id)} />
        </div>
      )}
      {view.name === 'curriculum-editor' && (
        <CurriculumEditor id={view.id} onSaved={() => setView({ name: 'home' })} />
      )}
      {view.name === 'lesson-editor' && <LessonPlanEditor />}
      {view.name === 'lesson-detail' && view.id && (
        <LessonPlanDetail id={view.id} onSaved={() => setView({ name: 'home' })} />
      )}
    </div>
  );
}
