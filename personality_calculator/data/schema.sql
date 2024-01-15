CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    enneagram INTEGER NOT NULL,
    chinese_zodiac TEXT NOT NULL,
    western_zodiac TEXT NOT NULL,
    physical INTEGER NOT NULL,
    emotional INTEGER NOT NULL,
    intellectual INTEGER NOT NULL
)