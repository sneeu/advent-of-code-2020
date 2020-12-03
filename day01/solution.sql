-- Create a table to store the input
CREATE TABLE aoc2020_day01 (
    n INTEGER
);

-- Load the input
\COPY aoc2020_day01 FROM 'input.txt';

-- A “naïve” O(n^2) CROSS JOIN for part 1
SELECT
    a.n AS a,
    b.n AS b,
    a.n + b.n AS sum,
    a.n * b.n AS product
FROM
    aoc2020_day01 a
CROSS JOIN
    aoc2020_day01 b
WHERE
    a.n + b.n = 2020
;


-- Although it turns out that the EXPLAIN on the `CROSS JOIN` is the same as the `INNER
-- JOIN`:
SELECT
    a.n AS a,
    b.n AS b,
    a.n + b.n AS sum,
    a.n * b.n AS product
FROM
    aoc2020_day01 a
INNER JOIN aoc2020_day01 b ON (a.n + b.n = 2020)
;

-- I recently learned about `LATERAL` so let’s it them out
SELECT
    a.n AS a,
    b.n AS b,
    c.n AS c,
    a.n + b.n + c.n AS sum,
    a.n * b.n * c.n AS product
FROM
    aoc2020_day01 a,
    LATERAL (
        SELECT n
        FROM aoc2020_day01 b
        WHERE a.n + b.n < 2020
    ) b,
    LATERAL (
        SELECT n
        FROM aoc2020_day01 c
        WHERE a.n + b.n + c.n = 2020
    ) c
;

-- In this case, the EXPLAIN for the LATERAL is the same as that for the `INNER JOIN`:
SELECT
    a.n AS a,
    b.n AS b,
    c.n AS c,
    a.n + b.n + c.n AS sum,
    a.n * b.n * c.n AS product
FROM
    aoc2020_day01 a
    INNER JOIN aoc2020_day01 b ON (a.n + b.n < 2020)
    INNER JOIN aoc2020_day01 c ON (a.n + b.n + c.n = 2020)
;
