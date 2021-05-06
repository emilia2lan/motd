GRANT ALL PRIVILEGES ON DATABASE motd TO motd;

CREATE TABLE IF NOT EXISTS random_greeting (greets VARCHAR);

CREATE TABLE IF NOT EXISTS user_greeting (user_name VARCHAR, greetings VARCHAR);