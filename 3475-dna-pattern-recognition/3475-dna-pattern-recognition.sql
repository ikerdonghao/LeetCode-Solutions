# Write your MySQL query statement below
SELECT
    sample_id,
    dna_sequence,
    species,
    CASE WHEN REGEXP_LIKE(dna_sequence,'^ATG','c') THEN 1 ELSE 0 END AS has_start,
    CASE WHEN REGEXP_LIKE(dna_sequence,'(TAA|TAG|TGA)$','c') THEN 1 ELSE 0 END AS has_stop,
    CASE WHEN REGEXP_LIKE(dna_sequence,'ATAT','c') THEN 1 ELSE 0 END AS has_atat,
    CASE WHEN REGEXP_LIKE(dna_sequence,'GGG','c') THEN 1 ELSE 0 END AS has_ggg
from Samples
ORDER BY sample_id