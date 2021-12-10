use project_dbms;

INSERT INTO app_linklession(id, time_phase, period_no)
VALUES
(1,"8.30-9.30", 1),
(2,"9.30-10.30",2),
(3,"10.30-11.30",3);

INSERT INTO app_linklession(id, time_phase, period_no)
VALUES
(4,"11.30-12.30",4),
(5,"12.30-13.30",5),
(6,"13.30-14.30",6),
(7,"14.30-15.30",7),
(8,"15.30-16.30",8),
(9,"16.30-17.30",9);

CREATE TABLE `app_post` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  -- `email_id` varchar(50) NOT NULL,
  `user_id_id` bigint(20) NOT NULL, 
  `post_text` varchar(500) NOT NULL,
  `upvotes` int(11) DEFAULT NULL,
  `downvotes` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_post_user_id_7d35b0b8` (`user_id_id`),
  CONSTRAINT `app_post_user_id_id_c31f0352_fk_app_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

CREATE TABLE `app_post` (
	email_id varchar(10) not null);

INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(1,'MONDAY', null ,null,null,1,'CSE','2024'),
(2,'MONDAY', 'ECB204','https://meet.google.com/mch-zvkw-gcq?authuser=0','Dr. NS Singha',2,'CSE','2024');
INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(3, 'MONDAY', 'ECB204', 'https://meet.google.com/mch-zvkw-gcq?authuser=0&hs=179', 'Dr. NS Singha',3,'CSE','2024');
INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(4, 'MONDAY', 'ECB204', 'https://meet.google.com/mch-zvkw-gcq?authuser=0&hs=179', 'Dr. NS Singha',4,'CSE','2024'),
(5, 'MONDAY', 'CSL201','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr. SHRUTI GUPTA',5,'CSE','2024');

INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(6, 'Tuesday', 'CSL201','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr. SHRUTI GUPTA',1,'CSE','2024');
INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(7,'WEDNESDAY', 'ECB204','https://meet.google.com/mch-zvkw-gcq?authuser=0','Dr. NS Singha',1,'CSE','2024');

INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(1,'MONDAY', null ,null,null,1,'CSE','2024'),
(2, 'TUESDAY', 'CSL201','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr. SHRUTI GUPTA',1,'CSE','2024'),
(3,'WEDNESDAY', 'ECB204','https://meet.google.com/mch-zvkw-gcq?authuser=0','Dr. NS Singha',1,'CSE','2024'),
(4,'THURSDAY', 'ECB206','https://meet.google.com/nst-jygs-kje?authuser=0&hs=179','Dr. Harikesh',1,'CSE','2024'),
(5,'FRIDAY', null, null, null,1,'CSE','2024');

INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(6, 'MONDAY','ECB204','https://meet.google.com/mch-zvkw-gcq?authuser=0','Dr NS Singha', 2,'CSE' ,'2024'),
(7,'TUESDAY', 'MAL241','https://meet.google.com/jqb-bomy-cqo?authuser=0','Dr. P. Kumar',2,'CSE','2024'),
(8,'WEDNESDAY',NULL, null, null,2,'CSE',2024),
(9,'THURSDAY', null,null,null,2,'CSE','2024'),
(10,'FRIDAY', NULL, NULL, NULL,2,'CSE','2024');

INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(11, 'MONDAY','ECB204 G1+G2','https://meet.google.com/mch-zvkw-gcq?authuser=0','Dr NS Singha', 3,'CSE' ,2024),
(12,'TUESDAY','CSB202 G2','https://meet.google.com/tyh-qyfz-ekk?authuser=0','Dr S. Sachdeva',3,'CSE','2024'),
(13,'WEDNESDAY','CSL201','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr. SHRUTI GUPTA',3,'CSE','2024'),
(14,'THURSADAY',null, null, null,3,'CSE','2024'),
(15,'FRIDAY','CSL203','https://meet.google.com/hiv-jjae-pvo?authuser=0&hs=179', 'Dr. Rohini Mahajan',3,'CSE','2024');

INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(16, 'MONDAY','ECB204 G1+G2','https://meet.google.com/mch-zvkw-gcq?authuser=0','Dr NS Singha', 4,'CSE' ,2024),
(17,'TUESDAY','CSB202 G2','https://meet.google.com/tyh-qyfz-ekk?authuser=0','Dr S. Sachdeva',4,'CSE','2024'),
(18,'WEDNESDAY','CSL203','', 'Dr. Rohini Mahajan',4,'CSE','2024'),
(19,'THURSDAY', 'CSB202','https://meet.google.com/tyh-qyfz-ekk?authuser=0','Dr S. Sachdeva',4,'CSE','2024'),
(20,'FRIDAY', 'CSB202 G1','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr S. Sachdeva',4,'CSE','2024');

INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(21, 'MONDAY','CSL201','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr. SHRUTI GUPTA',5,'CSE','2024'),
(22,'TUESDAY','CSB202 G1','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr S. Sachdeva',5,'CSE','2024'),
(23, 'WEDNESDAY',NULL, NULL, NULL, 5 , 'CSE','2024'),
(24,'THRUSDAY',NULL,NULL,NULL,5,'CSE','2024'),
(25,'FRIDAY','CSB202 G1','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr S. Sachdeva',5,'CSE','2024');

INSERT INTO app_lesson(id, period_day, subject_id, gmeet_link, teacher_name, period_no_id,branch, year)
values
(26,'MONDAY',NULL,NULL,NULL,6,'CSE',2024),
(27,'TUESDAY',NULL,NULL,NULL,6,'CSE',2024),
(28,'WEDNESDAY',NULL,NULL,NULL,6,'CSE',2024),
(29,'THURDAY','CSL201','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr. SHRUTI GUPTA',6,'CSE','2024'),
(30,'FRIDAY', 'ECB204','https://meet.google.com/mch-zvkw-gcq?authuser=0','Dr. NS Singha',6,'CSE','2024'),
(31,'MONDAY','CSB202 ','https://meet.google.com/tvb-odii-kfu?authuser=0','Dr S. Sachdeva',7,'CSE','2024'),
(32,'TUESDAY','MAL241','https://meet.google.com/jqb-bomy-cqo?authuser=0','Dr. P. Kumar',7,'CSE','2024'),
(33,'WEDNESDAY','ECB206','https://meet.google.com/nst-jygs-kje?authuser=0&hs=179','Dr. Harikesh',7,'CSE','2024'),
(34,'THURSDAY','CSL203','https://meet.google.com/hiv-jjae-pvo?authuser=0&hs=179', 'Dr. Rohini Mahajan',7,'CSE','2024'),
(35,'FRIDAY', NULL,NULL,NULL,7,'CSE',2024),
(36,'MONDAY', NULL,NULL,NULL,8,'CSE',2024),
(37,'TUESDAY', 'ECB206','https://meet.google.com/nst-jygs-kje?authuser=0&hs=179','Dr. Harikesh',8,'CSE','2024'),
(38,'WEDNESDAY','MAL241','https://meet.google.com/jqb-bomy-cqo?authuser=0','Dr. P. Kumar',8,'CSE','2024'),
(39,'THURSDAY','MAL241','https://meet.google.com/jqb-bomy-cqo?authuser=0','Dr. P. Kumar',8,'CSE','2024'),
(40,'FRIDAY','ECB206 G1+G2','https://meet.google.com/nst-jygs-kje?authuser=0&hs=179','Dr. BALJIT KAUR',8,'CSE','2024'),
(41,'MONDAY', NULL,NULL,NULL,9,'CSE',2024),
(42,'TUESDAY','CSL203','https://meet.google.com/hiv-jjae-pvo?authuser=0&hs=179', 'Dr. Rohini Mahajan',9,'CSE','2024'),
(43,'WEDNESDAY', NULL,NULL,NULL,9,'CSE',2024),
(44,'THURSDAY', NULL,NULL,NULL,9,'CSE',2024),
(45,'FRIDAY', 'ECB206 G1+G2','https://meet.google.com/nst-jygs-kje?authuser=0&hs=179','Dr. BALJIT KAUR',9,'CSE','2024');

-- ````````````````````````

use project_dbms;
insert into app_department 
values
("CSE"),("ECE"),("EEE"),("HUM"),("ASC");
insert into app_course
values
("MAL241"),("ECB206"),("CSL201"),("CSB202"),("ECB204"),("CSL203"),("ECB201"),("EEL201"),
("ECB202"),("ECL203");
drop table app_course;
create table app_course(
ccode varchar(10), 
dept varchar(100),
primary key(ccode),
foreign key(dept) references app_department(dept));
create table pyq(
id int auto_increment primary key, 
q_year integer, 
link varchar(300),
ccode varchar(10),
foreign key(ccode) references app_course(ccode));
insert into app_course
value("CSB202","CSE");
insert into app_department values
("HUM"),("ASC");
insert into app_course
values
("MAL241","ASC"),("ECB206","ECE"),("CSL201","CSE"),("ECB204","ECE"),("CSL203","CSE"),("CSB202","CSE"),("ECB201","ECE"),("EEL201","EEE"),
("ECB202","ECE"),("ECL203","ECE");
alter table pyq add qtype char(2);
select * from pyq;
insert into app_apppyq(id, q_year, link, ccode_id, qtype)
value
(1,2019,"https://drive.google.com/file/d/1oj2lIKbvlKzf-88L4gqeYkvCcGLOs0v2/view?usp=sharing","MAL241","ES");
insert into app_apppyq(id, q_year, link, ccode_id, qtype)
values
(2,2019,"https://drive.google.com/file/d/1oj2lIKbvlKzf-88L4gqeYkvCcGLOs0v2/view?usp=sharing","MAL241","ES"),
(3,2018,"https://drive.google.com/file/d/1wOduct3a83F2d61vUPnxrGrTcxOHBlXZ/view?usp=sharing","MAL241","ES"),
(4,2018,"https://drive.google.com/file/d/1m_1TRSRcaQv7thFfqWy365ifncthFTM2/view?usp=sharing","MAL241","MS"),
(5,2019,"https://drive.google.com/file/d/1woaXQLez0BC5Sl8aDgQ5XVvIB80Z7EQI/view?usp=sharing","ECB206","ES"),
(6,2019,"https://drive.google.com/file/d/18VMgsK3-EuZt1RUOh7k8wOleHmh9kuBZ/view?usp=sharing","ECB206","MS"),
(7, 2018,"https://drive.google.com/file/d/1lamW80fk6rdnoiawygxX1Hql2oR_R10u/view?usp=sharing","ECB206","ES"),
(8, 2018,"https://drive.google.com/file/d/1lX9MIDK3NJWGckYCxP29XiOwusH0blUS/view?usp=sharing","ECB206","MS"),
(9,2019,"https://drive.google.com/file/d/12EKb_yDqraqjOxt5-WjlDtBr5mQB-hKc/view?usp=sharing","CSL201","ES"),
(10,2019,"https://drive.google.com/file/d/1IxIPfWHONliaRq5O0GnrVX2h-lSump0K/view?usp=sharing","CSL201","MS"),
(11,2018,"https://drive.google.com/file/d/1PYk6-0dWiIZUk6vcN0Yf3YKLF-SH4Tvk/view?usp=sharing","CSL201","ES"),
(12,2018,"https://drive.google.com/file/d/1Q0Kr65fAPmXzotOD8RYxcJcBb-UC4sbL/view?usp=sharing","CSL201","MS"),
(13,2019,"https://drive.google.com/file/d/16-2G5mXftykomRt7A4L26jqi4P-buGaO/view?usp=sharing","CSB202","ES"),
(14,2019,"https://drive.google.com/file/d/1fvn1Ora2QHJMLcpB2lGOxdAgCr6A2EMy/view?usp=sharing","CSB202","MS"),
(15,2018,"https://drive.google.com/file/d/1UNlzULDbNBB9AV2E9I5QUlmEmDDPrlcC/view?usp=sharing","CSB202","ES"),
(16,2018,"https://drive.google.com/file/d/1tStGHFJgj6M2iC2ANKGqZVfRsPJYCM-d/view?usp=sharing","CSB202","MS"),
(17,2019,"https://drive.google.com/file/d/1LjxjWjs48pg48qiZRO1W6MVrtXnY1kdV/view?usp=sharing","ECB204","ES"),
(18,2019,"https://drive.google.com/file/d/1p4-wzEVTlMmu_By2ozr59f3SejkvIEV0/view?usp=sharing","ECB204","MS"),
(19,2018,"https://drive.google.com/file/d/1ERnGM7IpVPpUowlhF-L3v7crr_BywWtH/view?usp=sharing","ECB204","ES"),
(20,2018,"https://drive.google.com/file/d/13ALuxoTyawL_y633z3utDrbD5tNpjUu2/view?usp=sharing","ECB204","MS"),
(21,2019," https://drive.google.com/file/d/1ghcZuFVriJTNnj6a7y0J5LR8otCdWdpR/view?usp=sharing","CSL203","ES"),
(22,2019,"https://drive.google.com/file/d/1s4kVL7Y01gNzCw8gBoEA-56pJkUWgssq/view?usp=sharing ","CSL203","MS"),
(23,2018,"https://drive.google.com/file/d/1Zb_3-jZzFsiyO6sbZDXllVuMyf2hMgM6/view?usp=sharing ","CSL203","ES"),
(24,2018,"https://drive.google.com/file/d/1es4M7vCsVbpX23qg-JThxoS2uy2M_c6A/view?usp=sharing ","CSL203","MS"),
(25,2019,"https://drive.google.com/file/d/1qMuqmtgYAufx-0STmMeH4OQKj9PUeH2n/view?usp=sharing","ECB201","ES"),
(26,2019,"https://drive.google.com/file/d/15LxuHvytrLiehN5v60COH18tOxhZS8oy/view?usp=sharing","ECB201","MS"),
(27,2018,"https://drive.google.com/file/d/1VG4oAKUeKxFYYVk_IcOooY0l_lI6icuz/view?usp=sharing","ECB201","ES"),
(28,2018,"https://drive.google.com/file/d/100_oZBQQ-Ps5_u9pa3YDMlgYNMietvee/view?usp=sharing","ECB201","MS"),
(29,2019,"https://drive.google.com/file/d/1NIidiM440YLyth-YcQTKVL2mzfbvaLRI/view?usp=sharing","EEL201","ES"),
(30,2019,"https://drive.google.com/file/d/1UZXiMDeQM8CQM9f7X9CJCDNOP9TlZesW/view?usp=sharing","EEL201","MS"),
(31,2018,"https://drive.google.com/file/d/1QtZ6z89tNF8ThynCGv6uVrMZ6hUlhSsT/view?usp=sharing","EEL201","ES"),
(32,2018,"https://drive.google.com/file/d/1JrP-VNzxeYTndXTI6WtOhxtgscf7HGwL/view?usp=sharing","EEL201","MS"),
(33,2019,"https://drive.google.com/file/d/1gJbyr9zbWGSvNARyx53T_eJF-7ux23WV/view?usp=sharing","ECB202","ES"),
(34,2019,"https://drive.google.com/file/d/1KqzNp5jvZW6I_jDINlwA0ehcF66FmfVd/view?usp=sharing","ECB202","MS"),
(35,2018,"https://drive.google.com/file/d/1OlchpYEVoNX5fsR6alLD20Z7FhYROOPf/view?usp=sharing","ECB202","ES"),
(36,2018,"https://drive.google.com/file/d/1JXMPaEG_5jrb_RPMUrPSxC0lgpyu0RSy/view?usp=sharing","ECB202","MS"),
(37,2019,"https://drive.google.com/file/d/1tPu0tzol1KT4VmIh9PwnDTvx5y6mhGC2/view?usp=sharing","ECL203","ES"),
(38,2019,"https://drive.google.com/file/d/1LNpwVu6vFjH-BbH1TJaO2fBEew3_Bkr1/view?usp=sharing","ECL203","MS"),
(39,2018,"https://drive.google.com/file/d/12I_hpnurvlbx_htmnq63QlGgJMdpRzf8/view?usp=sharing","ECL203","ES"),
(40,2018,"https://drive.google.com/file/d/1BuYj_BLA6j4DmF6HKXvpVba2B6MGL_c2/view?usp=sharing","ECL203","MS");

drop table app_department;
select * from app_department;
insert into app_timetable values
(1,"CSE",null,2024),(2,"ECE",null,2024);
select * from app_timetable_days;
insert into app_timetable_days(id,day,time_from,tt_id_id,course_id,time_to)
values(1,"Monday","09:30",1,"ECB204","10:30"),(2,"Monday","10:30",1,"ECB204","12:30"),(3,"Monday","12:30",1,"CSL201","13:30"),
(4,"Monday","14:30",1,"CSB202","15:30"),(5,"Monday","15:30",1,"CSL203","16:30"),(6,"Tuesday","08:30",1,"CSL201","09:30"),(7,"Tuesday","09:30",1,"MAL241","10:30"),(8,"Tuesday","10:30",1,"CSB202","13:30"),(9,"Tuesday","14:30",1,"MAL241","15:30"),
(10,"Tuesday","15:30",1,"ECB206","16:30"),(11,"Tuesday","16:30",1,"CSL203","17:30"),(12,"Wednesday","08:45",1,"ECB204","09:30"),
(13,"Wednesday","10:15",1,"CSL201","11:00"),(14,"Wednesday","13:15",1,"ECB206","14:00"),(15,"Wednesday","13:15",1,"MAL241","14:00"),
(16,"Thursday","08:30",1,"ECB206","09:30"),(17,"Thursday","11:30",1,"CSB202","12:30"),(18,"Thursday","13:30",1,"CSL201","14:30"),(19,"Thursday","14:30",1,"CSL203","15:30"),(20,"Thursday","15:30",1,"MAL241","16:30"),
(21,"Friday","10:30",1,"CSL203","11:30"),(22,"Friday","11:30",1,"CSB202","13:30"),(23,"Friday","13:30",1,"ECB204","14:30"),(24,"Friday","14:30",1,"ECB206","15:30");
select * from app_register_user;

use project_dbms;

SELECT app_todo.todo_text, app_todo.reminder_date, app_user.email, app_user.username
FROM app_todo 
INNER JOIN app_user on app_todo.user_id_id = app_user.id;

SELECT app_user.username, app_user.email, app_post.post_text
FROM app_user
INNER JOIN app_post ON app_post.user_id_id = app_user.id;