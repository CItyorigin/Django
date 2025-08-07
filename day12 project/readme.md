# Django Restaurant Review Project

This is a sample Django project for a restaurant review app, originally developed on macOS. This version is cleaned up and ready for use on **Windows**.

## ✅ Requirements

- Python 3.10+
- pip
- virtualenv (or `python -m venv`)

## 🚀 How to Run (Windows)

1. Create virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start the server

```bash
python manage.py runserver
```

## 📁 Media & Static Files

Make sure your `settings.py` includes:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

## 📦 Project Structure

- `config/`: Django settings and urls
- `restaurants/`: Restaurant app
- `reviews/`: Review app
- `users/`: Custom user app

---

This version is cleaned for cross-platform compatibility.
