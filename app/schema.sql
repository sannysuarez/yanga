DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstname VARCHAR(100) NOT NULL,
  lastname VARCHAR(100),
  email VARCHAR(150) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  state VARCHAR(100) NOT NULL,
  tel VARCHAR(20) NOT NULL,
  gender VARCHAR(10) NOT NULL,
  google_id VARCHAR(255) UNIQUE,
  profile_pic VARCHAR(255),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );