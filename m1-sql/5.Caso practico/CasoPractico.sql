-- 1. Crear base de datos
DROP schema IF exists `m1_caso_practico`;
CREATE SCHEMA `m1_caso_practico`;
USE `m1_caso_practico`;
-- Opción 1: clientes, productos, pedidos, detalles_pedidos

CREATE TABLE `clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `telefono` int DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
);
CREATE TABLE `productos` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `articulo` varchar(250) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `precio` decimal(12,2) DEFAULT NULL,
  `id_cliente` int DEFAULT NULL,
  `stock` int,
  PRIMARY KEY (`id_producto`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`) -- añadir fk a columna id_cliente de productos
);

ALTER TABLE productos add stock int;

-- https://dev.mysql.com/doc/refman/8.0/en/integer-types.html
CREATE TABLE pedidos (
	id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    nif VARCHAR(9),
    email VARCHAR(50) UNIQUE,
    fecha DATE,
    codigo_postal VARCHAR(5),
    UNIQUE KEY `pedidos_nif_unique` (`nif`)
);

CREATE TABLE `detalles_pedido` (
  `id_detalles_pedido` int NOT NULL AUTO_INCREMENT,
  `id_producto` int DEFAULT NULL,
  `id_pedido` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`id_detalles_pedido`),
  KEY `id_producto` (`id_producto`),
  KEY `id_pedido` (`id_pedido`),
  CONSTRAINT `detalles_pedido_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`),
  CONSTRAINT `detalles_pedido_ibfk_2` FOREIGN KEY (`id_pedido`) REFERENCES `pedidos` (`id_pedido`)
);

select * from clientes;
select * from productos;
select * from pedidos;
select * from detalles_pedido;


INSERT INTO clientes (nombre, apellidos, fecha_nacimiento, email, telefono, direccion) 
VALUES 
('andres', 'andrade', '1970-01-01', 'cliente1@tecno.es', '601010101', 'calle de la alegria'),
('lalo', 'lima', '1980-02-02', 'cliente2@tecno.es', '601010102', 'calle de la euforia'),
('hernando', 'hernandez', '1990-03-03', 'cliente3@tecno.es', '601010103', 'calle de la esperanza'),
('fernando', 'fernandez', '2000-04-04', 'cliente4@tecno.es', '601010104', 'calle de la satisfaccion'),
('armando', 'torres de la luz', '1960-05-05', 'cliente5@tecno.es', '601010105', 'calle del aprendizaje'),
('martina', 'martinez', '1996-06-09', 'cliente6@tecno.es', '601010106','calle de las oportunidades')
;
INSERT INTO productos (articulo, descripcion, category, precio, id_cliente, stock) VALUES
('consolas de videojuegos', 'play station 5', 'tecnologia', 700.99, 2, 50),
('celular_telefono_movil', 'iphon 14', 'Tecnologia', 850.99, 4, 80),
('computadora', 'hp pavilion', 'tecnologia', 800.99, 2, 10),
('smartwatch', 'reloj sony','tecnologia', 640.99, 6, 7),
('televisores', 'sony', 'tecnologia', 1005.99, 2, 8),
('tablets', 'ipad', 'tecnologia',1999.99, 1, 2),
('televisores', 'panasonic', 'tecnologia', 259.99, 3, 12),
('consolas de videojuegos', 'xbox serie x', 'tecnologia', 700.99, 3, 20),
('celular_telefono_movil', 'iphon 13', 'Tecnologia', 850.99, 5, 10),
('computadora', 'hp pavilion', 'tecnologia', 800.99, 2, 20),
('smartwatch', 'reloj sony','tecnologia', 640.99, 3, 10),
('televisores', 'sony', 'tecnologia', 1005.99, 4, 10),
('tablets', 'ipad', 'tecnologia',1999.99, 6, 10),
('televisores', 'panasonic', 'tecnologia', 259.99, 6, 8);




INSERT INTO pedidos (nif, email, fecha, codigo_postal) VALUES
('000000A', 'cliente1@tecno.es', '2023-01-01', '28003'),
('111111B', 'cliente2@tecno.es', '2023-01-01', '28002'),
('222222C', 'cliente3@tecno.es', '2023-02-01', '28025'),
('333333D', 'cliente4@tecno.es', '2023-02-01', '28024'),
('444444E', 'cliente5@tecno.es', '2023-03-01', '28024'),
('555555G', 'cliente6@tecno.es', '2023-03-01', '28026'),
('666666H', 'cliente7@tecno.es', '2023-05-01', '28030')
;

INSERT INTO `m1_caso_practico`.`detalles_pedido` (`fecha`) VALUES
('2023-01-17'),
('2023-01-10'),
('2023-01-10'),
('2023-02-10'),
('2023-02-10'),
('2023-02-10'),
('2023-03-10'),
('2023-01-10'),
('2023-04-10'),
('2023-02-10'),
('2023-04-10'),
('2023-04-10'),
('2023-01-10'),
('2023-03-10'),
('2023-02-10');
;


-- Consultas
-- Mostrar todos los clientes ordenados alfabéticamente por apellido.
select * from clientes;
select * from clientes ORDER BY apellidos asc;
select * from clientes ORDER BY apellidos desc;

-- Mostrar todos los productos con un stock inferior a 10.
select * from productos;
select * from productos where stock <10;

-- Mostrar todos los productos con un stock inferior a 200.
select * from productos;
select * from productos where stock <200;

-- Mostrar todos los pedidos realizados por un cliente específico (por id_cliente).
select * from pedidos;
select id_cliente, count(*) from pedidos  group by id_cliente;

-- Mostrar el total de ventas (precio * cantidad) por cada pedido.
select dp.id_pedido, sum((pd.precio * dp.cantidad)) as total_ventas
from detalles_pedido as dp
inner join pedidos as p on p.id_pedido = dp.id_pedido
inner join productos as pd on pd.id_producto = dp.id_producto
group by dp.id_pedido;

select * from product;
select u.id, u.email, p.name from user u left join product p on u.id = p.created_by;
select u.id, u.email, p.name from user u right join product p on u.id = p.created_by;
select u.id, u.email, p.name from user u inner join product p on u.id = p.created_by;
select u.id, u.name, p.id, p.name from user u cross	join product p;
 
 select count(id), marca from product group by marca;
 select count(p.id), u.name from product p left join user u on u.id = p.created_by group by p.created_by;
 
 select count(p.id), u.name from product p left join user u 
 on u.id = p.created_by group by p.created_by
 having count(p.id) >= 2;
 
-- Mostrar el pedido con la mayor cantidad de productos diferentes.




-- Mostrar el pedido con la mayor cantidad de productos diferentes.