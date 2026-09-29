-- initialize.sql
-- Lab 04: users and posts with a primary key / foreign key relationship
 
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
 
CREATE TABLE users (
    user_id     INT PRIMARY KEY,
    username    VARCHAR(50)  NOT NULL,
    email       VARCHAR(100) NOT NULL,
    created_at  DATETIME     NOT NULL
);
 
CREATE TABLE posts (
    post_id     INT PRIMARY KEY,
    user_id     INT          NOT NULL,
    title       VARCHAR(100) NOT NULL,
    body        TEXT,
    posted_at   DATETIME     NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
 
-- 10 users
INSERT INTO users (user_id, username, email, created_at) VALUES (1, 'alice',   'alice@example.com',   '2026-01-05 09:15:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (2, 'bob',     'bob@example.com',     '2026-01-12 14:30:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (3, 'carla',   'carla@example.com',   '2026-02-01 11:00:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (4, 'dmitri',  'dmitri@example.com',  '2026-02-14 16:45:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (5, 'elena',   'elena@example.com',   '2026-03-03 08:20:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (6, 'farid',   'farid@example.com',   '2026-03-21 19:05:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (7, 'grace',   'grace@example.com',   '2026-04-09 10:10:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (8, 'hiro',    'hiro@example.com',    '2026-05-17 13:25:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (9, 'isabel',  'isabel@example.com',  '2026-06-02 17:40:00');
INSERT INTO users (user_id, username, email, created_at) VALUES (10, 'jamal',  'jamal@example.com',   '2026-07-30 12:00:00');
 
-- 10 posts (user_id values all reference existing users)
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (1,  1,  'Hello World',          'My first post on this site!',                  '2026-01-06 10:00:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (2,  1,  'Favorite Coffee Spots', 'Here are my top three cafes near campus.',     '2026-01-20 08:30:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (3,  2,  'Learning SQL',         'Joins are confusing but getting clearer.',     '2026-01-15 15:00:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (4,  3,  'Weekend Hike',         'Went up the mountain trail, great views.',     '2026-02-08 18:20:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (5,  4,  'Study Tips',           'Spaced repetition really works.',              '2026-02-20 09:45:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (6,  5,  'Book Recommendations', 'Three novels I could not put down.',            '2026-03-05 20:10:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (7,  6,  'Cooking Experiment',   'Tried making fresh pasta from scratch.',       '2026-03-25 12:30:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (8,  7,  'Project Update',       'Our team finished the database design.',       '2026-04-12 14:00:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (9,  8,  'Photography Basics',   'Notes on aperture, shutter speed, and ISO.',   '2026-05-20 16:15:00');
INSERT INTO posts (post_id, user_id, title, body, posted_at) VALUES (10, 9,  'Summer Plans',         'Looking for internship advice and ideas.',     '2026-06-10 11:50:00');
