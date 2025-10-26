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
