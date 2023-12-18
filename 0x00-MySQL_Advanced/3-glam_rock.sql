-- script that lists all bands with Glam rock as their main style, ranked by their longetivity
-- import this table metal_bands.sql
-- column names must be: band_name and lifespan use 2022
-- should use attribute formed and split for computing lifespan

SELECT band_name, COALESCE(split, 2022) - formed as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
