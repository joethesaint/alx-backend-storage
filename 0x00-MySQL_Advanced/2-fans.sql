-- ranks country origins of bands and their total number of fans in DESC order
-- columns name must be origin and nb_fans

SELECT origin,
    SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
