Copy(SELECT c.contentid, c.title
FROM CONTENT c
JOIN BODYCONTENT bc
    ON c.contentid = bc.contentid
JOIN SPACES s
    ON c.spaceid = s.spaceid
WHERE c.prevver IS NULL
    AND c.contenttype IN ('PAGE', 'BLOGPOST')
    AND bc.body LIKE '%/WORDSGOHERE/%') To '/tmp/test.csv' With CSV DELIMITER ',';
