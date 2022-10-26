--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 14.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'ru_RU.UTF-8';


ALTER DATABASE postgres OWNER TO postgres;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: db_info; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA db_info;


ALTER SCHEMA db_info OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: course; Type: TABLE; Schema: db_info; Owner: postgres
--

CREATE TABLE db_info.course (
    course_id integer NOT NULL,
    name_course character varying(30) NOT NULL,
    group_id integer
);


ALTER TABLE db_info.course OWNER TO postgres;

--
-- Name: course_id_seq; Type: SEQUENCE; Schema: db_info; Owner: postgres
--

CREATE SEQUENCE db_info.course_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE db_info.course_id_seq OWNER TO postgres;

--
-- Name: course_id_seq; Type: SEQUENCE OWNED BY; Schema: db_info; Owner: postgres
--

ALTER SEQUENCE db_info.course_id_seq OWNED BY db_info.course.course_id;


--
-- Name: groups; Type: TABLE; Schema: db_info; Owner: postgres
--

CREATE TABLE db_info.groups (
    group_id integer NOT NULL,
    name_group character varying NOT NULL,
    teacher_id integer,
    students_id integer
);


ALTER TABLE db_info.groups OWNER TO postgres;

--
-- Name: groups_group_id_seq; Type: SEQUENCE; Schema: db_info; Owner: postgres
--

CREATE SEQUENCE db_info.groups_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE db_info.groups_group_id_seq OWNER TO postgres;

--
-- Name: groups_group_id_seq; Type: SEQUENCE OWNED BY; Schema: db_info; Owner: postgres
--

ALTER SEQUENCE db_info.groups_group_id_seq OWNED BY db_info.groups.group_id;


--
-- Name: students; Type: TABLE; Schema: db_info; Owner: postgres
--

CREATE TABLE db_info.students (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(60) NOT NULL,
    email character varying(100),
    telephone character varying(25)
);


ALTER TABLE db_info.students OWNER TO postgres;

--
-- Name: students_id_seq; Type: SEQUENCE; Schema: db_info; Owner: postgres
--

CREATE SEQUENCE db_info.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE db_info.students_id_seq OWNER TO postgres;

--
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: db_info; Owner: postgres
--

ALTER SEQUENCE db_info.students_id_seq OWNED BY db_info.students.id;


--
-- Name: teachers; Type: TABLE; Schema: db_info; Owner: postgres
--

CREATE TABLE db_info.teachers (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(60) NOT NULL,
    email character varying(100),
    telephone character varying(25),
    specialized character varying(60)
);


ALTER TABLE db_info.teachers OWNER TO postgres;

--
-- Name: teachers_id_seq; Type: SEQUENCE; Schema: db_info; Owner: postgres
--

CREATE SEQUENCE db_info.teachers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE db_info.teachers_id_seq OWNER TO postgres;

--
-- Name: teachers_id_seq; Type: SEQUENCE OWNED BY; Schema: db_info; Owner: postgres
--

ALTER SEQUENCE db_info.teachers_id_seq OWNED BY db_info.teachers.id;


--
-- Name: course course_id; Type: DEFAULT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.course ALTER COLUMN course_id SET DEFAULT nextval('db_info.course_id_seq'::regclass);


--
-- Name: groups group_id; Type: DEFAULT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.groups ALTER COLUMN group_id SET DEFAULT nextval('db_info.groups_group_id_seq'::regclass);


--
-- Name: students id; Type: DEFAULT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.students ALTER COLUMN id SET DEFAULT nextval('db_info.students_id_seq'::regclass);


--
-- Name: teachers id; Type: DEFAULT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.teachers ALTER COLUMN id SET DEFAULT nextval('db_info.teachers_id_seq'::regclass);


--
-- Data for Name: course; Type: TABLE DATA; Schema: db_info; Owner: postgres
--

INSERT INTO db_info.course VALUES (26, 'Python-Developer', NULL);
INSERT INTO db_info.course VALUES (27, 'Java-Developer', NULL);
INSERT INTO db_info.course VALUES (28, '.NET-Developer', NULL);
INSERT INTO db_info.course VALUES (29, 'Learn DS&ML', NULL);
INSERT INTO db_info.course VALUES (30, 'C++ -Developer', NULL);


--
-- Data for Name: groups; Type: TABLE DATA; Schema: db_info; Owner: postgres
--

INSERT INTO db_info.groups VALUES (11, 'Python-Developer', NULL, NULL);
INSERT INTO db_info.groups VALUES (12, 'Python-Developer', NULL, NULL);
INSERT INTO db_info.groups VALUES (13, 'Python-Developer', NULL, NULL);
INSERT INTO db_info.groups VALUES (14, 'Python-Developer', NULL, NULL);
INSERT INTO db_info.groups VALUES (15, 'Python-Developer', NULL, NULL);


--
-- Data for Name: students; Type: TABLE DATA; Schema: db_info; Owner: postgres
--

INSERT INTO db_info.students VALUES (17, 'Oleg', 'Barabanov', 'baraban@gmail.com', '+375291234565');
INSERT INTO db_info.students VALUES (18, 'Afgustin', 'limonov', 'limon@gmail.com', '+375293222131');
INSERT INTO db_info.students VALUES (19, 'Petya', 'Fedorov', 'fedorov.p@gmail.com', '+375291234135');
INSERT INTO db_info.students VALUES (20, 'Alesya', 'Smirnova', 'alesya.smirnova@gmail.com', '+375293453124');
INSERT INTO db_info.students VALUES (21, 'Nina', 'Pavlovec', 'nina.pavl@gmail.com', '+375293453434');


--
-- Data for Name: teachers; Type: TABLE DATA; Schema: db_info; Owner: postgres
--

INSERT INTO db_info.teachers VALUES (41, 'Simen', 'Afanasinov', 'afanasim@gmail.com', '+375291234565', 'Python-Developer');
INSERT INTO db_info.teachers VALUES (42, 'Maksim', 'Geronov', 'maksialt@gmail.com', '+375293222131', 'Java-Developer');
INSERT INTO db_info.teachers VALUES (43, 'Valodya', 'Fedorov', 'valodya.fe@gmail.com', '+375291234135', 'Back-end Developer');
INSERT INTO db_info.teachers VALUES (44, 'Viktoria', 'Cherkasova', 'vik.cher@gmail.com', '+375293453124', 'Frond-end Developer');
INSERT INTO db_info.teachers VALUES (45, 'Sysanna', 'Perepelka', 'sys.anna@gmail.com', '+375293453434', 'GemeDev');


--
-- Name: course_id_seq; Type: SEQUENCE SET; Schema: db_info; Owner: postgres
--

SELECT pg_catalog.setval('db_info.course_id_seq', 30, true);


--
-- Name: groups_group_id_seq; Type: SEQUENCE SET; Schema: db_info; Owner: postgres
--

SELECT pg_catalog.setval('db_info.groups_group_id_seq', 15, true);


--
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: db_info; Owner: postgres
--

SELECT pg_catalog.setval('db_info.students_id_seq', 21, true);


--
-- Name: teachers_id_seq; Type: SEQUENCE SET; Schema: db_info; Owner: postgres
--

SELECT pg_catalog.setval('db_info.teachers_id_seq', 45, true);


--
-- Name: groups groups_pk; Type: CONSTRAINT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.groups
    ADD CONSTRAINT groups_pk PRIMARY KEY (group_id);


--
-- Name: course key_name; Type: CONSTRAINT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.course
    ADD CONSTRAINT key_name PRIMARY KEY (course_id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- Name: teachers teachers_pkey; Type: CONSTRAINT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.teachers
    ADD CONSTRAINT teachers_pkey PRIMARY KEY (id);


--
-- Name: groups foreign_key_name; Type: FK CONSTRAINT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.groups
    ADD CONSTRAINT foreign_key_name FOREIGN KEY (students_id) REFERENCES db_info.students(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: course foreign_key_name; Type: FK CONSTRAINT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.course
    ADD CONSTRAINT foreign_key_name FOREIGN KEY (group_id) REFERENCES db_info.groups(group_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: groups foreign_key_name2; Type: FK CONSTRAINT; Schema: db_info; Owner: postgres
--

ALTER TABLE ONLY db_info.groups
    ADD CONSTRAINT foreign_key_name2 FOREIGN KEY (teacher_id) REFERENCES db_info.teachers(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

