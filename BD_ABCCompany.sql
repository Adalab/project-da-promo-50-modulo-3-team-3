USE abccorporation;

CREATE TABLE IF NOT EXISTS info_personal (
employee_number INT PRIMARY KEY,
date_birth YEAR,
age INT,
gender VARCHAR(5),
education VARCHAR(100),
marital_status VARCHAR(100),
distance_home INT);

CREATE TABLE IF NOT EXISTS salario (
employee_number INT PRIMARY KEY,
monthly_rate INT,
percent_salary_hike INT,
salary INT);

ALTER TABLE info_personal ADD UNIQUE (education);

CREATE TABLE IF NOT EXISTS educacion (
employee_number INT PRIMARY KEY,
education VARCHAR(100),
education_field VARCHAR(200),
FOREIGN KEY (education) REFERENCES info_personal(education));

CREATE TABLE IF NOT EXISTS experiencia_laboral (
employee_number INT PRIMARY KEY,
total_working_years INT,
years_at_company INT,
years_current_role INT,
years_last_promotion INT,
year_current_manager INT,
num_companys_worked INT);

ALTER TABLE salario ADD UNIQUE (salary);

CREATE TABLE IF NOT EXISTS datos_company (
employee_number INT PRIMARY KEY,
job_level VARCHAR(5),
job_role VARCHAR(500),
department VARCHAR(500),
business_travel VARCHAR(50),
salary INT,
FOREIGN KEY (salary) REFERENCES salario(salary));

CREATE TABLE IF NOT EXISTS beneficios (
employee_number INT PRIMARY KEY,
standard_hours VARCHAR(500),
remote_work VARCHAR(10),
training_times_last_year INT,
stock_option_level INT);

CREATE TABLE IF NOT EXISTS evaluaciones_empleado (
employee_number INT PRIMARY KEY,
job INT,
enviroment INT,
relationship INT,
worklife_balance INT,
involvement INT);

CREATE TABLE IF NOT EXISTS evaluaciones_empresa (
employee_number INT PRIMARY KEY,
performance_rating INT);

CREATE TABLE IF NOT EXISTS horario (
employee_number INT PRIMARY KEY,
overtime VARCHAR(10),
standard_hours VARCHAR(500),
salary INT,
FOREIGN KEY (salary) REFERENCES salario(salary));

CREATE TABLE IF NOT EXISTS renuncias (
employee_number INT PRIMARY KEY,
attrition VARCHAR(10));




    