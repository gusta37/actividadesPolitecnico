USE proyect1;
CREATE TABLE productos(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    precio DOUBLE NOT NULL,
    stock INT,
    categoria VARCHAR(100)
);
DROP TABLE productos;
CREATE TABLE productos(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    precio DOUBLE NOT NULL,
    stock INT,
    categoria VARCHAR(100)
);

INSERT INTO productos (nombre, marca, precio, stock, categoria) VALUES 
    ('Coca Cola', 'Coca Cola', 2.00, 5, 'bebidas'),
    ('Fanta', 'Coca Cola', 2.00, 5, 'bebidas'),
    ('Pepsi', 'Coca Cola', 2.00, 5, 'bebidas'),
    ('Sprite', 'Coca Cola', 2.00, 5, 'bebidas'),
    ('Cerveza', 'Coca Cola', 2.00, 5, 'bebidas'),
    ('Agua', 'Coca Cola', 2.00, 5, 'bebidas');