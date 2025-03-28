- Run `pip install python-decouple` to be to load environment variables from a `.env`
- Run `pip freeze > requirements.txt` to generate all required dependencies
---
- Run `python manage.py collectstatic --noinput` to collect static files after this configuration in settingd
```bash
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

```
---

