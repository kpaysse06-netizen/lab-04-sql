-- media_query.sql
-- Posts written in 2026 from March onward, with the author's username and email
 
SELECT
    users.username,
    users.email,
    posts.title,
    posts.posted_at
FROM posts
INNER JOIN users
    ON posts.user_id = users.user_id
WHERE posts.posted_at >= '2026-03-01 00:00:00'
ORDER BY posts.posted_at;
