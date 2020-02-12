-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

lines = LOAD 'data.tsv'
    AS (letra:CHARARRAY, 
        fecha:CHARARRAY,  
        valor:INT);
    
ordenar = ORDER lines BY $2;

aux = LIMIT ordenar 5;

l = FOREACH aux GENERATE $2;

STORE l INTO 'output';