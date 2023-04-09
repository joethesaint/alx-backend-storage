-- create an index
-- first letter of the name an score

CREATE INDEX idx_name_first_score
ON names (
    name(1),
    score
);
