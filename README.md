# 💊 MedRemind — Medicine Reminder Web App

A full-stack Django web application with a stunning 3D glassmorphism UI.

## Tech Stack
- **Backend**: Django 6.x, Python 3
- **Database**: SQLite (default)
- **Frontend**: HTML5, Custom CSS (3D effects, glassmorphism), Vanilla JS
- **Notifications**: Browser Notification API (no external services)

## Project Structure
```
medreminder/
├── accounts/          # Auth: register, login, logout
├── medicines/         # CRUD for medicines
├── reminders/         # CRUD for reminders + toggle
├── dashboard/         # Main dashboard view
├── templates/         # All HTML templates
│   ├── base.html
│   ├── accounts/
│   ├── medicines/
│   ├── reminders/
│   └── dashboard/
├── static/
│   ├── css/styles.css   # 3D + glassmorphism + animations
│   └── js/notifications.js  # Browser notification system
└── manage.py
```

## Quick Start

```bash
# 1. Clone / extract project
cd medreminder

# 2. Install Django
pip install django

# 3. Run migrations
python manage.py migrate

# 4. (Optional) Create superuser
python manage.py createsuperuser

# 5. Start server
python manage.py runserver

# 6. Open browser
#    http://127.0.0.1:8000/
```

## Features
- ✅ User registration & login (Django auth)
- ✅ Add/Edit/Delete medicines (name + dosage)
- ✅ Set multiple time-based reminders per medicine
- ✅ Toggle reminders active/paused
- ✅ Dashboard with live clock + active reminder cards
- ✅ Browser push notifications (checks every minute)
- ✅ 3D glassmorphism UI with floating medical artifacts
- ✅ 3D tilt effect on hover (mousemove perspective)
- ✅ Floating pill, sphere, cross, ring animations
- ✅ Responsive mobile layout

## UI Design Notes
- **Glassmorphism**: backdrop-filter blur + rgba backgrounds
- **3D Cards**: CSS perspective + rotateX/Y on mousemove
- **Hero**: CSS-only rotating sphere (no Three.js dependency needed)
- **Artifacts**: Pure CSS pills, spheres, crosses, rings
- **Theme**: Dark space gradient + indigo/cyan accent palette

## Notification Logic
- Checks current time every 60 seconds
- Compares against all active reminder times (HH:MM)
- Shows browser notification if permission granted
- Falls back to in-app toast if permission denied
- Prevents duplicate alerts using a JavaScript Set per session
