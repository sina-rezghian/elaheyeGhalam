# Elaheye Ghalam

Persian Django website for Elaheye Ghalam Parsian. Requires Python 3.10–3.14.

From the repository root on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\ElaheyeGhalam\requirements.txt
cd ElaheyeGhalam
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py runserver 8001
```

Open http://127.0.0.1:8001/. Port 8001 avoids conflicting with other local projects on port 8000.

All styles, scripts, and illustrations are in `ElaheyeGhalam/site1/static/site1/` and are served automatically by Django's development server. No Node.js, Bootstrap CDN, or `collectstatic` step is needed for local development.

The original repository did not include its referenced logos, banners, photographs, CSS, JavaScript, or catalog pages. The repaired site includes local replacement illustrations and preserves the original service categories, company description, contact details, and social links. Add original brand artwork and catalog files here when available.

Run checks with `..\.venv\Scripts\python.exe manage.py check` and `..\.venv\Scripts\python.exe manage.py test` from the Django directory.
