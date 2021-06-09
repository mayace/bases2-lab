-- drop table elecciones.voto;
-- drop table elecciones.acta;
-- drop table elecciones.eleccion;
-- drop table elecciones.partido;
-- drop table elecciones.municipio;
-- drop table elecciones.departamento;


create table elecciones.departamento(
	codigo_depto number not null, 
	nombre_depto varchar(100), 
	constraint depta_pk primary key (codigo_depto)
) tablespace eleccionestbs ;


select  * from elecciones.departamento ;

create table elecciones.municipio(
	codigo_muni number not null, 
	depto_muni number not null, 
	nombre_muni varchar(100), 
	constraint muni_pk primary key (codigo_muni, depto_muni),
	constraint depto_muni_fk
    foreign key (depto_muni)
    references elecciones.departamento(codigo_depto)
) tablespace eleccionestbs;


select  * from elecciones.municipio ;

create table elecciones.partido(
	codigo_part number not null, 
	nombre_part varchar(100), 
	constraint part_pk primary key (codigo_part)
) tablespace eleccionestbs;


select * from elecciones.partido;

create  table elecciones.eleccion(
	codigo_ele number not null, 
	nombre_ele varchar(100), 
	constraint ele_pk primary key (codigo_ele)
) tablespace eleccionestbs;


select  * from elecciones.eleccion ;

create table elecciones.acta(
	numero_mesa number not null, 
	tipo_eleccion number not null, 
	departamento number not null,
	municipio number not null, 
	papeletas_recibidas number, 
	total_votos_validos number, 
	votos_nulos number, 
	votos_blanco number, 
	votos_validos_emitidos  number,
	votos_invalidos number, 
	imagen blob, 
	estado_imagen varchar(3), -- val, anu, act
	cuadra_acta varchar(1), -- s o n 
	conteo_impugna number, 
	conteo_inscritos number, 
	stacta varchar(3), -- val, anu, act
	stescan varchar(3), 
	stsfisic varchar(3), 
	ststrans varchar(3),
	constraint acta_pk primary key (numero_mesa, tipo_eleccion),
	constraint depto_acta_fk
    foreign key (departamento, municipio)
    references elecciones.municipio(depto_muni, codigo_muni),
	constraint ele_acta_fk
    foreign key (tipo_eleccion)
    references elecciones.eleccion(codigo_ele)
) tablespace eleccionestbs;




select  * from elecciones.acta;

create table elecciones.voto(
	voto_partido number not null, 
	voto_mesa number not null, 
	voto_eleccion number not null, 
	voto_cantidad number,
	constraint voto_pk primary key (voto_partido, voto_mesa, voto_eleccion),
	constraint partido_voto_fk
    foreign key (voto_partido)
    references elecciones.partido(codigo_part),
	constraint acta_voto_fk
    foreign key (voto_mesa, voto_eleccion)
    references elecciones.acta(numero_mesa, tipo_eleccion)
) tablespace eleccionestbs;


select * from elecciones.voto;


-- creacion de vista
-- danto privilegios personal, porque por lo no funciona
grant select on elecciones.DEPARTAMENTO to guest1;
grant select on elecciones.MUNICIPIO to guest1;
grant select on elecciones.PARTIDO to guest1;
grant select on elecciones.ELECCION to guest1;
grant select on elecciones.ACTA to guest1;
grant select on elecciones.VOTO to guest1;

create view guest1.VOTOSPRESIDENTE as
select 
d.nombre_depto as Departamento, 
m.nombre_muni as Municipio, 
p.nombre_part as Partido ,
sum(v.voto_cantidad) as "No. Votos"
from elecciones.voto v
inner join elecciones.acta a on a.numero_mesa = v.voto_mesa and a.tipo_eleccion = v.voto_eleccion and a.tipo_eleccion = 1
inner join elecciones.municipio m on m.codigo_muni = a.municipio and m.depto_muni = a.departamento
inner join elecciones.departamento d on d.codigo_depto = m.depto_muni
inner join elecciones.partido p on p.codigo_part = v.voto_partido
group by d.nombre_depto, m.nombre_muni, p.nombre_part
order by 1,2,3
;



select owner, view_name from sys.all_views where owner in ('ELECCIONES', 'SYSTEM', 'GUEST1', 'MAYACE');