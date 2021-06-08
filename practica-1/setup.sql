

-- creacion de tablespace
create tablespace ELECCIONESTBS
datafile 'C:\Users\ce2\Downloads\bases2-lab\ELECCIONESDTF.tbs' size 250M
    autoextend on
    maxsize 500M;

alter database datafile 'C:\Users\ce2\Downloads\bases2-lab\ELECCIONESDTF.tbs'
    autoextend off;


-- creacion de scheme
create user elecciones identified by elecciones14;
alter user elecciones quota unlimited on eleccionestbs;

-- roles
create role guest;
grant create session to guest;
grant select on elecciones.DEPARTAMENTO to guest;
grant select on elecciones.MUNICIPIO to guest;
grant select on elecciones.PARTIDO to guest;
grant select on elecciones.ELECCION to guest;
grant select on elecciones.ACTA to guest;
grant select on elecciones.VOTO to guest;

create role mesas;
grant create session to mesas;
grant select on elecciones.DEPARTAMENTO to mesas;
grant select on elecciones.MUNICIPIO to mesas;
grant select on elecciones.PARTIDO to mesas;
grant select on elecciones.ELECCION to mesas;
grant select on elecciones.ACTA to mesas;
grant select on elecciones.VOTO to mesas;

grant insert on elecciones.DEPARTAMENTO to mesas;
grant insert on elecciones.MUNICIPIO to mesas;
grant insert on elecciones.PARTIDO to mesas;
grant insert on elecciones.ELECCION to mesas;
grant insert on elecciones.ACTA to mesas;
grant insert on elecciones.VOTO to mesas;

create role it;
grant create session to it;
grant create table to it;
grant create user to it;

grant select on elecciones.DEPARTAMENTO to it;
grant select on elecciones.MUNICIPIO to it;
grant select on elecciones.PARTIDO to it;
grant select on elecciones.ELECCION to it;
grant select on elecciones.ACTA to it;
grant select on elecciones.VOTO to it;


create role admin;
grant create session to admin;
grant create user to admin;

grant select, update, insert, delete on elecciones.DEPARTAMENTO to admin;
grant select, update, insert, delete on elecciones.MUNICIPIO to admin;
grant select, update, insert, delete on elecciones.PARTIDO to admin;
grant select, update, insert, delete on elecciones.ELECCION to admin;
grant select, update, insert, delete on elecciones.ACTA to admin;
grant select, update, insert, delete on elecciones.VOTO to admin;


-- creacion de usuarios
create user guest1 identified by guest1;
create user guest2 identified by guest2;
create user guest3 identified by guest3;


grant guest to guest1;
grant guest to guest2;
grant guest to guest3;


create user mesas1 identified by mesas1;
create user mesas2 identified by mesas2;
create user mesas3 identified by mesas3;
create user mesas4 identified by mesas4;

grant mesas to mesas1;
grant mesas to mesas2;
grant mesas to mesas3;
grant mesas to mesas4;


-- insert into elecciones.departamento select 1, 'depto from mesas1' from dual;


create user it1 identified by it1;
create user it2 identified by it2;
create user it3 identified by it3;

grant it to it1;
grant it to it2;
grant it to it3;


create user admin1 identified by admin1;
create user admin2 identified by admin2;

grant admin to admin1;
grant admin to admin2;

