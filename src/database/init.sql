create table productos(
    id int auto_increment,
    nombre varchar(255),
    precio decimal(18,2),
    primary key (id)
);

insert into productos (nombre,precio) 
values ('camiseta',9.08),('pantalon',6.65);

create table users(
    id int auto_increment,
    username varchar(255),
    password varchar(255),
    primary key (id)
);

insert into users (username,password) 
values ('user1','12345'),('user2','54321');