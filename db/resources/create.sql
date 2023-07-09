-- create table
CREATE TABLE random_no(
  time TIMESTAMPTZ NOT NULL,
  event TEXT NOT NULL,
  number DOUBLE PRECISION NULL
);

-- create hypertable (for timescaledb)
SELECT create_hypertable('random_no','time');

-- create indices
CREATE INDEX ix_symbol_time ON random_no (event, time DESC);