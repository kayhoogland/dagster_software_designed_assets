{{ config(materialized='table') }}

SELECT
    char,
    SUBSTR(timestamp, 1, 8) as day,
    COUNT(char) as count
FROM {{ source('main', 'avatar_history') }}
GROUP BY char, SUBSTR(timestamp, 1, 8);
