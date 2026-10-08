import os

API_KEY = os.environ.get("YOUTUBE_API_KEY", "").strip()

KEYWORDS = [
    # Español (general)
    "mujeres en tecnología",
    "mujeres en tech",
    "mujeres programadoras",
    "mujeres ingenieras",
    "mujeres en informática",
    "mujeres en software",
    "mujeres en inteligencia artificial",
    "mujeres en ciberseguridad",
    "mujeres en ciencia de datos",
    "mujeres en STEM",
    "brecha de género en tecnología",
    "diversidad en tecnología",
    "inclusión en tecnología",
    "igualdad en STEM",
    "chicas en tecnología",
    "mujeres que inspiran",

    # Inglés (general)
    "women in technology",
    "women in tech",
    "female programmers",
    "women engineers",
    "women in computer science",
    "women in software",
    "women in artificial intelligence",
    "women in cybersecurity",
    "women in data science",
    "women in STEM",
    "gender gap in technology",
    "diversity in technology",
    "inclusion in technology",
    "women role models in tech",

    # Comunidades / eventos
    "Girls Who Code",
    "Women Techmakers",
    "Women in Data Science",
    "Ada Lovelace Day",
    "Grace Hopper Celebration",
    "AnitaB.org",
    "She Codes",
    "Technovation Girls"
]

MAX_RESULTS = 50  # puedes subir hasta 50
