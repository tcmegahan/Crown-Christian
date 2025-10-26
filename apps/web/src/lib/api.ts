export async function fetchJSON<T>(url: string): Promise<T> {
  const res = await fetch(url, { credentials: 'same-origin' });
  if (!res.ok) throw new Error(`Failed to fetch ${url}: ${res.status}`);
  return (await res.json()) as T;
}

export type Curriculum = {
  curriculum_id: string;
  name: string;
  description?: string;
};

export type LessonPlan = {
  lesson_id: string;
  title: string;
  objectives?: string;
  activities?: string;
  created_on?: string;
  curriculum?: Curriculum;
};

export async function getCurriculums(): Promise<Curriculum[]> {
  return fetchJSON<Curriculum[]>('/api/academics/curriculums/');
}

export async function getLessonPlans(): Promise<LessonPlan[]> {
  return fetchJSON<LessonPlan[]>('/api/academics/lessonplans/');
}

export async function createCurriculumAPI(name: string, description = ''): Promise<Curriculum> {
  const res = await fetch('/api/academics/curriculums/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, description }),
    credentials: 'same-origin',
  });
  if (!res.ok) throw new Error(`Failed to create curriculum: ${res.status}`);
  return (await res.json()) as Curriculum;
}

export async function createLessonPlanAPI(payload: {
  title: string;
  curriculum_id?: string;
  objectives?: string;
  activities?: string;
}): Promise<LessonPlan> {
  const res = await fetch('/api/academics/lessonplans/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'same-origin',
  });
  if (!res.ok) throw new Error(`Failed to create lesson plan: ${res.status}`);
  return (await res.json()) as LessonPlan;
}

export async function getCurriculumById(id: string): Promise<Curriculum> {
  return fetchJSON<Curriculum>(`/api/academics/curriculums/${id}/`);
}

export async function updateCurriculum(
  id: string,
  payload: { name?: string; description?: string },
): Promise<Curriculum> {
  const res = await fetch(`/api/academics/curriculums/${id}/`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'same-origin',
  });
  if (!res.ok) throw new Error(`Failed to update curriculum: ${res.status}`);
  return (await res.json()) as Curriculum;
}

export async function getLessonPlanById(id: string): Promise<LessonPlan> {
  return fetchJSON<LessonPlan>(`/api/academics/lessonplans/${id}/`);
}

export async function updateLessonPlan(
  id: string,
  payload: {
    title?: string;
    objectives?: string;
    activities?: string;
    curriculum_id?: string | null;
  },
): Promise<LessonPlan> {
  const res = await fetch(`/api/academics/lessonplans/${id}/`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'same-origin',
  });
  if (!res.ok) throw new Error(`Failed to update lesson plan: ${res.status}`);
  return (await res.json()) as LessonPlan;
}
