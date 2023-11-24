
create database  if not exists olimpiadas;

use olimpiadas;

create table if not exists Olimpiada(
	id integer auto_increment primary key,
	year_olimpiada integer not null,
    check(year_olimpiada > 0)
);

create table if not exists Pais(
	id integer auto_increment primary key,
    nombre varchar(150) not null
);

create table if not exists Genero(
	id integer auto_increment primary key,
    nombre varchar(150) not null
);

create table if not exists Resultados(
	idOlimpiada integer,
    idPais integer,
    idGenero integer,
    oro integer not null check(oro>0),
    plata integer not null check(plata>0),
    bronce integer not null check(bronce>0),
    primary key(idOlimpiada, idPais, idGenero),
    foreign key (idOlimpiada) references Olimpiada(id),
    foreign key (idPais) references Pais(id),
    foreign key (idGenero) references Genero(id)
    
)
