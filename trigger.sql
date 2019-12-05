CREATE TRIGGER insert_user_info
AFTER INSERT ON auth_user
FOR EACH ROW
INSERT INTO safenet_user_info 
SELECT id, username ,email , MD5(password)
FROM auth_user ORDER BY id DESC LIMIT 1;
