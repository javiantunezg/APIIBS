-- Tabla que almacena los tipos de usuario, como Superadministrador, Organizador y Usuario
CREATE TABLE UserTypes (
    idUserType INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL
);

-- Inserción de tipos de usuario por defecto
INSERT INTO UserTypes (name, description) VALUES 
('Superadministrator', 'Superadministrador con acceso completo'),
('Organizer', 'Organizador de eventos con permisos de gestión'),
('User', 'Usuario regular con acceso limitado');

-- -----------------------------------------------------

-- Tabla que almacena los detalles de los usuarios, incluyendo información personal y de contacto
CREATE TABLE users (
    idUser INT AUTO_INCREMENT PRIMARY KEY,
    apiUserId INT NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    dni VARCHAR(20) NOT NULL UNIQUE,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    birthDate DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    createdBy INT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedBy INT,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    isActive BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (apiUserId) REFERENCES apiuser(idApiUser),
    FOREIGN KEY (createdBy) REFERENCES apiuser(idApiUser),
    FOREIGN KEY (updatedBy) REFERENCES apiuser(idApiUser)
);

-- -----------------------------------------------------

-- Tabla que almacena la información de los usuarios para autenticación y seguimiento de accesos
CREATE TABLE apiuser (
    idApiUser INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    passwordHash VARCHAR(255) NOT NULL,
    loginCount INT DEFAULT 0,
    lastLogin TIMESTAMP NULL,
    idUserType INT NOT NULL,
    createdBy INT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedBy INT,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (idUserType) REFERENCES UserTypes(idUserType),
    FOREIGN KEY (createdBy) REFERENCES apiuser(idApiUser),
    FOREIGN KEY (updatedBy) REFERENCES apiuser(idApiUser),
    status INT
);

-- -----------------------------------------------------

-- Tabla que almacena los tipos de eventos que se pueden gestionar en la aplicación
CREATE TABLE EventTypes (
    idEventType INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL,
    createdBy INT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedBy INT,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (createdBy) REFERENCES apiuser(idApiUser),
    FOREIGN KEY (updatedBy) REFERENCES apiuser(idApiUser)
);

-- -----------------------------------------------------

-- Tabla que almacena los eventos, incluyendo detalles como nombre, descripción, fechas y organizador
CREATE TABLE events (
    idEvent INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    idEventType INT NOT NULL,
    organizerId INT NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    startRegistration DATE NOT NULL,
    endRegistration DATE NOT NULL,
    createdBy INT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedBy INT,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (idEventType) REFERENCES EventTypes(idEventType),
    FOREIGN KEY (organizerId) REFERENCES apiuser(idApiUser),
    FOREIGN KEY (createdBy) REFERENCES apiuser(idApiUser),
    FOREIGN KEY (updatedBy) REFERENCES apiuser(idApiUser)
);

-- -----------------------------------------------------

-- Tabla que almacena los campos de inscripción personalizados para cada evento
CREATE TABLE eventregistrationfields (
    idField INT AUTO_INCREMENT PRIMARY KEY,
    idEvent INT NOT NULL,
    fieldName VARCHAR(100) NOT NULL,
    fieldType VARCHAR(50) NOT NULL,
    isRequired BOOLEAN DEFAULT FALSE,
    createdBy INT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedBy INT,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (idEvent) REFERENCES events(idEvent),
    FOREIGN KEY (createdBy) REFERENCES apiuser(idApiUser),
    FOREIGN KEY (updatedBy) REFERENCES apiuser(idApiUser)
);

-- -----------------------------------------------------

-- Tabla que almacena las inscripciones de los usuarios a los eventos, incluyendo datos personalizados de registro
CREATE TABLE registrations (
    idRegistration INT AUTO_INCREMENT PRIMARY KEY,
    idEvent INT NOT NULL,
    idUser INT NOT NULL,
    registrationData JSON NOT NULL,
    createdBy INT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedBy INT,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (idEvent) REFERENCES events(idEvent),
    FOREIGN KEY (idUser) REFERENCES users(idUser),
    FOREIGN KEY (createdBy) REFERENCES apiuser(idApiUser),
    FOREIGN KEY (updatedBy) REFERENCES apiuser(idApiUser)
);
