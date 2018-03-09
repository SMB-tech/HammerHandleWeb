------------------------------
-- CREATE ROLE AND DATABASE --
------------------------------
DROP USER hammer;
CREATE ROLE hammer WITH LOGIN CREATEDB SUPERUSER PASSWORD 'hammerhandle';
CREATE DATABASE hammerhandle OWNER hammer;

-------------------
-- CREATE TABLES --
-------------------
CREATE TABLE race (
  rce_id SERIAL PRIMARY KEY,
  rce_name TEXT NOT NULL,
  rce_description TEXT NOT NULL
);

CREATE TABLE class (
  cls_id SERIAL PRIMARY KEY,
  cls_name TEXT NOT NULL
);

CREATE TABLE unit (
  uni_id SERIAL PRIMARY KEY,
  uni_name TEXT NOT NULL,
  uni_description TEXT NOT NULL
);

CREATE TABLE unit_rule (
  url_id SERIAL PRIMARY KEY,
  url_name TEXT NOT NULL,
  url_descripction TEXT NOT NULL
);

CREATE TABLE unit_boss (
  ubo_id SERIAL PRIMARY KEY,
  ubo_name TEXT NOT NULL,
  ubo_description TEXT NOT NULL
);
