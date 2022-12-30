CREATE DATABASE dagidb;

\c dagidb;

CREATE TABLE employees(
  id serial PRIMARY KEY, name VARCHAR ( 50 ) ,
  surname VARCHAR ( 50 ) , age VARCHAR ( 50 ) ,
  email VARCHAR ( 50 ) UNIQUE NOT NULL 
);
