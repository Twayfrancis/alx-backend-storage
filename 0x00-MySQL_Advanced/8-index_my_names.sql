-- script that creates an index idx_name_first on the tables names and the first letter of name
-- import table dump: name.sql.zip
-- only first letter of name must be indexed

CREATE INDEX idx_name_first
ON names(name(1));
