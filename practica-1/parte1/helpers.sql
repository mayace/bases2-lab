-- tablespace
select  tablespace_name, status, contents
from user_tablespaces;;

select * from dba_data_files where tablespace_name = 'ELECCIONESTBS';

-- tablas en schema
select owner, object_name from dba_objects where object_type = 'TABLE' and owner in('EQUIPOS','JORNADAS');