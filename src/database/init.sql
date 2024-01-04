create table productos(
    id int auto_increment,
    nombre varchar(255),
    precio decimal(18,2),
    primary key (id)
);

insert into productos (nombre,precio) 
values ('camiseta',9.08),('pantalon',6.65);