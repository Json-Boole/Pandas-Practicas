INSERT INTO roles (name)
VALUES
('User'),
('Vendedor'),
('Admin');



INSERT INTO user (email, first_name, last_name, password, address, date_joined, is_active, is_staff, is_superuser, role_id) 
VALUES 


('marcovirinni@gmail.com', 'Marcoa', 'Virinni', 'pbkdf2_sha256$600000$0tpRVCb7Lhck7nuwn1d1j4$y7Yq+UqpPNDzzuaJdaJEPRtQEeJozkQF6SFWDLu6kK0=', '123 Main St',  '2024-05-23 16:00:04', true, true, false, 2), 

('perfiles_admin@gmail.com', 'Admin', 'Team','pbkdf2_sha256$600000$eqo3klH506j3K7Mhhm5PtE$xajzovu8ExldoIETGBZEIEw5vUDQZT9WdQJKtkLwYQE=', 'localhost',  '2024-05-23 16:00:04', true, true, true, 3);
