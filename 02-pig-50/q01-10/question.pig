-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
-- Escriba el resultado a la carpeta `output` del directorio actual.
--
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
--fs -put data.tsv

data = LOAD 'data.tsv' USING PigStorage('\t')
    AS (letra:CHARARRAY,
        fecha:CHARARRAY,
        val:INT);
        
g = GROUP data BY $0;

count = FOREACH g GENERATE group, COUNT(data);

STORE count INTO 'output' USING PigStorage('\t');