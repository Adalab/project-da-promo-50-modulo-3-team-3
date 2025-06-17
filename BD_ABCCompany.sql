USE abccorporation;

CREATE TABLE IF NOT EXISTS info_personal (
    employeenumber INT PRIMARY KEY,
    datebirth YEAR,
    age INT,
    gender VARCHAR(5),
    education INT,
    maritalstatus VARCHAR(100),
    distancefromhome INT
);

CREATE TABLE IF NOT EXISTS salario (
    employeenumber INT PRIMARY KEY,
    monthlyrate INT,
    percentsalaryhike INT,
    salary INT,
    FOREIGN KEY (employeenumber) REFERENCES info_personal(employeenumber)
);

CREATE TABLE IF NOT EXISTS educacion (
    employeenumber INT PRIMARY KEY,
    education INT,
    educationfield VARCHAR(200),
    FOREIGN KEY (employeenumber) REFERENCES info_personal(employeenumber)
);

CREATE TABLE IF NOT EXISTS experiencia_laboral (
    employeenumber INT PRIMARY KEY,
    totalworkingyears INT,
    yearsatcompany INT,
    yearsincurrentrole INT,
    yearssincelastpromotion INT,
    yearswithcurrmanager INT,
    numcompaniesworked INT,
    FOREIGN KEY (employeenumber) REFERENCES info_personal(employeenumber)
);

CREATE TABLE IF NOT EXISTS datos_company (
    employeenumber INT PRIMARY KEY,
    joblevel VARCHAR(5),
    jobrole VARCHAR(500),
    department VARCHAR(500),
    businesstravel VARCHAR(50),
    salary INT,
    FOREIGN KEY (employeenumber) REFERENCES info_personal(employeenumber)
);

CREATE TABLE IF NOT EXISTS beneficios (
    employeenumber INT PRIMARY KEY,
    standardhours VARCHAR(500),
    remotework VARCHAR(10),
    trainingtimeslastyear INT,
    stockoptionlevel INT,
    FOREIGN KEY (employeenumber) REFERENCES info_personal(employeenumber)
);

CREATE TABLE IF NOT EXISTS evaluaciones_empleado (
    employeenumber INT PRIMARY KEY,
    jobsatisfaction INT,
    environmentsatisfaction INT,
    relationshipsatisfaction INT,
    worklifebalance INT,
    jobinvolvement INT,
    FOREIGN KEY (employeenumber) REFERENCES info_personal(employeenumber)
);

CREATE TABLE IF NOT EXISTS evaluaciones_empresa (
    employeenumber INT PRIMARY KEY,
    performancerating INT,
    FOREIGN KEY (employeenumber) REFERENCES info_personal(employeenumber)
);

CREATE TABLE IF NOT EXISTS horario (
    employeenumber INT PRIMARY KEY,
    overtime VARCHAR(10),
    standardhours VARCHAR(500),
    salary INT
);
