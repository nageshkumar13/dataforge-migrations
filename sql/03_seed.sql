INSERT INTO dataforge.users (name,email)
VALUES
('Rahul','rahul@test.com'),
('Dev','dev@test.com')
ON CONFLICT DO NOTHING;