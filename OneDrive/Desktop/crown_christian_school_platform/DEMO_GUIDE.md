# Crown Christian School Platform Demo Guide

This guide walks you through the main features and workflows of the Crown Christian School Platform using comprehensive demo data. Use this as a script for investor presentations or onboarding.

---

## 1. Accessing the Platform

- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the dashboard.
- Log in to the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) with your admin credentials.

## 2. Dashboard Highlights

- View total students, tuition, aid awarded, and donations.
- See recent discipline incidents for quick insights.

## 3. Student Management

- Browse and search students by name or grade.
- View and edit student details, guardians, and enrollments.

## 4. Admissions

- Review applications for PK3-12.
- Track status: Received, Review, Accepted, Waitlist, Declined.

## 5. Staff & Teachers

- View staff directory (administrators, principal, teachers by grade).
- Edit staff roles and contact info.

## 6. Curriculum & Enrollments

- Explore courses by grade band.
- See student enrollments for the current year.

## 7. Events

- Browse upcoming and past school events.
- View event details: title, date, location, description.

## 8. Communications

- Review sent messages (Email, SMS, Teams).
- Check subjects, bodies, and sent dates.

## 9. Devotions

- Access daily/weekly devotion entries with scripture and content.

## 10. Finance & Aid

- View finance records (tuition, fees, payments).
- Review financial aid applications and awards.

## 11. Discipline

- Track discipline incidents by student, type, and notes.

---

## Backup & Restore

- To backup the database, copy `db.sqlite3` to `backups/`.
- To restore, replace `db.sqlite3` with your backup file.

## Deployment

- For local demo, use `python manage.py runserver`.
- For Docker, use `docker compose up --build`.

## Technical Readiness

- All dependencies are listed in `requirements.txt`.
- Environment variables are loaded from `.env`.
- All code and data are isolated to this workspace.

---

## Demo Script Example

1. Start at the dashboard and highlight key metrics.
2. Show student and guardian management.
3. Walk through an admissions application.
4. Introduce staff and teacher directory.
5. Explore curriculum and enrollments.
6. Present events and communications.
7. Review devotions and spiritual content.
8. Demonstrate finance and aid workflows.
9. Show discipline tracking and reporting.
10. End with admin panel features and search/filter capabilities.

---

## Technical Notes

- All data is mock/demo for presentation purposes.
- Admin panel allows full CRUD operations for all modules.
- UI/UX is modern, mobile-friendly, and branded.

---

## Next Steps

- Backup code and database before making further changes.
- Prepare for deployment if remote access is needed.

---

python [manage.py](http://_vscodecontentref_/0) runserver

For questions or support, contact the development team.
