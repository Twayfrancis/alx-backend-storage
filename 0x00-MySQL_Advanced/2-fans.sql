-- script that ranks county origin of bands, ordered by num of (non-unique) fans
-- column names must be: origin and nb_fans

SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
